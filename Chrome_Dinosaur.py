from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *
import numpy as np

Coordinates=dict()
Coordinates["replay"]=(680,190)

Sprites=dict()    
Sprites["replay"]=(666,177,699,206)
Sprites["land"]=(527,218,556,227)
Sprites["land_night"]=(527,218,556,227)
Sprites["dino_standstill"]=(384,196,424,226)
Sprites["dino_moving"]=(406,196,446,226)
Sprites["sky"]=(494,199,517,206)
Sprites["sky_night"]=(494,199,517,206)

stable_value=dict()
stable_value["replay"]=105999
stable_value["land"]=64467
stable_value["land_night"]=0
stable_value["dino_standstill"]=199836
stable_value["dino_moving"]=201312
stable_value["sky"]=39767
stable_value["sky_night"]=0

def click(target):
    pyautogui.click(Coordinates[target])

def press(button):
    pyautogui.keyDown(button)
    time.sleep(0.1)
    pyautogui.keyUp(button)
    
def changing(target):    
    image=ImageGrab.grab(Sprites[target])
    gray_image=ImageOps.grayscale(image)
    target_pixels=np.array(gray_image)
    
    return target_pixels.sum()!=stable_value[target]

def value(target):
    image=ImageGrab.grab(Sprites[target])
    gray_image=ImageOps.grayscale(image)
    target_pixels=np.array(gray_image)
    
    return target_pixels.sum()

def scan_value(target):
    while(True):
        print(value(target))

def game():
    while(True):
        if(value("land")<=40000):
            if(changing("land_night") ):
                press("space")
            if(changing("sky_night") ):
                press("space")
        else:
            if(changing("land") ):
                press("space")
            if(changing("sky")):
                press("down") 
            if(not(changing("replay"))):
                time.sleep(3)
game()
