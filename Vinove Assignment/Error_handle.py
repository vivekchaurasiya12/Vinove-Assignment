import time
import socket
import requests

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

# Main function with graceful shutdown
def main():
    try:
        print("Application is running... (Press Ctrl+C to exit)")
        while True:
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
