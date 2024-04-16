#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) 
    # 通过 np.float32() 创建了一个2x3的变换矩阵 transMat，用来描述平移变换
    # 这个矩阵的第一行[1, 0, x]表示在x轴上的平移量，第二行[0, 1, y]表示在y轴上的平移量
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions) # 调用cv.warpAffine()函数, 该函数用于对图像进行仿射变换

# -x --> Left
# -y --> Up   
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    # cv.getRotationMatrix2D()函数创建一个旋转矩阵rotMat, 接受三个参数：旋转中心点rotPoint、旋转角度angle和缩放比例1.0
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
# flip = cv.flip(img, 1) # flip horizontally
# flip = cv.flip(img, 0) # flip vertically
flip = cv.flip(img, -1) # flip both horizontally and vertically
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
