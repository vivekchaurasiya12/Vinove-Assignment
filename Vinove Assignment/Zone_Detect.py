import time
import requests
import pytz
from datetime import datetime

# Function to get the current timezone based on geographical location
def get_current_timezone():
    try:
        # Get the user's location using a geolocation API
        response = requests.get('http://ipinfo.io/json')
        data = response.json()

        # Extract timezone from the API response
        timezone_str = data.get('timezone', 'UTC')  # Default to UTC if not found
        timezone = pytz.timezone(timezone_str)  # Get timezone object
        return timezone
    except Exception as e:
        print(f"Error getting timezone: {e}. Defaulting to UTC.")
        return pytz.utc  # Fallback to UTC if an error occurs

# Main function to monitor timezone changes
def main():
    previous_timezone = get_current_timezone()  # Initial timezone
    print(f"Initial timezone: {previous_timezone.zone}")

    while True:
        current_timezone = get_current_timezone()

        # Detect timezone changes
        if current_timezone != previous_timezone:
            print(f"Timezone changed from {previous_timezone.zone} to {current_timezone.zone}")
            previous_timezone = current_timezone  # Update to new timezone

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
