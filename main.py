from scraper import get_attendance  # Import the function to fetch attendance data
from emailer import send_email  # Import the function to send email notifications

def daily_attendance_check():
    """
    Function to check daily attendance.
    It fetches the attendance data and sends it via email.
    """
    # Fetch attendance data
    attendance_data = get_attendance()
    
    # Send the data via email with a subject line
    send_email("Daily Attendance Report", attendance_data)

if __name__ == "__main__":
    print("Starting attendance notifier...")  # Indicate that the notifier is starting

    # Execute the daily attendance check immediately (if running locally)
    daily_attendance_check()