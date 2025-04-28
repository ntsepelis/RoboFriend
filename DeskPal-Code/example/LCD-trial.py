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

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
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
    
    for i in range(5):
        # eyes
        eyes = Image.new("RGB", (disp.width, disp.height), "BLACK")
        draw = ImageDraw.Draw(eyes)
        font18 = ImageFont.truetype("../Font/Font00.ttf",18) 
        draw.ellipse((35,35,65,65), fill = (0,255,0))
        draw.ellipse((95,35,125,65), fill = (0,255,0))
        disp.ShowImage(eyes)
        time.sleep(2)
    
        # blink
        blink = Image.new("RGB", (disp.width, disp.height), "BLACK")
        draw2 = ImageDraw.Draw(blink)
        draw2.line([(35, 50),(65,50)], fill = (0,255,0),width = 5)
        draw2.line([(95, 50),(125,50)], fill = (0,255,0),width = 5)
        disp.ShowImage(blink)
        time.sleep(0.5)
    
        # eyes
        draw.ellipse((35,35,65,65), fill = (0,255,0))
        draw.ellipse((95,35,125,65), fill = (0,255,0))
        disp.ShowImage(eyes)
        time.sleep(2)
    
    '''

    logging.info("draw text")
    Font0 = ImageFont.truetype("../Font/Font00.ttf",16)
    Font1 = ImageFont.truetype("../Font/Font01.ttf",20)
    Font2 = ImageFont.truetype("../Font/Font02.ttf",25)    
    draw.text((5, 40), 'Hello world', fill = "BLACK",font=Font0)
    draw.text((5, 60), 'WaveShare', fill = "RED",font=Font1)
    draw.text((5, 80), '1234567890', fill = "GREEN",font=Font2)
    text= u"微雪电子"
    draw.text((5, 100),text, fill = "BLUE",font=Font0)
    
    '''
    
    #im_r=image.rotate(90)
    #disp.ShowImage(image)

    #time.sleep(3)
    
    '''
    logging.info("show image")
    image = Image.open('../pic/LCD_1inch8.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(3)
    '''
    
    disp.module_exit()
    logging.info("quit:")
    
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
