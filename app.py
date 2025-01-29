import pandas as pd
import pyautogui
import time

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("youtube.com")
pyautogui.press("enter") 
time.sleep(2)
pyautogui.click(x=900, y=118)
pyautogui.write("cepo de madeira")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=497, y=356)