import requests
import datetime
import pytz
from cachetools import cached, TTLCache

access_token = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTEwNTgyLCJqdGkiOiI1ZTA5OGFmYS0wZGNiLTQxNTEtYmU5Ni03ZmU3OTM5YWE2MjgiLCJ1c2VyX3V1aWQiOiIwZWRiZGFlMS03NTk1LTRmOGYtODk3Zi0zMDA2MWZjNjRlYTgifQ.fx_ImaAFuPRfaeIO2cM_vHGc_lSTPh7EKPFF5puAjo573SE3nZRQ_pQ_-tEXSmReZ9YWuvGWgXwc17NHhESFqQ'

test_event_uuid = '3f1111db-eccb-4b66-b37c-8ded1451f6db' #  a3af19d1-f011-41fd-b8ac-c0566579f864
test_invitees_uuid = 'a3af19d1-f011-41fd-b8ac-c0566579f864'
test_today = '2023-12-20'
test_endtime = '2023-12-24'
test_datetime = '2023-12-23T22:30:00Z',

app_timezone = 'UTC'  # Example timezone
calendly_timezone = 'UTC'
user_timezone = 'US/Central'

def change_timezone(arr, timezone):
    change_days_byTimezone = []
    for day in arr:
        original_dt = datetime.datetime.strptime(day["start_time"], "%Y-%m-%dT%H:%M:%SZ")
        original_timezone = pytz.timezone(calendly_timezone)  # Example original timezone
        # Define the target timezone
        target_timezone = pytz.timezone(timezone)  # Example target timezone
        # Convert the localized datetime to the target timezone
        converted_dt = original_timezone.localize(original_dt).astimezone(target_timezone)

        day["start_time"] = converted_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        change_days_byTimezone.append(day)
    
    return change_days_byTimezone


@cached(cache=TTLCache(maxsize=100, ttl=300))  # Cache with maxsize of 100 and 300 seconds (5 minutes) time-to-live
def get_availabilities(event_type, timezone):
    url = "https://api.calendly.com/event_type_available_times"

    today = datetime.date.today()
    after_4_days = datetime.date.today() + datetime.timedelta(days=4)

    querystring = {
        "event_type": f"https://api.calendly.com/event_types/{event_type}",
        "start_time": test_today,
        "end_time": test_endtime,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    original_dt = response.json()['collection']
    result = change_timezone(original_dt, timezone)
    return result

cache_available_days = get_availabilities(test_event_uuid, app_timezone)
print(cache_available_days)

def book_appointment(datetime, timezone):
    booking_time = datetime.datetime.strptime(datetime, "%Y-%m-%dT%H:%M:%SZ")
    flg = False
    for day in cache_available_days:
        if day['start_time'] == booking_time:
            flg = True
            url = f"https://api.calendly.com/scheduled_events/{test_invitees_uuid}/cancellation"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}"
            }

            response = requests.request("GET", url, headers=headers, json={"reason": "Already is scheduled."})
            print(response.status_code)
            cache_available_days.remove(day)
            return None
    # if flg == False:
    #     raise SlotAlreadyBookedException("Slot is already booked!")

# try:
    book_appointment(test_datetime, user_timezone)
# except SlotAlreadyBookedException as e:
#     print(str(e))