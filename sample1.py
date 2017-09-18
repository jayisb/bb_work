from pywinauto.application import Application
import pyautogui
import time

pyautogui.click(300,50)
pyautogui.typewrite("SPLC")
#pyautogui.click(300,50)
time.sleep(2)
pyautogui.click(150,140)
time.sleep(5)
#Disable panel
pyautogui.click(200, 880, button='right')
pyautogui.click(210, 890)
