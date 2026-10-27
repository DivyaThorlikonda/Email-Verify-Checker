# Email Verifier – Email Address Checking Tool

## Project Description

Email Verifier is a simple web application developed using Python and Flask. It allows users to enter multiple email addresses and checks whether each address is likely to bounce or has an unknown delivery status.

The application validates email formats and checks domain mail records using DNS lookups.

## Features

- Check multiple email addresses at once.
- Validate email address formats.
- Check domain MX records using DNS.
- Display individual results for each email address.
- Classify addresses as Likely Delivered, Likely Bounce, or Unknown where supported by the available checks.
- Simple and user-friendly web interface.
- No emails are sent to the entered addresses.

## Technologies Used

- Python 3.11
- Flask
- dnspython
- HTML
- CSS
- Git and GitHub
- Gunicorn
- Render (deployment)

## How It Works

1. The user enters email addresses, one per line.
2. The application checks the format of each address.
3. It looks up DNS mail records for the domain.
4. It displays a result and explanation for each address.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd email-verifier
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open the following address in your browser:

`http://127.0.0.1:5000`

## Limitations

- A valid email format does not prove that the mailbox exists.
- DNS MX records indicate that a domain has mail servers, but they cannot confirm that a particular mailbox will accept messages.
- Some hosting providers may restrict DNS or outbound mail-server connections.
- Timeouts and inconclusive checks should be reported as Unknown rather than as a definite bounce.
- The application does not send verification emails and cannot guarantee successful delivery.

## Project Links

**Live Application:** https://email-verify-checker.onrender.com

**GitHub Repository:** https://github.com/DivyaThorlikonda/Email-Verify-Checker

## Author
Thorlikonda Divya.
Developed as a Software Development project.
