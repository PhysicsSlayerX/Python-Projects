##################################################### 
# Import the relevant modules
#####################################################
from ast import literal_eval as make_tuple
from datetime import datetime
from tkinter import LEFT, Button
from time import sleep
from turtle import left
import pyautogui

#####################################################
# Dashboard
#####################################################

# Number of browsers
browsers = 1
name_list = ['All1', 'All2', 'All3', 'All4', 
             'Exit1', 'Exit2', 'Exit3', 'Exit4', 
             'TH1','TH2', 'TH3', 'TH4',
             'Back1', 'Back2', 'Back3', 'Back4',
             'HP1', 'HP2', 'HP3', 'HP4',
             'RA1', 'RA2', 'RA3', 'RA4']

pos = []
timeInterval = 0.25; #one second interval
numSteps = 24;
secs = 1
minutes = 60*secs
bombingTime = 20*minutes
restingTime = 75*minutes

#####################################################
# Import the locations.txt
#####################################################
with open('realLoc.txt') as f:
    lines = f.read().splitlines()

# Dictionary #
line = 0 
for browser in range(1, browsers+1):
    pos.append(dict())
    count = 0
    for item in lines[line:(browser*numSteps)]:
        t_item = make_tuple(item)
        pos[browser-1][name_list[count]] = t_item
        count += 1
    line += numSteps

print(pos)

#Give the python file some time before continuing
print("Commencing Program...")
sleep(3)

#Prints the resolution of your screen
print("Get screen resolution")
print(pyautogui.size()) 

# Prints the current position of the mouse
print("Get initial mouse cursor position")
print(pyautogui.position()) 

#####################################################
# Automation
#####################################################
count = 0
while True:
    for i in range(browsers):
        pyautogui.moveTo(x=pos[i][name_list[count]][0], y=pos[i][name_list[count]][1], duration=timeInterval)
        sleep(timeInterval)
        print('Move to ' + name_list[count])
        pyautogui.click(x=pos[i][name_list[count]][0], y=pos[i][name_list[count]][1], clicks = 5, interval = timeInterval, button='left')
        #pyautogui.click()
        print('click ' + name_list[count])
        sleep(timeInterval)
        count +=1
        print(count)
        if count == 12:
            print('Bombing time')
            sleep(bombingTime)
            print('Let them sleep')
            
        if count >= 24:
            count = 0
            print('Sleeping Time')
            sleep(restingTime)
            print('Wake the bombers!')
            
            

#Move the mouse over time
#pyautogui.moveTo(100,100, 0.5)

#Move the mouse relative to its current position
#pyautogui.moveRel(100, 100, 3)

# Click
#pyautogui.click(500,500, 3, 3, button = "left")

#pyautogui.tripleClick()
#pyautogui.doubleClick()
#pyautogui.rightClick()
#pyautogui.leftClick()

#Scrolling

#Scrolls up
#pyautogui.scroll(500)

#Scrolls down
#pyautogui.scroll(-500)

# Mouse up and down
#pyautogui.mouseUp(100,100, button="left")
#pyautogui.mouseDown(100,100, button="left")

# Example of mouse up and down
#pyautogui.mouseDown(300, 400, button="left")
#pyautogui.moveTo(800,400,3)
#pyautogui.mouseUp()
#pyautogui.moveTo(1000,400,3)

# Create a square spiral

# time.sleep(1)
# distance = 300
# while distance > 0:
#     pyautogui.dragRel(distance, 0, 1, button="left")
#     distance -= 20
#     pyautogui.dragRel(0, distance, 1, button="left")
#     pyautogui.dragRel(-distance, 0, 1, button="left")
#     distance -= 20
#     pyautogui.dragRel(0, -distance,1, button="left")
#     time.sleep(2)
    
# Tiktok Liker - Example
# time.sleep(3)

# for i in range(10):
#     pyautogui.moveTo(450,500)
#     time.sleep(1)
#     pyautogui.moveTo(854,515)
#     time.sleep(1)
#     pyautogui.leftClick()

# # Keyboard functions
# pyautogui.write("hello")
# pyautogui.press("enter")
# pyautogui.press("space")

# # Dino game
# time.sleep(3)
# for i in range(20):
#     pyautogui.preess("space")
#     time.sleep(0.5)

# Screenshot
#pyautogui.screenshot("screenshot.png")