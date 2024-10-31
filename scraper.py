from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
import os  # Importing os to access environment variables

def get_attendance():
    """
    Retrieves the attendance percentage from the specified attendance page.

    The function uses Selenium WebDriver to automate the login process
    and navigate to the attendance page. It fetches the cumulative 
    attendance percentage and handles cases where data might be missing.

    Returns:
        str or None: The cumulative attendance percentage as a string if available, 
                     otherwise None if no data is retrieved.
    """
    
    # Retrieve sensitive information from environment variables
    USERNAME = os.getenv('USERNAME')          # Student's username
    PASSWORD = os.getenv('PASSWORD')          # Student's password
    URL = os.getenv('URL')                    # Login page URL
    ATTENDANCE_URL = os.getenv('ATTENDANCE_URL')  # Attendance page URL

    # Initialize WebDriver with options for headless operation
    options = Options()
    options.add_argument('--headless')  # Run Chrome in headless mode
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    options.add_argument('--no-sandbox')  # Bypass OS security model
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Set up WebDriverWait with a timeout for dynamic content loading
    wait = WebDriverWait(driver, 10)

    try:
        # Open the login page
        driver.get(URL)

        # Wait for the username field to load and enter the username
        username_field = wait.until(EC.presence_of_element_located((By.ID, "txtun")))
        username_field.send_keys(USERNAME)

        # Locate the password field, enter the password, and submit the form
        password_field = driver.find_element(By.ID, "txtpass")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)  # Simulate hitting the Enter key

        # Wait for the URL to change indicating a successful login
        wait.until(EC.url_changes(URL))

        # Navigate to the attendance page after login
        driver.get(ATTENDANCE_URL)

        # Wait for the attendance data to load on the attendance page
        attendance_table = wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_rptrcontact_lblCumAtt"))
        )

        # Extract the text from the attendance table
        attendance_text = attendance_table.text.strip()
        
        # Check if the attendance data is empty and return None if so
        if not attendance_text:
            print("Attendance data is empty.")
            return None
        
        return attendance_text  # Return the attendance percentage

    except Exception as e:
        # Print an error message if an exception occurs
        print("An error occurred:", e)
        return None  # Return None in case of an error

    finally:
        # Ensure the browser is closed after the operations
        driver.quit()