import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(subject, cumulative_percentage):
    # Retrieve SMTP details and email addresses from environment variables
    smtp_server = os.environ.get("SMTP_SERVER")
    smtp_port = int(os.environ.get("SMTP_PORT"))
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    receiver_email = os.environ.get("RECEIVER_EMAIL")

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Create the HTML body
    body = create_html_body(cumulative_percentage)
    msg.attach(MIMEText(body, "html"))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def create_html_body(cumulative_percentage):
    # Create a simple HTML body
    html = f"""\
    <html>
        <body>
            <h2>Your Daily Attendance Report</h2>
            <p>Your cumulative attendance percentage is: <strong>{cumulative_percentage}%</strong></p>
            <p>Keep up the good work!</p>
        </body>
    </html>
    """
    return html
