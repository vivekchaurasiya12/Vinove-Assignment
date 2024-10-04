from pynput.mouse import Listener as MouseListener
from time import time

# Variables to store mouse movement data
mouse_positions = []
mouse_times = []
irregular_movements = 0

# Threshold for detecting irregular patterns (adjust as needed)
MOVEMENT_THRESHOLD = 100  # pixels
TIME_THRESHOLD = 2  # seconds

def on_move(x, y):
    global mouse_positions, mouse_times, irregular_movements
    current_time = time()

    if mouse_positions:
        prev_x, prev_y = mouse_positions[-1]
        distance = ((x - prev_x) ** 2 + (y - prev_y) ** 2) ** 0.5
        time_diff = current_time - mouse_times[-1]

        # Detect irregular large movements or long periods of inactivity
        if distance > MOVEMENT_THRESHOLD or time_diff > TIME_THRESHOLD:
            irregular_movements += 1
            print(f"Irregular movement detected at position ({x}, {y})")

    # Store current position and time
    mouse_positions.append((x, y))
    mouse_times.append(current_time)

# Start listening to mouse events
def track_mouse_movements():
    with MouseListener(on_move=on_move) as listener:
        listener.join()

track_mouse_movements()
