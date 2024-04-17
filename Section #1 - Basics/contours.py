#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
# -1：要绘制的轮廓索引, 如果设置为负数（-1），则绘制所有的轮廓
# (0, 0, 255)：绘制轮廓的颜色, 这里是红色，表示 (B, G, R) 形式的颜色值
# 1：轮廓的线条粗细, 表示轮廓线的宽度
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
