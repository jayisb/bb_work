from pywinauto.application import Application
import pyautogui
import time
from PIL import Image
import pyscreenshot as ImageGrab
import datetime
import os
import pyperclip

def startbb():
    app = Application().start("C:\\Program Files\\blp\\Wintrv\\WINTRV.EXE")
    time.sleep(40)
    a = pyautogui.locateOnScreen("C:\\Users\\Administrator\\Pictures\\max.PNG")
    b = pyautogui.locateOnScreen("C:\\Users\\Administrator\\Pictures\\max1.PNG")
    c = pyautogui.locateOnScreen("C:\\Users\\Administrator\\Pictures\\max2.PNG")
    d = pyautogui.locateOnScreen("C:\\Users\\Administrator\\Pictures\\max3.PNG")
    if a or b or c or d:
        if a:
           buttonx, buttony = pyautogui.center(a)
           pyautogui.click(buttonx, buttony)
        elif b:
            buttonx, buttony = pyautogui.center(b)
            pyautogui.click(buttonx, buttony)
        elif c:
            buttonx, buttony = pyautogui.center(c)
            pyautogui.click(buttonx, buttony)
        else:
            buttonx, buttony = pyautogui.center(d)
            pyautogui.click(buttonx, buttony)
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
    time.sleep(5)
    pyautogui.click(300,50)
    pyautogui.typewrite("SPLC")
    #pyautogui.click(300,50)
    time.sleep(2)
    pyautogui.click(150,140)
    time.sleep(5)
    #Disable panel
    pyautogui.click(200, 880, button='right')
    pyautogui.click(210, 890)
    time.sleep(5)

def closebb():
    first_run = 0
    pyautogui.moveTo(900, 1050)
    time.sleep(1)
    pyautogui.rightClick(330, 1060)
    time.sleep(1)
    pyautogui.click(353, 1036)
    time.sleep(3)
    pyautogui.click(950, 590)
    time.sleep(5)
    
def screenshot():
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print timestr
    file_name = "sample_" + timestr + ".png"
    file_location = os.path.join('C:\\Users\\Administrator\\Desktop\\suppliers', file_name)
    print file_location
    im.save(file_location)
    return os.path.join('C:\\Users\\Administrator\\Desktop\\suppliers', file_name)

def screenshot1():
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print timestr
    file_name = "sample_" + timestr + ".png"
    file_location = os.path.join('C:\\Users\\Administrator\\Desktop\\customers', file_name)
    print file_location
    im.save(file_location)
    return os.path.join('C:\\Users\\Administrator\\Desktop\\customers', file_name)

def reader():
    with open('C:\\Users\\Administrator\\Desktop\\status.txt', 'r+') as f:
        text = f.read()
        print text
        line_number = int(text)
        next_num = int(text) + 1
        text = str(next_num)
        f.seek(0)
        f.write(text)
        f.truncate()
    
    with open('C:\\Users\\Administrator\\Downloads\\file_to_process_jp.csv') as file:
        second_line = list(file)[line_number]
        print second_line
        print second_line.split(",")[0]
        firm_name = second_line.split(",")[0].replace("\"","").upper()
        print firm_name

    return firm_name        

firm_count = 0
first_run = 0

def closebb():
    first_run = 0
    pyautogui.moveTo(900, 1050)
    time.sleep(1)
    pyautogui.rightClick(330, 1060)
    time.sleep(1)
    pyautogui.click(353, 1036)
    time.sleep(3)
    pyautogui.click(950, 590)
    time.sleep(5)

if __name__ == "__main__":
        startbb()
        while firm_count < 1390:
            pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\quan.png', region=(1350,121, 600, 40))
            time.sleep(2)
            if pyautogui.locate("C:\\Users\\Administrator\\Pictures\\Capture.PNG", "C:\\Users\\Administrator\\Desktop\\quan.png"):
                company_name = reader()
                company_name = company_name 
                #Equity Name
                pyautogui.click(150,130)
                time.sleep(1)
                pyautogui.typewrite(company_name)
                time.sleep(2)
                pyautogui.click(150,210)
                time.sleep(2)

                #Ticker
                pyautogui.click(1000,200)
                time.sleep(1)
                pyautogui.click(1000,240)
                time.sleep(0.5)

                #Currency
                pyautogui.click(700,200)
                time.sleep(1)
                pyautogui.click(1190,610)
                time.sleep(3.5)

                #Date
                pyautogui.click(1730, 170)
                pyautogui.typewrite('06')
                time.sleep(0.1)
                pyautogui.typewrite('30')
                time.sleep(0.1)
                pyautogui.typewrite('13')
                time.sleep(0.1)
                pyautogui.press('enter')
                time.sleep(3)
                
                #Disable warning
##                if first_run == 0:
##                    if pyautogui.locateOnScreen("C:\\Users\\Administrator\\Pictures\\close.PNG"):
##                            pyautogui.click(1500,680)
##                            time.sleep(1)
##                            first_run = 1

                pyautogui.click(700, 240)
                time.sleep(1)
                pyautogui.click(730, 320)
                time.sleep(1)
                pyautogui.click(1000, 180)
                time.sleep(4)
                im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\up.png', region=(1870,290, 60, 60))
                time.sleep(1)
                print "check"
                test_v = pyautogui.locate("C:\\Users\\Administrator\\Pictures\\Up1.PNG", "C:\\Users\\Administrator\\Desktop\\up.png") or pyautogui.locate("C:\\Users\\Administrator\\Pictures\\Up3.PNG", "C:\\Users\\Administrator\\Desktop\\up.png") or pyautogui.locate("C:\\Users\\Administrator\\Pictures\\Up4.PNG", "C:\\Users\\Administrator\\Desktop\\up.png")
                print "check1"
                print test_v
                if test_v:
                    im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\prev.png', region=(0,850, 50, 38))
                    time.sleep(1)
                    while(True):
                        pyautogui.moveTo(1850, 240)
                        screenshot_name = screenshot()
                        time.sleep(0.5)
                        im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\curr.png', region=(0,955, 50, 38))
                        time.sleep(1)
                        if pyautogui.locate("C:\\Users\\Administrator\\Desktop\\curr.png", "C:\\Users\\Administrator\\Desktop\\prev.png"):
                            print "end"
                            os.remove(screenshot_name)
                            break
                        else:
                            print "entered imp"
                            im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\prev.png', region=(0,955, 50, 38))
                            time.sleep(1)
                            for x in range(18):
                                pyautogui.click(1910, 980)
                                time.sleep(0.01)
                else:
                        print "simple life"
                        screenshot()
                        time.sleep(1)

                pyautogui.click(700, 240)
                time.sleep(1)
                pyautogui.click(730, 350)
                time.sleep(1)
                pyautogui.click(1000, 180)
                time.sleep(4)
                im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\up.png', region=(1870,290, 60, 60))
                time.sleep(1)
                print "check"
                test_v = pyautogui.locate("C:\\Users\\Administrator\\Pictures\\Up1.PNG", "C:\\Users\\Administrator\\Desktop\\up.png") or pyautogui.locate("C:\\Users\\Administrator\\Pictures\\Up3.PNG", "C:\\Users\\Administrator\\Desktop\\up.png") or pyautogui.locate("C:\\Users\\Administrator\\Pictures\\Up4.PNG", "C:\\Users\\Administrator\\Desktop\\up.png")
                print "check2"
                if test_v:
                    im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\prev.png', region=(0,850, 50, 38))
                    time.sleep(1)
                    while(True):
                        pyautogui.moveTo(1850, 240)
                        screenshot_name = screenshot1()
                        time.sleep(1)
                        im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\curr.png', region=(0,955, 50, 38))
                        time.sleep(1)
                        if pyautogui.locate("C:\\Users\\Administrator\\Desktop\\curr.png", "C:\\Users\\Administrator\\Desktop\\prev.png"):
                            print "end"
                            os.remove(screenshot_name)
                            break
                        else:
                            print "entered imp"
                            im = pyautogui.screenshot('C:\\Users\\Administrator\\Desktop\\prev.png', region=(0,955, 50, 38))
                            time.sleep(1)
                            for x in range(18):
                                pyautogui.click(1910, 980)
                                time.sleep(0.01)
                else:
                        print "simple life"
                        screenshot1()
                        time.sleep(1)
                firm_count = firm_count + 1
            else:
                first_run = 0
                closebb()
                startbb()
            
	

