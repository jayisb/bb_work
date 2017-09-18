from PIL import Image
import pyscreenshot as ImageGrab
import datetime
import time
import os
import pyperclip

def screenshot():
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print timestr
    file_name = "sample_" + timestr + ".png"
    file_location = os.path.join('C:\\Users\\31049\\Desktop\\03-05-2017', file_name)
    print file_location
    im.save(file_location)

def screenshot1():
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print timestr
    file_name = "sample_" + timestr + ".png"
    file_location = os.path.join('C:\\Users\\31049\\Desktop\\03-05-2017_c', file_name)
    print file_location
    im.save(file_location)

def screenshot2():
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print timestr
    file_name = "sample_" + timestr + ".png"
    file_location = os.path.join('C:\\Users\\31049\\Desktop\\03-05-2017_p', file_name)
    print file_location
    im.save(file_location)

def reader():
    with open('C:\\Users\\31049\\Desktop\\status.txt', 'r+') as f:
        text = f.read()
        print text
        line_number = int(text)
        next_num = int(text) + 1
        text = str(next_num)
        f.seek(0)
        f.write(text)
        f.truncate()
    
    with open('C:\\Users\\31049\\Downloads\\file_to_process_27.csv') as file:
        second_line = list(file)[line_number]
        print second_line
        print second_line.split(",")[0]
        firm_name = second_line.split(",")[0].replace("\"","").upper()
        print firm_name
        pyperclip.copy(firm_name)

if __name__ == "__main__":
    while True:
        x = raw_input('Press enter for a random letter...')
        print x
        if x == "":
            screenshot()

        if x == "a":
            screenshot1()
        
        if x == "s":
            screenshot2()

        if x == "0":
            reader()

        if x == "d":
            break
    
