import threading
import pydirectinput
import time


def press_key_in_background(key, command):
    thread = threading.Thread(target=press_key, args=(key, command,))
    thread.start()


def press_key(key, command):
    if command == 'press':
        pydirectinput.keyDown(key)
        time.sleep(0.8)
        pydirectinput.keyUp(key)
    elif command == 'keydown':
        pydirectinput.keyDown(key)
    elif command == 'keyup':
        pydirectinput.keyUp(key)