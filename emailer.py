import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os  # Importing os to access environment variables

def send_email(subject, cumulative_percentage):
    # Check if cumulative_percentage is None
    if cumulative_percentage is None:
        cumulative_percentage = "No data available"  # Handle the case of no data

    # Retrieve sensitive information from environment variables
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = int(os.getenv('SMTP_PORT'))
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
    RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

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
