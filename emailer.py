import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os  # Importing os to access environment variables

def send_email(subject, cumulative_percentage):
    # Check if cumulative_percentage is None
    if cumulative_percentage is None:
        cumulative_percentage = "No data available"  # Handle the case of no data

    # Retrieve sensitive information from environment variables
    SMTP_SERVER = os.getenv('SMTP_SERVER')  # SMTP server address
    SMTP_PORT = int(os.getenv('SMTP_PORT'))  # SMTP server port
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')  # Sender's email address
    SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')  # Sender's email password
    RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')  # Receiver's email address

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL  # Set sender's email
    msg["To"] = RECEIVER_EMAIL  # Set receiver's email
    msg["Subject"] = subject  # Set email subject

    # Create the HTML body for the email
    body = create_html_body(cumulative_percentage)
    msg.attach(MIMEText(body, "html"))  # Attach the HTML body to the email

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:  # Connect to the SMTP server
            server.starttls()  # Upgrade the connection to secure
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email
        print("Email sent successfully!")  # Confirmation message
    except Exception as e:
        print(f"Failed to send email: {e}")  # Print error message if sending fails

def create_html_body(cumulative_percentage):
    # Create a simple HTML body for the email
    html = f"""\
    <html>
        <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
            <div style="max-width: 600px; margin: 20px auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <h2 style="color: #4CAF50; text-align: center;">Daily Attendance Report</h2>
                <p style="font-size: 16px; color: #555555; line-height: 1.5; text-align: center;">
                    Hello! Here is your attendance summary for today.
                </p>
                <div style="text-align: center; margin-top: 20px;">
                    <p style="font-size: 24px; color: #333333; font-weight: bold;">Cumulative Attendance:</p>
                    <p style="font-size: 42px; color: #4CAF50; font-weight: bold; margin: 10px;">{cumulative_percentage}%</p>
                </div>
                <hr style="border: none; border-top: 1px solid #e0e0e0; margin: 20px 0;">
                <p style="font-size: 14px; color: #888888; text-align: center;">
                    Stay consistent and maintain your attendance to achieve your goals!
                </p>
            </div>
            <footer style="text-align: center; font-size: 12px; color: #aaaaaa; margin-top: 20px;">
                <p>If you have any questions, please contact your support team.</p>
            </footer>
        </body>
    </html>
    """
    return html  # Return the generated HTML body