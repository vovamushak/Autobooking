import requests

access_token = "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTEwNTgyLCJqdGkiOiI1ZTA5OGFmYS0wZGNiLTQxNTEtYmU5Ni03ZmU3OTM5YWE2MjgiLCJ1c2VyX3V1aWQiOiIwZWRiZGFlMS03NTk1LTRmOGYtODk3Zi0zMDA2MWZjNjRlYTgifQ.fx_ImaAFuPRfaeIO2cM_vHGc_lSTPh7EKPFF5puAjo573SE3nZRQ_pQ_-tEXSmReZ9YWuvGWgXwc17NHhESFqQ"

def get_eventType ():
    url = "https://api.calendly.com/event_types"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "organization" : "https://api.calendly.com/organizations/74b9dfac-a9aa-4648-b756-24cd33d80bbf"
    }

    response = requests.request("GET", url, headers=headers, params=params)

    print(response.text)
    return response.json()

get_eventType()

# {
#   "collection": [
#     {
#       "active": true,
#       "admin_managed": false,
#       "booking_method": "instant",
#       "color": "#0099ff",
#       "created_at": "2023-01-16T09:13:36.813219Z",
#       "custom_questions": [
#         {
#           "answer_choices": [],
#           "enabled": true,
#           "include_other": false,
#           "name": "Please share anything that will help prepare for our meeting.",
#           "position": 0,
#           "required": false,
#           "type": "text"
#         }
#       ],
#       "deleted_at": null,
#       "description_html": "<p><br></p>",
#       "description_plain": "",
#       "duration": 15,
#       "internal_note": null,
#       "kind": "solo",
#       "name": "Air.ai Resources Call",
#       "pooling_type": null,
#       "profile": {
#         "name": "Thomas Lancer",
#         "owner": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#         "type": "User"
#       },
#       "scheduling_url": "https://calendly.com/airai/success",
#       "secret": false,
#       "slug": "success",
#       "type": "StandardEventType",
#       "updated_at": "2023-11-26T16:29:15.936552Z",
#       "uri": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c"
#     },
#     {
#       "active": true,
#       "admin_managed": false,
#       "booking_method": "instant",
#       "color": "#0099ff",
#       "created_at": "2023-02-19T06:15:08.352726Z",
#       "custom_questions": [
#         {
#           "answer_choices": [],
#           "enabled": true,
#           "include_other": false,
#           "name": "Please share anything that will help prepare for our meeting.",
#           "position": 0,
#           "required": false,
#           "type": "text"
#         }
#       ],
#       "deleted_at": null,
#       "description_html": null,
#       "description_plain": null,
#       "duration": 40,
#       "internal_note": null,
#       "kind": "solo",
#       "name": "Air Interview",
#       "pooling_type": null,
#       "profile": {
#         "name": "Thomas Lancer",
#         "owner": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#         "type": "User"
#       },
#       "scheduling_url": "https://calendly.com/airai/air-interview",
#       "secret": false,
#       "slug": "air-interview",
#       "type": "StandardEventType",
#       "updated_at": "2023-11-26T16:29:15.936552Z",
#       "uri": "https://api.calendly.com/event_types/a97cc2e5-e502-4177-a507-07694883634b"
#     },
#     {
#       "active": true,
#       "admin_managed": false,
#       "booking_method": "instant",
#       "color": "#0099ff",
#       "created_at": "2023-03-08T09:38:05.587655Z",
#       "custom_questions": [
#         {
#           "answer_choices": [],
#           "enabled": false,
#           "include_other": false,
#           "name": "Please share anything that will help prepare for our meeting.",
#           "position": 0,
#           "required": false,
#           "type": "text"
#         },
#         {
#           "answer_choices": [],
#           "enabled": true,
#           "include_other": false,
#           "name": "phone",
#           "position": 1,
#           "required": true,
#           "type": "phone_number"
#         }
#       ],
#       "deleted_at": null,
#       "description_html": "",
#       "description_plain": "",
#       "duration": 30,
#       "internal_note": null,
#       "kind": "solo",
#       "name": "Air Sync",
#       "pooling_type": null,
#       "profile": {
#         "name": "Thomas Lancer",
#         "owner": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#         "type": "User"
#       },
#       "scheduling_url": "https://calendly.com/airai/airdial",
#       "secret": false,
#       "slug": "airdial",
#       "type": "StandardEventType",
#       "updated_at": "2023-11-26T16:29:15.936552Z",
#       "uri": "https://api.calendly.com/event_types/9e990b1c-5950-43b3-a482-a813f9e502fd"
#     },
#     {
#       "active": true,
#       "admin_managed": false,
#       "booking_method": "instant",
#       "color": "#8247f5",
#       "created_at": "2023-11-26T16:29:15.708774Z",
#       "custom_questions": [
#         {
#           "answer_choices": [],
#           "enabled": true,
#           "include_other": false,
#           "name": "Please share anything that will help prepare for our meeting.",
#           "position": 0,
#           "required": false,
#           "type": "text"
#         }
#       ],
#       "deleted_at": null,
#       "description_html": null,
#       "description_plain": null,
#       "duration": 30,
#       "internal_note": null,
#       "kind": "solo",
#       "name": "Test Calendar",
#       "pooling_type": null,
#       "profile": {
#         "name": "Thomas Lancer",
#         "owner": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#         "type": "User"
#       },
#       "scheduling_url": "https://calendly.com/airai/test-calendar",
#       "secret": false,
#       "slug": "test-calendar",
#       "type": "StandardEventType",
#       "updated_at": "2023-11-26T16:29:15.708774Z",
#       "uri": "https://api.calendly.com/event_types/3f1111db-eccb-4b66-b37c-8ded1451f6db"
#     }
#   ],
#   "pagination": {
#     "count": 4,
#     "next_page": null,
#     "next_page_token": null,
#     "previous_page": null,
#     "previous_page_token": null
#   }
# }