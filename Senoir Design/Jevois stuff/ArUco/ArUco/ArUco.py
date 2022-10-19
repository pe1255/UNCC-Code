import libjevois as jevois
import cv2
import numpy as np
 
class Hello:
    def __init__(self):
      self.dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
      self.params = cv2.aruco.DetectorParameters_create()
      self.timer = jevois.Timer('ArUco detection', 50, jevois.LOG_DEBUG)
 
    def process(self, inframe, outframe):
      img = inframe.getCvBGR()
      self.timer.start()
      grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      corners, ids, rej = cv2.aruco.detectMarkers(grayimg, self.dict, parameters = self.params)
      img = cv2.aruco.drawDetectedMarkers(img, corners, ids)
      
      if str(ids) != 'None':                                # new code
        for id in ids:                                      # new code
          jevois.sendSerial('Detected ArUco {}'.format(id)) # new code
      
      fps = self.timer.stop()
      cv2.putText(img, fps, (3,img.shape[0]-7), cv2.FONT_HERSHEY_SIMPLEX,
          0.4, (255,255,255), 1, cv2.LINE_AA)
      outframe.sendCv(img)
