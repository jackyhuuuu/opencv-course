#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # (7,7) is kernel size
cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)
# blur：经过模糊处理的输入图像。模糊操作有助于减少噪声并使边缘检测更准确
# 125：低阈值，用于边缘连接。低于该阈值的像素将被视为边缘，但是它们只有在连接到高于高阈值的像素时才被接受为真正的边缘
# 175：高阈值，用于边缘连接。高于该阈值的像素被认为是真正的边缘像素
# cv.Canny() 函数将返回一个包含边缘的二进制图像，其中检测到的边缘像素被标记为白色（255），而非边缘像素被标记为黑色（0）
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# canny：输入的二值图像，通常是经过边缘检测后得到的图像
# (7, 7)：膨胀操作的核（kernel）的大小，这里是一个 7x7 的正方形核，用于膨胀操作
# iterations=3：膨胀操作的迭代次数，指定对输入图像进行膨胀操作的次数
# 膨胀操作的作用是将图像中的白色区域进行扩张，从而增加其大小，而黑色区域则不受影响
# 这通常用于连接图像中的元素或填充小的空洞。在边缘检测后进行膨胀操作可以弥合边缘之间的空隙，使得边缘更加连续
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
# the reverse operation of dilated
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
