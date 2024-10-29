import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL

def send_email(subject, cumulative_percentage):
    # Create the email
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    # Create the HTML body
    body = create_html_body(cumulative_percentage)
    msg.attach(MIMEText(body, "html"))

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
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
