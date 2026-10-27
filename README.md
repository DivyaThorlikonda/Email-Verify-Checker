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

## How the Application Works

The Email Verifier processes email addresses through the following steps:

1. **User Input:** The user pastes multiple email addresses into the input field, usually one address per line.
2. **Email Format Validation:** The application checks whether each address follows a basic email format using Python regular expressions.
3. **Domain Extraction:** If the format is valid, the application extracts the domain name from the email address.
4. **DNS Lookup:** The application uses the `dnspython` library to check the domain's DNS mail records (MX records).
5. **Result Classification:** Based on the available checks, the application assigns a delivery status and provides an explanation.
6. **Display Results:** The application displays the status of each address separately on the web page.

## Understanding the Results

- **Likely Delivered:** The address has passed the available checks, and the domain appears to support email delivery. This does not guarantee that the specific mailbox exists or will accept a message.
- **Likely Bounce:** The address is invalid in format, or the checks indicate that delivery is unlikely, depending on the application's implemented rules.
- **Unknown:** The available checks cannot determine whether the address is deliverable. This can happen because of DNS errors, timeouts, restricted network access, or inconclusive server responses.

## Example Usage

**Example input:**

    student@example.com
    invalid-email
    user@nonexistent-domain.invalid

**Example results (illustrative):**

<img width="1061" height="861" alt="image" src="https://github.com/user-attachments/assets/78747d4b-99db-4151-b5dc-866ef6c66844" />


The actual results depend on DNS responses and the application's classification rules.

## Deployment

The application is deployed on Render and can be accessed using the live application link provided below. DNS lookups and delivery checks may be affected by the hosting provider's network restrictions.

The application does not send emails or attempt to access users' mailboxes. It only performs the checks implemented in the application.


## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/DivyaThorlikonda/Email-Verify-Checker.git
cd Email-Verify-Checker
```
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
