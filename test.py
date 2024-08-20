import requests
import datetime
import pytz
import time

# Install the required libraries
# Run these commands in your terminal or command prompt:
# pip install requests
# pip install pytz

# User's authentication token for Calendly API
access_token = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTEwNTgyLCJqdGkiOiI1ZTA5OGFmYS0wZGNiLTQxNTEtYmU5Ni03ZmU3OTM5YWE2MjgiLCJ1c2VyX3V1aWQiOiIwZWRiZGFlMS03NTk1LTRmOGYtODk3Zi0zMDA2MWZjNjRlYTgifQ.fx_ImaAFuPRfaeIO2cM_vHGc_lSTPh7EKPFF5puAjo573SE3nZRQ_pQ_-tEXSmReZ9YWuvGWgXwc17NHhESFqQ'

# Calendly scheduling link
scheduling_link = 'https://calendly.com/airai/test-calendar?month=2023-12'

# Global variable to track the last API request time
last_api_request_time = 0

# Custom exception class for "Slot Already Booked" scenario
class SlotAlreadyBookedException(Exception):
    pass

# Function to fetch available times from Calendly scheduling link
def get_availabilities(timezone):
    try:
        # Calculate the next 4 days
        today = datetime.datetime.now()
        end_date = today + datetime.timedelta(days=4)

        # Create a list to store available times
        available_times = []

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        # Loop through the next 4 days
        while today < end_date:
            # Create the URL with the specific date and timezone
            url = f"{scheduling_link}&day={today.strftime('%Y-%m-%d')}&timezone={timezone}"

            # Make the API call to fetch available times for the current day
            response = make_api_request(url, "GET", headers=headers)
            # Extract available times from the response
            available_times_day = response.json().get('available_times', [])
            
            # Adjust the available times to the given timezone
            for time_str in available_times_day:
                time = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S')
                time = pytz.timezone(timezone).localize(time)
                available_times.append(time)

            # Move to the next day
            today += datetime.timedelta(days=1)

        return available_times
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch available times: {str(e)}")
        return []

# Function to book an appointment at a specific time with timezone
def book_appointment(datetime, timezone):
    try:
        # Create the URL with the specific timezone
        url = f"{scheduling_link}&timezone={timezone}"

        # Format the datetime as required by the API
        time_to_book = datetime.strftime('%Y-%m-%dT%H:%M:%S')

        # Make the API call to book the appointment
        response = make_api_request(url, method='POST', json={
            'time': time_to_book,
            'timezone': timezone
        })

        # Check if the appointment was successfully booked
        if response.status_code == 200:
            print("Appointment booked successfully!")
        elif response.status_code == 409:
            raise SlotAlreadyBookedException("Appointment is already booked.")
        else:
            print("Failed to book appointment.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to book appointment: {str(e)}")

# Function to make an API request with rate limiting
def make_api_request(url, method='GET', **kwargs):
    global last_api_request_time

    # Calculate the time elapsed since the last API request
    elapsed_time = time.time() - last_api_request_time

    # If less than 1 second has passed, wait before making the next request
    if elapsed_time < 1:
        time.sleep(1 - elapsed_time)

    # Make the API request and update the last API request time
    response = requests.request(method, url, **kwargs)
    last_api_request_time = time.time()

    return response

# Example usage:

# Choose a specific timezone
timezone = 'America/New_York'  # Example timezone

# Fetch available times from the scheduling link for the next 4 days
available_times = get_availabilities(timezone)
print(f"Available times: {available_times}")

# Choose a specific time to book
time_to_book = datetime.datetime(2023, 11, 15, 10, 0)  # Example: November 15, 2023 at 10:00 AM

# Book the appointment
try:
    book_appointment(time_to_book, timezone)
except SlotAlreadyBookedException:
    print("The slot is already booked.")