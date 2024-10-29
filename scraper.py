from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import os  # Importing os to access environment variables

def get_attendance():
    # Retrieve sensitive information from environment variables
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    URL = os.getenv('URL')
    ATTENDANCE_URL = os.getenv('ATTENDANCE_URL')

    # Initialize WebDriver with options
    options = Options()
    options.add_argument('--headless')  # Enable headless mode
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Set up WebDriverWait with a timeout
    wait = WebDriverWait(driver, 10)

    try:
        # Open the login page
        driver.get(URL)
        
        # Enter username
        username_field = wait.until(EC.presence_of_element_located((By.ID, "txtun")))
        username_field.send_keys(USERNAME)
        
        # Enter password
        password_field = driver.find_element(By.ID, "txtpass")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)

        # Wait for the login to process
        wait.until(EC.url_changes(URL))

        # Navigate to the attendance page
        driver.get(ATTENDANCE_URL)

        # Wait for the attendance data to load
        attendance_table = wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_rptrcontact_lblCumAtt"))
        )

        # Check if attendance_table text is retrieved correctly
        attendance_text = attendance_table.text.strip()
        if not attendance_text:
            print("Attendance data is empty.")
            return None
        
        return attendance_text

    except Exception as e:
        print("An error occurred:", e)
        return None

    finally:
        # Close the browser
        driver.quit()
