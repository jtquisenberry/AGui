import pyautogui
import time
import datetime
import random

now = datetime.datetime.now()
stop = datetime.datetime(2025, 2, 19, 21, 0, 0)

while now < stop:
    now = datetime.datetime.now()

    #pyautogui.press('volumedown')
    #time.sleep(1)
    #pyautogui.press('volumeup')  # press the F15 key
    #interval = random.randint(280, 440)

    # press the F15 key
    pyautogui.press('f23')
    interval = random.randint(280, 440)
    time.sleep(interval)
