import ctypes
import time
import random
from datetime import datetime

stop_time = "18:00:00"
wait_max = 30


class POINT(ctypes.Structure):
  _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


while True:
  current_time = datetime.now().strftime("%H:%M:%S")
  wait_time = random.randint(0, wait_max)
  if current_time == stop_time:
    print("Quitting time")
    break
screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)
x = random.randint(0, screen_width)
y = random.randint(0, screen_height)
ctypes.windll.user32.SetCursorPos(x, y)
point = POINT()
ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
x, y = point.x, point.y
print(f"{current_time} - waitTime: ({wait_time}s) -|- Pointer coords: ({x}, {y})")
time.sleep(wait_time)
