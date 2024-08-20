import datetime
import pytz

def get_timezone():
    # Get the current datetime in UTC
    utc_now = datetime.datetime.now(pytz.utc)

    # Convert the UTC datetime to a specific timezone
    timezone = pytz.timezone("America/New_York")
    ny_time = utc_now.astimezone(timezone)

    # Get a list of all available timezones
    all_timezones = pytz.all_timezones

    return str(ny_time), all_timezones

ny_time, all_timezones = get_timezone()
print("New York Time:", ny_time)
print("All Timezones:", all_timezones)