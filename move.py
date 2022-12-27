import pyautogui
import time
import random
from datetime import datetime

stop_time = "18:00:00"
wait_max = 30

while True:
  current_time = datetime.now().strftime("%H:%M:%S")
  wait_time = random.randint(0, wait_max)
  if current_time == stop_time:
    print("Quitting time")
    break
screen_width, screen_height = pyautogui.size()
x = random.randint(0, screen_width)
y = random.randint(0, screen_height)
pyautogui.moveTo(x, y)
x, y = pyautogui.position()
print(f"{current_time} - waitTime: ({wait_time}s) -|- Pointer coords: ({x}, {y})")
time.sleep(wait_time)
