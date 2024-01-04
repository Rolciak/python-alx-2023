import pyautogui
import time

# https://pyautogui.readthedocs.io/en/latest/

screen_w, screen_h = pyautogui.size()

pyautogui.moveTo(10, screen_h - 10, duration=3)
pyautogui.click()
time.sleep(1)
pyautogui.write("notepad\n", interval=0.5)
time.sleep(2)
pyautogui.write("Wake up, Neo!\nFollow the white rabbit", interval=0.25)