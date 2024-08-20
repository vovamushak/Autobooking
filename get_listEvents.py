import requests

access_token = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTEwNTgyLCJqdGkiOiI1ZTA5OGFmYS0wZGNiLTQxNTEtYmU5Ni03ZmU3OTM5YWE2MjgiLCJ1c2VyX3V1aWQiOiIwZWRiZGFlMS03NTk1LTRmOGYtODk3Zi0zMDA2MWZjNjRlYTgifQ.fx_ImaAFuPRfaeIO2cM_vHGc_lSTPh7EKPFF5puAjo573SE3nZRQ_pQ_-tEXSmReZ9YWuvGWgXwc17NHhESFqQ'
organization: "https://api.calendly.com/organizations/74b9dfac-a9aa-4648-b756-24cd33d80bbf"

def get_schedule_listEvents ():
    url = "https://api.calendly.com/scheduled_events"

    querystring = {"organization":"https://api.calendly.com/organizations/74b9dfac-a9aa-4648-b756-24cd33d80bbf", "count":"100"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# {
#   "collection": [
#     {
#       "calendar_event": {
#         "external_id": "683rqjgmq16k9ud5tpddkcevf8",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T10:16:19.666897Z",
#       "end_time": "2023-01-16T18:15:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-16T18:00:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T10:16:20.535283Z",
#       "uri": "https://api.calendly.com/scheduled_events/d7ea49e3-ee55-4d28-9a23-97b64b89cbe7"
#     },
#     {
#       "calendar_event": {
#         "external_id": "8qdrrb38bafr32s0tqe4qqhkto",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T12:55:26.511620Z",
#       "end_time": "2023-01-17T17:15:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-17T17:00:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T12:55:27.186664Z",
#       "uri": "https://api.calendly.com/scheduled_events/ecb531ee-29f0-490b-86fc-5fbde9ab9810"
#     },
#     {
#       "calendar_event": {
#         "external_id": "i1cekeskp4s4fqee6skeastols",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T14:48:12.682389Z",
#       "end_time": "2023-01-17T21:45:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-17T21:30:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T14:48:13.459104Z",
#       "uri": "https://api.calendly.com/scheduled_events/5d3fd139-766a-4044-9019-fd0765da6ae1"
#     },
#     {
#       "calendar_event": {
#         "external_id": "mgfpshhep4e449hduludhdfod4",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T17:11:36.190224Z",
#       "end_time": "2023-01-17T16:15:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-17T16:00:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T17:11:37.079879Z",
#       "uri": "https://api.calendly.com/scheduled_events/45bb1af9-167b-48fe-810a-5f24cd66d835"
#     },
#     {
#       "calendar_event": {
#         "external_id": "qa1365c628a0mjovm5cau4ecp8",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T18:02:25.755273Z",
#       "end_time": "2023-01-17T18:45:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-17T18:30:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T18:02:26.586991Z",
#       "uri": "https://api.calendly.com/scheduled_events/6895528a-5087-4858-a9bf-72bd3eac7833"
#     },
#     {
#       "calendar_event": {
#         "external_id": "ln98ck7rjhalpoq7qhbditrqv8",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T19:36:54.408163Z",
#       "end_time": "2023-01-17T00:15:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-17T00:00:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T19:36:55.262085Z",
#       "uri": "https://api.calendly.com/scheduled_events/8d2e16da-c082-4fe9-81a5-a6eda70e0709"
#     },
#     {
#       "calendar_event": {
#         "external_id": "f949m3m6pv20lbbv6lq56hmo6g",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T20:30:19.367699Z",
#       "end_time": "2023-01-17T17:45:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-17T17:30:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T20:30:21.998204Z",
#       "uri": "https://api.calendly.com/scheduled_events/6d0b8477-c029-4336-8c98-67c044205ed5"
#     },
#     {
#       "calendar_event": {
#         "external_id": "oopl8uv47c55b04446u1ol3eug",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T22:02:40.758510Z",
#       "end_time": "2023-01-17T19:45:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-17T19:30:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T22:02:41.359910Z",
#       "uri": "https://api.calendly.com/scheduled_events/53496570-f5b8-49ea-8f25-7535ef83b4d2"
#     },
#     {
#       "calendar_event": {
#         "external_id": "kalk62p296481u9hqia7se78ik",
#         "kind": "google"
#       },
#       "created_at": "2023-01-16T23:56:36.363614Z",
#       "end_time": "2023-01-18T01:45:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-18T01:30:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-16T23:56:37.016337Z",
#       "uri": "https://api.calendly.com/scheduled_events/105dd706-4e02-4920-b344-4557e6cd5d19"
#     },
#     {
#       "calendar_event": {
#         "external_id": "3jfs4sf7i0ejnna32kict71n2s",
#         "kind": "google"
#       },
#       "created_at": "2023-01-17T03:51:11.929386Z",
#       "end_time": "2023-01-19T01:45:00.000000Z",
#       "event_guests": [],
#       "event_memberships": [
#         {
#           "user": "https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8",
#           "user_email": "t@air.ai"
#         }
#       ],
#       "event_type": "https://api.calendly.com/event_types/44d29aa8-8e46-4008-9e2f-c24c160c050c",
#       "invitees_counter": {
#         "active": 1,
#         "limit": 1,
#         "total": 1
#       },
#       "location": {
#         "location": null,
#         "type": "custom"
#       },
#       "name": "Air.ai Resources Call",
#       "start_time": "2023-01-19T01:30:00.000000Z",
#       "status": "active",
#       "updated_at": "2023-01-17T03:51:12.591656Z",
#       "uri": "https://api.calendly.com/scheduled_events/818c8c47-5b72-4493-b4c8-2198e016f081"
#     }
#   ],
#   "pagination": {
#     "count": 10,
#     "next_page": "https://api.calendly.com/scheduled_events?count=10&organization=https%3A%2F%2Fapi.calendly.com%2Forganizations%2F74b9dfac-a9aa-4648-b756-24cd33d80bbf&page_token=BaxRKuyHraa-YPh6WKBvXwC-cTJfzwHd&status=active",
#     "next_page_token": "BaxRKuyHraa-YPh6WKBvXwC-cTJfzwHd",
#     "previous_page": null,
#     "previous_page_token": null
#   }
# }