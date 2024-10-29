import os
from scraper import get_attendance
from emailer import send_email

def daily_attendance_check():
    # Fetch attendance data
    attendance_data = get_attendance()
    
    # Send the data via email
    send_email("Your Daily Attendance Report", attendance_data)

if __name__ == "__main__":
    print("Starting attendance notifier...")

    # Execute the daily attendance check immediately (if running locally)
    daily_attendance_check()