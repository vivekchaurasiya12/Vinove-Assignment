import time
from pynput.mouse import Listener as MouseListener
from PIL import ImageGrab

# Function to capture screenshot
def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshot_{int(time.time())}.png")
    print("Screenshot taken!")

# Function to listen to mouse events (you can customize this as per your need)
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

def on_scroll(x, y, dx, dy):
    print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# Start mouse listener
def start_mouse_listener():
    with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

# Main function to capture screenshots every 30 seconds
def main():
    interval_seconds = 30  # Set interval to 30 seconds
    print("Taking screenshots every 30 seconds...")

    while True:
        take_screenshot()
        time.sleep(interval_seconds)

if __name__ == "__main__":
    main()
