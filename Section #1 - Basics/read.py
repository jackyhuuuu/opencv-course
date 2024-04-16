#pylint:disable=no-member

import cv2 as cv

# Reading Images
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)
# cv.waitKey()函数用于等待键盘输入。它会等待指定的毫秒数（如果为0，则一直等待），并返回按下的键的ASCII码值。
# 如果没有键被按下，则返回-1。通常，它与cv.destroyAllWindows()一起使用，以确保窗口可以正常关闭。

# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'): # If the letter 'd' is pressed, then break out of the loop
            # cv.waitKey(20)会等待20毫秒（1秒等于1000毫秒），并返回按下的键的ASCII码值。
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
