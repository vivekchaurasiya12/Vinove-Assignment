import time
import socket
import requests
import psutil

# Function to check internet connectivity
def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80), timeout=2)
        return True
    except OSError:
        return False

# Function to detect firewall issues (simple check)
def check_firewall():
    try:
        response = requests.get('https://www.google.com', timeout=2)
        return response.status_code == 200
    except requests.ConnectionError:
        print("Firewall might be blocking the connection.")
        return False

# Function to check battery status
def check_battery_status():
    battery = psutil.sensors_battery()
    if battery is not None:
        return battery.percent, battery.power_plugged
    return None, None

# Main function with graceful shutdown and low battery detection
def main():
    try:
        print("Application is running... (Press Ctrl+C to exit)")
        while True:
            # Check battery status
            battery_percent, is_plugged = check_battery_status()
            if battery_percent is not None:
                if not is_plugged and battery_percent < 20:  # Change the threshold as needed
                    print(f"Low battery detected: {battery_percent}%. Suspending activity tracking to save power.")
                    time.sleep(60)  # Suspend for 60 seconds (adjust as needed)
                    continue  # Skip further processing
            
            # Check internet connection
            if not check_internet_connection():
                print("No internet connection. Application will continue to run.")
                if not check_firewall():
                    print("Potential firewall issue detected.")
            else:
                print("Internet connection is available.")
                
            time.sleep(1)  # Simulating application workload
    except KeyboardInterrupt:
        print("Shutting down gracefully...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Application has been terminated.")

if __name__ == "__main__":
    main()
