from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
import os

def get_attendance():
    # Retrieve credentials and URLs from environment variables
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")
    url = os.environ.get("URL")
    attendance_url = os.environ.get("ATTENDANCE_URL")

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
        driver.get(url)
        
        # Enter username
        username_field = wait.until(EC.presence_of_element_located((By.ID, "txtun")))
        username_field.send_keys(username)
        
        # Enter password
        password_field = driver.find_element(By.ID, "txtpass")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Wait for the login to process
        wait.until(EC.url_changes(url))

        # Navigate to the attendance page
        driver.get(attendance_url)

        # Wait for the attendance data to load
        attendance_table = wait.until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_rptrcontact_lblCumAtt"))
        )

        # Return attendance details
        return attendance_table.text

    except Exception as e:
        print("An error occurred:", e)
        return None

    finally:
        # Close the browser
        driver.quit()
