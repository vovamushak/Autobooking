import requests

calendly_api_url = "https://api.calendly.com"
event_invitee_link = "https://calendly.com/airai/test-calendar/invitees/f8efc2ff-98d3-46a8-b23b-cee38e752dac"
access_token = "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAxMTA4NzY0LCJqdGkiOiJkM2Y4MDIwMy1mYzVlLTQ5ZDEtOTQ0NC0yZTZiMGYwNTBhZDQiLCJ1c2VyX3V1aWQiOiJkNjUzOWE2Zi0xNTZhLTQzODUtODlkYS1jY2QyNDEyMTIwZDUifQ._JCtIqEm11KbNN3YzctIkruUi7O51PzByKdTA1ZaMztjK6QXeIyliZBjyBOHwyJNv1iCP0WMhaqBP4vieWDB2g"

# Extract event ID from the invitee link
event_id = "airai/test-calendar"

print(event_id)

# Set up headers with your authentication token
headers = {
    "Authorization": f"Bearer {access_token}",  # Replace with your API key or use OAuth token
    "Content-Type": "application/json",
}

# Retrieve event details
event_url = f"{calendly_api_url}/scheduled_events/{event_id}"
response = requests.get(event_url, headers=headers)

event_details = response.json()
print("Event Details:", event_details)