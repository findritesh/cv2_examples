import numpy as np
import cv2 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
#%matplotlib inline

img_raw = cv2.imread('mandrill_colour.png')
#type(img_raw) 
#np.ndarray
# It's a 3d array as can be seen by running following command
#img_raw.shape 
# OpenCV expects primary colors in BGR and matplot
# lib expects it in RGB, hence, we need to convert
# the formatting
#plt.imshow(img_raw)
#plt.show()
img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
#plt.imshow(img)
#plt.show()
# Below code only keeps the image open
# if escape has not been pressed
while True:
    cv2.imshow('mandrill',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

# We can save these images
cv2.imwrite('mandaril_out.png',img)