from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def book_appointment(calendly_url, selected_datetime):
    # Use the appropriate webdriver for your browser (e.g., ChromeDriver, GeckoDriver for Firefox)
    driver = webdriver.Chrome()

    try:
        # Open the Calendly URL
        driver.get(calendly_url)

        # Wait for the page to load
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="onetrust-accept-btn-handler"]')))

        cookie_button = driver.find_element(By.CSS_SELECTOR, '[id="onetrust-accept-btn-handler"]')
        cookie_button.click()

        # Perform actions to select the desired date and time
        # Example: Click on a date and time element
        date_time_element = driver.find_element(By.CSS_SELECTOR, '[data-start-time="00:30"]')
        date_time_element.click()

        next_time_element = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next 00:30"]')
        next_time_element.click()

        name_element = driver.find_element(By.CSS_SELECTOR, '[name="full_name"]')
        name_element.clear()
        name_element.send_keys("Thomas")

        email_element = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
        email_element.clear()
        email_element.send_keys("t@air.ai")

        submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        print(submit_button)
        submit_button.click()
        # # Wait for the booking confirmation or submit the formname="full_name"
        # # Example: Click on a submit button
        # submit_button = driver.find_element(By.XPATH, 'your-xpath-for-submit-button')
        # submit_button.click()

        # # Wait for the confirmation page to load
        print("Booking successful!")

    except Exception as e:
        print(f"Error: {e}")

    # finally:
    #     # Close the browser
    #     driver.quit()

# Example usage
calendly_url = "https://calendly.com/airai/test-calendar?month=2023-12&date=2023-12-21"
selected_datetime = "2023-12-21 12:00:00"  # Replace with the actual datetime

book_appointment(calendly_url, selected_datetime)