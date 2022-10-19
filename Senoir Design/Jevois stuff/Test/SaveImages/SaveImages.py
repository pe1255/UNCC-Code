import libjevois as jevois
import cv2
import numpy as np

## Save Images to JeVois A33 Camera
#
# Add some description of your module here.
#
# @author Eric Lee
# 
# @videomapping YUYV 640 480 30 YUYV 640 480 30 Test SaveImages
# @email 
# @address 123 first street, Los Angeles CA 90012, USA
# @copyright Copyright (C) 2018 by Eric Lee
# @mainurl 
# @supporturl 
# @otherurl 
# @license 
# @distribution Unrestricted
# @restrictions None
# @ingroup modules
class SaveImages:
    def __init__(self):
        self.frame = 0
    
    ## Process function with no USB output
    def processNoUSB(self, inframe):
        img = inframe.getCvBGR()
        cv2.imwrite("/jevois/data/saveimages{}.png".format(self.frame), img)
        self.frame += 1    
    
    def process(self, inframe, outframe):
        img = inframe.getCvBGR()
        outframe.sendCv(img)
