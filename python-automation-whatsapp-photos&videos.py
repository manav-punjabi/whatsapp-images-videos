#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from numpy import genfromtxt
import webbrowser
import time
import pyautogui as gui

interval = 1

position= 1023,230

pos2=1711,96


numbers=genfromtxt('numbers (2).csv',delimiter=',',skip_header=1,dtype='str')
x=input("enter the file path")    

    
for i in numbers:
    url=f'https://wa.me/{i}'
    webbrowser.open(url)
    time.sleep(1)
    gui.click(position)
    time.sleep(2)
    gui.click(pos2)
    time.sleep(interval)
    gui.press('down')
    time.sleep(interval)
    gui.press('enter')
    time.sleep(interval)
    gui.write(x)
    time.sleep(2)
    gui.press('enter')
    time.sleep(1)
    gui.press('enter')
    time.sleep(1)
    gui.press('enter')
    time.sleep(interval)
    gui.keyDown('alt')
    gui.press('tab')
    gui.keyUp('alt')
    gui.keyDown('ctrl')
    gui.press('w')
    gui.keyUp('ctrl')
    time.sleep(1)
    
    

