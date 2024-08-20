import requests

access_token = "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTEwNTgyLCJqdGkiOiI1ZTA5OGFmYS0wZGNiLTQxNTEtYmU5Ni03ZmU3OTM5YWE2MjgiLCJ1c2VyX3V1aWQiOiIwZWRiZGFlMS03NTk1LTRmOGYtODk3Zi0zMDA2MWZjNjRlYTgifQ.fx_ImaAFuPRfaeIO2cM_vHGc_lSTPh7EKPFF5puAjo573SE3nZRQ_pQ_-tEXSmReZ9YWuvGWgXwc17NHhESFqQ"

def get_user():
    url = "https://api.calendly.com/users/me"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

userInfo = get_user()

print(userInfo)

# {'resource': {
#     'avatar_url': 'https://d3v0px0pttie1i.cloudfront.net/uploads/user/avatar/23726469/dec92322.png', 
#     'created_at': '2023-01-16T09:13:00.708604Z', 
#     'current_organization': 'https://api.calendly.com/organizations/74b9dfac-a9aa-4648-b756-24cd33d80bbf', 
#     'email': 't@air.ai', 
#     'name': 'Thomas Lancer', 
#     'resource_type': 'User', 
#     'scheduling_url': 'https://calendly.com/airai', 
#     'slug': 'airai', 
#     'timezone': 'America/Phoenix', 
#     'updated_at': '2023-11-19T04:20:43.640564Z', 
#     'uri': 'https://api.calendly.com/users/0edbdae1-7595-4f8f-897f-30061fc64ea8'
#     }
# }