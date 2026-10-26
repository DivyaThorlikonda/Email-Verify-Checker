
import re
import socket
from concurrent.futures import ThreadPoolExecutor

from flask import Flask, render_template, request, jsonify
import dns.resolver
import dns.exception

app = Flask(__name__)

EMAIL_PATTERN = (
    r"^[A-Za-z0-9._%+-]+@"
    r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)


def check_email(email):
    email = email.strip()

    # 1. Validate email format
    if len(email) > 254 or not re.fullmatch(EMAIL_PATTERN, email):
        return {
            "email": email,
            "status": "Likely Bounce",
            "reason": "Invalid email format"
        }

    domain = email.rsplit("@", 1)[1].lower()

    # 2. Check whether the domain has mail records
    try:
        answers = dns.resolver.resolve(
            domain, "MX", lifetime=4
        )
        mx_records = sorted(
            answers, key=lambda record: record.preference
        )
        mx_host = str(mx_records[0].exchange).rstrip(".")

    except dns.resolver.NXDOMAIN:
        return {
            "email": email,
            "status": "Likely Bounce",
            "reason": "Domain does not exist"
        }

    except dns.resolver.NoAnswer:
        return {
            "email": email,
            "status": "Unknown",
            "reason": "No MX records found; mailbox not confirmed"
        }

    except (dns.exception.DNSException, OSError):
        return {
            "email": email,
            "status": "Unknown",
            "reason": "DNS lookup failed or timed out"
        }

    # 3. Try to connect to the mail server.
    # This does not send an email or verify a mailbox.
    try:
        with socket.create_connection((mx_host, 25), timeout=3):
            reason = "Mail server reachable; mailbox not confirmed"

    except (OSError, socket.timeout):
        reason = "Connection blocked or server unreachable"

    return {
        "email": email,
        "status": "Unknown",
        "reason": reason
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json(silent=True) or {}
    raw_emails = data.get("emails", "")

    if not isinstance(raw_emails, str):
        return jsonify({
            "error": "Enter email addresses as text."
        }), 400

    emails = list(dict.fromkeys(
        item.strip()
        for item in re.split(r"[\s,;]+", raw_emails)
        if item.strip()
    ))

    if not emails:
        return jsonify({
            "error": "Please enter email addresses."
        }), 400

    if len(emails) > 50:
        return jsonify({
            "error": "Maximum 50 addresses per check."
        }), 400

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(check_email, emails))

    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True)
