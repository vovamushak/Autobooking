from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import datetime
import pytz
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=1)

access_token = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTEwNTgyLCJqdGkiOiI1ZTA5OGFmYS0wZGNiLTQxNTEtYmU5Ni03ZmU3OTM5YWE2MjgiLCJ1c2VyX3V1aWQiOiIwZWRiZGFlMS03NTk1LTRmOGYtODk3Zi0zMDA2MWZjNjRlYTgifQ.fx_ImaAFuPRfaeIO2cM_vHGc_lSTPh7EKPFF5puAjo573SE3nZRQ_pQ_-tEXSmReZ9YWuvGWgXwc17NHhESFqQ'
event_type = 'https://api.calendly.com/event_types/3f1111db-eccb-4b66-b37c-8ded1451f6db'
start_time = '2023-12-21T20:00:00.000000Z'
end_time = '2023-12-25T24:00:00.000000Z'

calendly_timezone = 'UTC'
thomas_timezone = 'CET'

test_userTimezone = 'America/Phoenix'
test_datetime = '2023-12-21T17:30:00Z'

# Custom exception class for "Slot Already Booked" scenario
class SlotAlreadyBookedException(Exception):
    pass

def get_available_times(timezone):
    # Check if data is already in the cache for today
    today = datetime.date.today()
    cache_key = f"{event_type}_{start_time}_{end_time}_{today}"
    
    if cache_key in cache:
        print("Data retrieved from cache.")
        return cache[cache_key]
    
    # If not in the cache, make the API request
    url = "https://api.calendly.com/event_type_available_times"
    querystring = {"event_type": event_type, "start_time": start_time, "end_time": end_time}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers, params=querystring)
    available_days = response.json()

    change_days_byTimezone = []

    for day in available_days['collection']:

        original_dt = datetime.datetime.strptime(day["start_time"], "%Y-%m-%dT%H:%M:%SZ")
        original_timezone = pytz.timezone(calendly_timezone)

        target_timezone = pytz.timezone(timezone)  # Example target timezone
        converted_dt = original_timezone.localize(original_dt).astimezone(target_timezone)

        day["start_time"] = converted_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        change_days_byTimezone.append(day)

    # Update the cache with the current data
    cache[cache_key] = change_days_byTimezone

    return change_days_byTimezone

# for _ in range(10):
#     available_times = get_available_times(event_type, start_time, end_time, access_token)
#     print(available_times)

available_times = get_available_times(thomas_timezone)
# print(available_times)
def book_appointment(tdatetime, timezone):
    today = datetime.date.today()
    cache_key = f"{event_type}_{start_time}_{end_time}_{today}"

    invitee_time = datetime.datetime.strptime(tdatetime, "%Y-%m-%dT%H:%M:%SZ")
    invitee_timezone = pytz.timezone(timezone)

    target_timezone = pytz.timezone(thomas_timezone)  # Example target timezone
    converted_dt = invitee_timezone.localize(invitee_time).astimezone(target_timezone)

    booking_time = converted_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    flg = False
    booking_point = {}
    update_available_times = []
    for day in available_times:
        if day['start_time'] == booking_time:
            flg = True
            booking_point = day
            print(booking_point)
            day["invitees_remaining"] = day["invitees_remaining"] - 1
            if(day["invitees_remaining"] > 0):
                update_available_times.push(day)
            elif(day["invitees_remaining"] == 0):
                available_times.remove(day)
                cache[cache_key] = available_times
        update_available_times.append(day)

    try:
        cal_timezone = pytz.timezone(calendly_timezone)
        time_byCalendly = invitee_timezone.localize(invitee_time).astimezone(cal_timezone).strftime("%Y-%m-%dT%H:%M:%SZ")
        print(time_byCalendly)
        print(booking_time)
        print(booking_point)
        calendly_url = booking_point["scheduling_url"]
        # Use the appropriate webdriver for your browser (e.g., ChromeDriver, GeckoDriver for Firefox)
        driver = webdriver.Chrome()
        try:
            # Open the Calendly URL
            driver.get(calendly_url)

            # Wait for the page to load
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="onetrust-accept-btn-handler"]')))

            cookie_button = driver.find_element(By.CSS_SELECTOR, '[id="onetrust-accept-btn-handler"]')
            cookie_button.click()

            name_element = driver.find_element(By.CSS_SELECTOR, '[name="full_name"]')
            name_element.clear()
            name_element.send_keys("Thomas")

            email_element = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
            email_element.clear()
            email_element.send_keys("t@air.ai")

            submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
            print(submit_button)
            submit_button.click()

            # # Wait for the confirmation page to load
            print("Booking successful!")

        except Exception as e:
            print(f"Error: {e}")

        # finally:
        #     # Close the browser
        #     driver.quit()
    except Exception as e:
        print(f"Error: {e}")
# while True:
#     time.sleep(3/25) # up to 500 per minute 
book_appointment(test_datetime, test_userTimezone)