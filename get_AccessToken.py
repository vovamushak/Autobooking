import base64
import requests

eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTA4NzY0LCJqdGkiOiJkM2Y4MDIwMy1mYzVlLTQ5ZDEtOTQ0NC0yZTZiMGYwNTBhZDQiLCJ1c2VyX3V1aWQiOiJkNjUzOWE2Zi0xNTZhLTQzODUtODlkYS1jY2QyNDEyMTIwZDUifQ._JCtIqEm11KbNN3YzctIkruUi7O51PzByKdTA1ZaMztjK6QXeIyliZBjyBOHwyJNv1iCP0WMhaqBP4vieWDB2g

# Set the username and password
# Client ID = xtIrznxVvyvS7eDKmggLYbkzxFuh2xXu2ubH0SpyCRI // Your app's unique identifier that's used to initiate OAuth.
# Client secret = wA04T9eqyDFyV4Qmdh7DJBsOisbWcypuqlRgbgEyE5c // A secret that's shared between your app and Calendly's authorization server that's used to establish and refresh OAuth authentication.
# Webhook signing key = VLaUUhGPvygWruc4FKbTqkQWrXAZsYk410x_ySV8tno // A unique key shared between your app and Calendly that's used to verify events sent to your endpoints.

client_id = "xtIrznxVvyvS7eDKmggLYbkzxFuh2xXu2ubH0SpyCRI"
client_secret = "wA04T9eqyDFyV4Qmdh7DJBsOisbWcypuqlRgbgEyE5c"

def get_AuthToken():
    # Encode the username and password in base64
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    # Construct the Authorization header
    authorization_header = f"Basic {encoded_credentials}"

    # Use the authorization_header in your HTTP request headers
    headers = {
        "Authorization": authorization_header,
        "Content-Type": "application/json",
    }

    # Send your HTTP request with the headers

    url = "https://auth.calendly.com/oauth/token"

    payload = ""

    response = requests.request("POST", url, data=payload, headers=headers, params={"grant_type": "client_credentials"})

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data

get_AuthToken()


# print(response.json()["access_token"])