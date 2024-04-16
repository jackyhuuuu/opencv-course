#pylint:disable=no-member

import cv2 as cv
import numpy as np

# draw a blank image
blank = np.zeros((500,500,3), dtype='uint8') # 3 is color channels
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[:] = 0,0,255 # paint a certain color in the whole image
blank[200:300, 300:400] = 0,0,255 # paint a certain color in a certain portion of image 
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) 
# (0,0) is the origin of rectangle
# thickness = -1 means fullfill the rectangle with color
cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Jacky!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.putText(image, "Hello, OpenCV!", (x, y), cv.FONT_HERSHEY_TRIPLEX, fontScale, color, thickness)
# cv.FONT_HERSHEY_TRIPLEX 是用于指定文本字体的常量之一
cv.imshow('Text', blank)

cv.waitKey(0)
