"""
Sends today's job report Excel file by email using Gmail SMTP.
Requires two GitHub secrets:
  GMAIL_USER          - the Gmail address that sends the mail
  GMAIL_APP_PASSWORD  - a 16-character Gmail App Password (not your normal password)
"""

import os
import datetime
import smtplib
from email.message import EmailMessage

TO_EMAIL = "srikanthpatel5141@gmail.com"   # recipient

GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")


def main():
    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        raise SystemExit("GMAIL_USER / GMAIL_APP_PASSWORD secrets are not set.")

    today = datetime.date.today().isoformat()
    report_path = f"reports/jobs_{today}.xlsx"

    if not os.path.exists(report_path):
        raise SystemExit(f"Report not found: {report_path}")

    msg = EmailMessage()
    msg["Subject"] = f"Daily Job Openings - {today}"
    msg["From"] = GMAIL_USER
    msg["To"] = TO_EMAIL
    msg.set_content(
        f"Hi Srikanth,\n\n"
        f"Please find attached today's job openings report ({today}).\n\n"
        f"Open the Excel file and use the filters on each column to narrow "
        f"down by company, location, or source. Apply links are clickable.\n\n"
        f"- Automated Job Tracker"
    )

    with open(report_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=os.path.basename(report_path),
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        smtp.send_message(msg)

    print(f"Emailed {report_path} to {TO_EMAIL}")


if __name__ == "__main__":
    main()
