from pywinauto.application import Application
import pyautogui
import time

app = Application().start("C:\\Program Files\\blp\\Wintrv\\WINTRV.EXE")
time.sleep(40)
#Bring desktop back
pyautogui.click(1910, 1060)
time.sleep(5)
#Open first screen only
pyautogui.click(330, 1060)
time.sleep(1)
pyautogui.click(280, 960)
time.sleep(1)
pyautogui.click(500, 500)
time.sleep(15)
pyautogui.click(100, 270)
pyautogui.typewrite('jaycsa')
time.sleep(3)
pyautogui.click(100, 370)
pyautogui.typewrite('password')
time.sleep(3)
pyautogui.click(100, 460)
time.sleep(45)
#For launchpad
pyautogui.click(1880, 5)
#For mini launchpad
time.sleep(5)
pyautogui.click(325, 5)

