import cv2
import numpy as np
import yaml
import os
import serial
import re

ser = serial.Serial("COM10", 115200)                           # Switch COM port to desired port

print("Data Received: ")

camLocationX = []
realTime = []
while True:

    xOffset = []
    xzCoord = []

    coordinates = ser.readline()
    #coordinates = coordinates.strip()
    coordinates = coordinates.decode("utf-8")
    print('cord= ', coordinates)
    realTime.append(coordinates)
    #print('time = ', time)
    if 'done' in coordinates :
        data = str(realTime)
        print('cord1= ', data)

