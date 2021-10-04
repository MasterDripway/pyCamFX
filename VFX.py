#!./venv/Scripts/python.exe
import cv2, random
import numpy as np

face_cascade = cv2.CascadeClassifier("data\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("data\\haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
box = False
tts = False
state = None
flipdisplay = False
blur = False
flipwithface = False
canny = False
hide = False
clearblur = False
pencilSketch = False
lag = False
choices = [cv2.COLOR_RGB2HSV, cv2.COLOR_RGB2BGR, cv2.COLOR_RGB2HLS, cv2.COLOR_RGB2LAB]
multi = 10


while True:
    ret, frame = cap.read()
    img = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if state != None:
        img = cv2.cvtColor(img, state)
    
    if pencilSketch:
        invimg = 255 - gray
        gauss = cv2.GaussianBlur(invimg, (21, 21), 0)
        invgauss = 255 - gauss
        img = cv2.divide(gray, invgauss, scale=256.0)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)


    if blur:
        img = cv2.blur(img, (10, 10))

    if flipwithface:
        img = np.array(img[::-1,::-1,:])
    



    
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 2)

        if hide:
            region = np.zeros(img[y:y+h, x:x+w].shape)
            region[:] = [235, 12, 108]
            img[y:y+h, x:x+w] = region
        if box:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            img[y: y + h, x: x + w, :] = roi_color

        if flipdisplay:
            img = np.array(img[::-1,::-1,:])


    if clearblur:
        img = cv2.medianBlur(img, 15)

    if canny:
        img = cv2.Canny(img, 100, 200)


    if lag:
        sh = img.shape
        if sh[0] > multi and sh[1] > multi:
            img = cv2.resize(img, (sh[0] // multi, sh[1] // multi))
            img = cv2.resize(img, (sh[0], sh[1]))



    cv2.namedWindow('SFX', cv2.WINDOW_FREERATIO)
    cv2.imshow('SFX', img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord("2"):
        box = not box
    elif k == ord("1"):
        pencilSketch = not pencilSketch
    elif k == ord("3"):
        state = cv2.COLOR_RGB2HSV
    elif k == ord("4"):
        state = cv2.COLOR_RGB2BGR
    elif k == ord("5"):
        state = cv2.COLOR_RGB2HLS
    elif k == ord("6"):
        state = cv2.COLOR_RGB2LAB
    elif k == ord("7"):
        state = None
    elif k == ord("8"):
        flipdisplay = not flipdisplay
    elif k == ord("9"):
        blur = not blur
    elif k == ord("0"):
        box = False
        state = None
        flipdisplay = None
        blur = False
        flipwithface = False
        canny = False
        hide = False
        clearblur = False
        lag = False
        pencilSketch = False
    elif k == ord("f"):
        flipwithface = not flipwithface
    elif k == ord('a'):
        canny = not canny
    elif k == ord('h'):
        hide = not hide
    elif k == ord('l'):
        lag = not lag
    elif k == ord('m'):
        clearblur = not clearblur
    else:
        continue

cap.release()
cv2.destroyAllWindows()
