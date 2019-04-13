#https://levelup.gitconnected.com/face-detection-with-python-using-opencv-5c27e521c19a
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import cv2
# Draw a diagonal red line with thickness of 5 px
img = np.zeros(shape=(512,512,3),dtype=np.int16)
line_red = cv2.line(img,(0,0),(511,511),(255,0,0),5)
plt.imshow(line_red)
rectangle= cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)
plt.imshow(rectangle)
circle = cv2.circle(img,(447,63), 63, (0,0,255), -1) # -1 corresponds to a filled circle 
plt.imshow(circle)
font = cv2.FONT_HERSHEY_SIMPLEX
text = cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
plt.imshow(text)
plt.show()
