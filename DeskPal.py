#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch8
from PIL import Image,ImageDraw,ImageFont

from datetime import datetime
import pandas as pd

import RPi.GPIO as GPIO

def button_callback(channel):
    print("Button Pressed!")
    printCalendar()
    time.sleep(1)
        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback)
GPIO.cleanup

'''
INPUT_PIN = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
'''   


# --- CAMERA START

import random
import time
import json
from huskylib import HuskyLensLibrary

hl = HuskyLensLibrary("I2C","", address=0x32)

# Ανάγνωση Αρχείου Ημερολογίου
# Ο τύπος της μεταβλητής είναι DataFrame
df = pd.read_csv('cal.csv')

# Εμφάνιση των Περιεχομένων του Αρχείου
print("\n----- Υποχρεώσεις -----\n") # Τίτλος
print(df) # Περιεχόμενα 


now = datetime.now() # Μεταβλητή σ ημερινής Ημερομηνίας
today = now.strftime("%d/%m/%Y") # Μετατροπή σε οικία μορφή
print("\nΣήμερα:",today) # Εμφάνιση σημερινής Ημερομηνίας
print() # Αλλαγή Σειράς


# Ερώτηση σημερινής υποχρέωσης
# Εμφάνιση αυριανών υποχρεώσεων
for i in range(len(df)):
    day = df['Ημερομηνία'][i]
    #print("Today: " + dates)
    if (day == today):
        print(df['Υποχρέωση'][i] +" σήμερα! Πώς τα πήγες;")
        if (i + 1 < len(df)):
            print("\n- Ετοιμάστηκες για το αυριανό " + df['Υποχρέωση'][i+1] +";")
        

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)

def printEyes():
    eyes = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawEyes = ImageDraw.Draw(eyes)
    drawEyes.ellipse((35,35,65,65), fill = (0,255,0))
    drawEyes.ellipse((95,35,125,65), fill = (0,255,0))
    drawEyes.arc((35,85,125,105),0, 180, fill =(0,255,0),width = 5)
    disp.ShowImage(eyes)
    time.sleep(2)

def printBlink():
    blink = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawBlink = ImageDraw.Draw(blink)
    drawBlink.line([(35, 50),(65,50)], fill = (0,255,0),width = 5)
    drawBlink.line([(95, 50),(125,50)], fill = (0,255,0),width = 5)
    #drawBlink.arc((35,85,125,105),0, 180, fill =(0,255,0))
    drawBlink.arc((65,85,95,105),0, 180, fill =(0,255,0),width = 5)
    disp.ShowImage(blink)
    time.sleep(0.5)

def printBlackEyes():
    blackeyes = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawBlackEyes = ImageDraw.Draw(blackeyes)
    font18 = ImageFont.truetype("../Font/Font00.ttf",18) 
    drawBlackEyes.ellipse((35,35,65,65), fill = (0,255,0))
    #drawBlackEyes.ellipse((45,35,55,65), fill = (0,0,0)) #Makrostena
    drawBlackEyes.ellipse((45,45,55,55), fill = (0,0,0)) # Stroggyla
    drawBlackEyes.ellipse((95,35,125,65), fill = (0,255,0))
    #drawBlackEyes.ellipse((105,35,115,65), fill = (0,0,0))#Makrostena
    drawBlackEyes.ellipse((105,45,115,55), fill = (0,0,0)) # Stroggyla
    drawBlackEyes.arc((65,85,95,105),0, 180, fill =(0,255,0),width = 5)
    disp.ShowImage(blackeyes)
    time.sleep(4)

def printSmile():
    smile = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawSmile = ImageDraw.Draw(smile)
    drawSmile.arc((35,85,125,105),0, 180, fill =(0,255,0))
    drawSmile.arc((35,85,125,105),0, 180, fill =(0,255,0))
    disp.ShowImage(smile)
    time.sleep(4)
    
def printPromt():
    promt = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawPromt = ImageDraw.Draw(promt)
    Font0 = ImageFont.truetype("../Font/Font00.ttf",15)
    drawPromt.text((0, 10),"Press button to communicate", fill = (0,255,0),font=Font0)
    disp.ShowImage(promt)
    time.sleep(2)

def printCalendar():
    '''
    calendar = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawCalendar = ImageDraw.Draw(calendar)
    Font0 = ImageFont.truetype("../Font/Font00.ttf",11)
    drawCalendar.text((0, 0), str(df), fill = (0,255,0),font=Font0)
    disp.ShowImage(calendar)
    time.sleep(10)
    '''
    Font0 = ImageFont.truetype("../Font/Font00.ttf",20)
    for i in range(len(df)):
        day = df['Ημερομηνία'][i]
        #print("Today: " + dates)
        if (day == today):
            msg = Image.new("RGB", (disp.width, disp.height), "BLACK")
            drawMsg = ImageDraw.Draw(msg)
            drawMsg.text((0, 10), df['Υποχρέωση'][i] +" σήμερα! \n Πώς τα πήγες;", fill = (0,255,0),font=Font0)
            disp.ShowImage(msg)
            time.sleep(5)
            try:
                if (hl.blocks().ID == 2):
                    #resp = "Όχι πολύ καλά"
                    my_resp = "\n\n Δεν πειράζει. Την επόμενη \n φορά καλύτερα"
                elif (hl.blocks().ID == 1):
                    #resp = "Τέλεια!"
                    my_resp = "\n\n BRAVO!\n Συνέχισε δυνατά!"
                rsp = Image.new("RGB", (disp.width, disp.height), "BLACK")
                drawResp = ImageDraw.Draw(rsp)
                drawResp.text((0, 10), my_resp, fill = (0,255,0),font=Font0)
                #disp.clear()
                disp.ShowImage(rsp)
                time.sleep(5)
            except Exception as e:
                pass
            if (i + 1 < len(df)):
                tomorow = Image.new("RGB", (disp.width, disp.height), "BLACK")
                drawTomorow = ImageDraw.Draw(tomorow)
                drawTomorow.text((0, 50), "- Ετοιμάστηκες για το αυριανό \n" + df['Υποχρέωση'][i+1] +";", fill = (0,255,0),font=Font0)
                #disp.clear()
                disp.ShowImage(tomorow)
                time.sleep(5)
            

try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_1inch8.LCD_1inch8(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch8.LCD_1inch8()
    Lcd_ScanDir = LCD_1inch8.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    #Set the backlight to 100
    disp.bl_DutyCycle(50)
    
    while(True):
        printBlackEyes()    # eyes
        printBlink()   # blink
        printBlackEyes()    # eyes
        #GPIO.cleanup
        #printSmile()
        #printSmiley()
        #printCalendar()
        
        
    disp.module_exit()
    logging.info("quit:")
    
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
