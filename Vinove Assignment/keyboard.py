from pynput import keyboard

# Track if Alt key is pressed
is_alt_pressed = False

def on_press(key):
    global is_alt_pressed
    try:
        # Print all key presses for debugging
        print(f"Key pressed: {key}")
        
        # Detect if Alt is pressed
        if key == keyboard.Key.alt:
            is_alt_pressed = True

        # Detect if Tab is pressed while Alt is held down (Alt + Tab switch)
        if key == keyboard.Key.tab and is_alt_pressed:
            print("Tab switch detected (Alt + Tab)")

    except AttributeError:
        pass

def on_release(key):
    global is_alt_pressed
    try:
        # Reset Alt key press status when released
        if key == keyboard.Key.alt:
            is_alt_pressed = False

    except AttributeError:
        pass

# Start listening to keyboard events
def track_tab_switches():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

track_tab_switches()
