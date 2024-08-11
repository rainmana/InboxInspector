import streamlit as st
import requests
import json
import pandas as pd
from io import StringIO
import time
from datetime import datetime

# Function to extract domain from email address
def extract_domain(email):
    return email.split('@')[-1]

# Function to query VirusTotal API for domain analysis results
def query_virustotal_domain(domain, api_key, rate_limit=False):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"x-apikey": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Rate limiting
        if rate_limit:
            time.sleep(15)  # Wait 15 seconds to ensure 4 requests per minute
        
        return response.json()
    except requests.exceptions.HTTPError as err:
        st.error(f"HTTP error occurred: {err}")
        return None
    except Exception as err:
        st.error(f"An error occurred: {err}")
        return None

# Function to extract analysis results from the JSON response
def extract_analysis_results(data):
    if not data:
        st.error("No data provided.")
        return None
    
    attributes = data.get('data', {}).get('attributes', {})
    
    analysis_results = {
        'domain': data.get('data', {}).get('id', ''),
        'last_analysis_stats': attributes.get('last_analysis_stats', {}),
        'reputation': attributes.get('reputation', 0),
        'registrar': attributes.get('registrar', ''),
        'creation_date': attributes.get('creation_date', ''),
        'last_update_date': attributes.get('last_update_date', ''),
        'last_analysis_date': attributes.get('last_analysis_date', ''),
        'tags': attributes.get('tags', []),
        'categories': attributes.get('categories', {}),
        'total_votes': attributes.get('total_votes', {}),
        'last_dns_records': attributes.get('last_dns_records', []),
        'last_https_certificate': attributes.get('last_https_certificate', {}),
    }
    
    return analysis_results

# Main function to run the Streamlit app
def main():
    st.title("InboxInspector")
    st.write("""
    *A simple email address domain querying tool by [Rainmana (Alec Akin)](https://github.com/rainmana)*         
             """)

    api_key = st.text_input("Enter your VirusTotal API Key:", type="password", help="You can use the [following](https://www.virustotal.com/gui/my-apikey) link to get your VirusTotal API key")
    uploaded_file = st.file_uploader("Choose a CSV file with email addresses", type=['csv'], help="Single column CSV file with header of 'email' and one email address per line.")
    rate_limit = st.checkbox("Enable rate limiting (4 requests per minute)", value=True, help="Note: Check this box if you use VirusTotal's API free tier. Enterprise customers shouldn't need this setting.")

    if st.button("Analyze"):
        if not api_key:
            st.warning("Please enter your VirusTotal API Key.")
        elif not uploaded_file:
            st.warning("Please upload a CSV file.")
        else:
            # Read the uploaded CSV file
            df = pd.read_csv(uploaded_file)
            
            # Ensure there's a column for email addresses
            if 'email' not in df.columns:
                st.error("The CSV file must contain a column labeled 'email'.")
                return
            
            results = []
            for index, row in df.iterrows():
                email = row['email']
                domain = extract_domain(email)
                
                # Query VirusTotal for domain analysis
                api_response = query_virustotal_domain(domain, api_key, rate_limit)
                
                if api_response:
                    analysis_result = extract_analysis_results(api_response)
                    if analysis_result:
                        results.append({
                            "email": email,
                            "domain": domain,
                            **analysis_result
                        })
                    else:
                        st.error(f"Failed to extract analysis results for {domain}.")
                else:
                    st.error(f"Failed to retrieve data from VirusTotal API for {domain}.")
            
            # Create a structured JSON output
            output_data = {
                "metadata": {
                    "run_date": datetime.now().isoformat(),
                    "input_file": uploaded_file.name,
                    "records_processed": len(df),
                    "successful_lookups": len(results)
                },
                "results": results
            }
            
            # Convert structured data to JSON
            json_output = json.dumps(output_data, indent=2)
            
            # Display results in Streamlit
            st.subheader("Analysis Results")
            
            # Create two columns: one for the download button and one for the results
            col1, col2 = st.columns([1, 3])
            
            with col1:
                # Allow download of JSON file
                st.download_button(
                    label="Download Results",
                    data=json_output,
                    file_name='vt_domain_analysis.json',
                    mime='application/json'
                )
            
            with col2:
                st.json(output_data)

if __name__ == "__main__":
    main()