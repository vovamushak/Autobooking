import requests

access_token = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTEwNTgyLCJqdGkiOiI1ZTA5OGFmYS0wZGNiLTQxNTEtYmU5Ni03ZmU3OTM5YWE2MjgiLCJ1c2VyX3V1aWQiOiIwZWRiZGFlMS03NTk1LTRmOGYtODk3Zi0zMDA2MWZjNjRlYTgifQ.fx_ImaAFuPRfaeIO2cM_vHGc_lSTPh7EKPFF5puAjo573SE3nZRQ_pQ_-tEXSmReZ9YWuvGWgXwc17NHhESFqQ'
event_type = 'https://api.calendly.com/event_types/3f1111db-eccb-4b66-b37c-8ded1451f6db'
start_time = '2023-12-21T20:00:00.000000Z'
end_time = '2023-12-25T24:00:00.000000Z'

def get_availableTimes() :
    url = "https://api.calendly.com/event_type_available_times"

    querystring = f{"event_type":{event_type},"start_time":{start_time},"end_time":{end_time}}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    return response.json()

get_availableTimes()

# {
#   "collection": [
#     {
#       "status": "available",
#       "start_time": "2023-12-21T20:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T20:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-21T20:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T20:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-21T21:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T21:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-21T21:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T21:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-21T22:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T22:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-21T22:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T22:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-21T23:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T23:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-21T23:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-21T23:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T00:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T00:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T00:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T00:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T01:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T01:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T01:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T01:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T16:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T16:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T17:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T17:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T17:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T17:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T18:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T18:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T19:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T19:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T20:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T20:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T20:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T20:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T21:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T21:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T21:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T21:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T22:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T22:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T22:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T22:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T23:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T23:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-22T23:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-22T23:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T00:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T00:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T00:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T00:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T01:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T01:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T01:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T01:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T16:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T16:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T17:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T17:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T17:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T17:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T18:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T18:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T18:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T18:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T19:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T19:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T20:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T20:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T20:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T20:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T21:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T21:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T21:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T21:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T22:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T22:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T22:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T22:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T23:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T23:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-23T23:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-23T23:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-24T00:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-24T00:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-24T00:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-24T00:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-24T01:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-24T01:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-24T01:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-24T01:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T16:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T16:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T17:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T17:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T18:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T18:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T19:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T19:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T20:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T20:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T20:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T20:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T21:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T21:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T21:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T21:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T22:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T22:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T22:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T22:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T23:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T23:00:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-25T23:30:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-25T23:30:00Z"
#     },
#     {
#       "status": "available",
#       "start_time": "2023-12-26T00:00:00Z",
#       "invitees_remaining": 1,
#       "scheduling_url": "https://calendly.com/airai/test-calendar/2023-12-26T00:00:00Z"
#     }
#   ]
# }