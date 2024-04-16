#pylint:disable=no-member

import cv2 as cv

# img = cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75): # set the dafault scale to 0.75
    # works on Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height): # change the resolution
    # only works on Live video
    capture.set(3, width)
    capture.set(4, height)
    # 函数的一般形式是 capture.set(property, value)，其中 property 是要设置的属性的标识符，value 是要设置的属性值
    # 对于capture.set()函数来说，参数3和参数4分别表示视频帧的宽度和高度
    # e.g. changeRes(640, 480)表示将视频的分辨率设置为640x480
    
# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = .2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
