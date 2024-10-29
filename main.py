from scraper import get_attendance
from emailer import send_email
import schedule
import time

def daily_attendance_check():
    # Fetch attendance data
    attendance_data = get_attendance()
    
    # Send the data via email
    send_email("Your Daily Attendance Report", attendance_data)

# Schedule the job to run daily at a specific time (e.g., 10 PM)
schedule.every().day.at("02:07").do(daily_attendance_check)

if __name__ == "__main__":
    print("Starting attendance notifier...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
