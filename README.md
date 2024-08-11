# InboxInspector

InboxInspector is a simple Streamlit application that allows users to upload a CSV file of email addresses and query VirusTotal for domain reports on each domain represented in the email addresses.

---

> [!CAUTION]
> You can try a [live demo](https://inboxinspector.streamlit.app/) of this application on Streamlit's cloud at the following link, however, I do not claim any responsibility for the safety or security of your API key or accuracy of results should you use the demo hosted on Streamlit's cloud, nor self-hosted variants of this example application. 

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Using Poetry (Recommended)](#using-poetry-recommended)
  - [Manual Installation](#manual-installation)
- [Usage](#usage)
- [Getting a VirusTotal API Key](#getting-a-virustotal-api-key)
- [Input File Format](#input-file-format)
- [Output](#output)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.12 or higher
- pip (Python package installer)

## About Poetry and pipx

### Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

Benefits of using Poetry:
- Dependency resolution and management
- Isolation of project environments
- Streamlined packaging and publishing

### pipx

pipx is a tool to help you install and run end-user applications written in Python. It's designed to install applications to isolated environments, but make them available in your shell as if they were installed globally.

Benefits of using pipx:
- Installs apps in isolated environments
- Makes installed apps available globally
- Allows for easy upgrades and uninstallations

## Installation

### Using Poetry (Recommended)

1. Install pipx if you haven't already. Follow the installation instructions in the [pipx documentation](https://github.com/pypa/pipx#install-pipx).

2. Once pipx is installed, use it to install Poetry:
   ```
   pipx install poetry
   ```

3. Clone the repository:
   ```
   git clone https://github.com/rainmana/InboxInspector.git
   cd inboxinspector
   ```

4. Install dependencies using Poetry:
   ```
   poetry install
   ```

5. Activate the virtual environment:
   ```
   poetry shell
   ```

### Manual Installation

If you prefer not to use Poetry, you can set up the project manually:

1. Clone the repository:
   ```
   git clone https://github.com/rainmana/inboxinspector.git
   cd inboxinspector
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

   Note: You may need to create a `requirements.txt` file by running `poetry export -f requirements.txt --output requirements.txt` if it doesn't exist.

## Usage

1. Ensure you're in the project directory and your virtual environment is activated.

2. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

   Note: If you encounter issues or if Poetry is not in your PATH, you can use the following command as a safe alternative:
   ```
   python -m poetry run streamlit run main.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

4. Enter your VirusTotal API key in the provided field.

5. Upload a CSV file containing email addresses.

6. Click the "Analyze" button to start the process.

7. Once complete, you can view the results in the browser and download them as a JSON file.

## Getting a VirusTotal API Key

1. Go to [VirusTotal](https://www.virustotal.com/) and sign up for an account if you don't have one.
2. After logging in, go to your [API key page](https://www.virustotal.com/gui/my-apikey).
3. Copy your API key and use it in the InboxInspector application.

Note: The free tier of VirusTotal API has rate limits. Enable the "Rate limiting" checkbox in the app if you're using a free API key.

## Input File Format

The input CSV file should have a single column with the header "email". Each row should contain one email address. For example:

```
email
user1@example.com
user2@example.org
user3@example.net
```

## Output

The application provides a JSON output with the following structure:

- Metadata: Contains information about the analysis run, including the date, input file name, number of records processed, and successful lookups.
- Results: An array of objects, each containing:
  - Email address
  - Domain
  - VirusTotal analysis results, including reputation, registrar information, creation date, last update date, analysis stats, and more.

You can download this JSON file for further analysis or record-keeping.

## Troubleshooting

- If you're having trouble running the app with `streamlit run main.py`, try using:
  ```
  python -m poetry run streamlit run main.py
  ```
  This is especially useful if Poetry is not in your PATH or if you haven't refreshed your terminal after installing Poetry.

- If you encounter any issues with dependencies, try updating your Poetry lock file:
  ```
  poetry update
  ```

- Ensure your VirusTotal API key is correct and has the necessary permissions.

- If you're using the free tier of VirusTotal API, make sure the rate limiting option is enabled to avoid exceeding usage limits.

- If you're still experiencing issues, try closing and reopening your terminal or command prompt to ensure all environment changes are applied.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimers 
**All opinions are my own and do not represent those of my employer.**

**Any tools listed or linked here are for ethical, legal, authorized, and educational purposes only.**

**You are responsible for the securtity of your API keys, information, data, and applications, etc.**
