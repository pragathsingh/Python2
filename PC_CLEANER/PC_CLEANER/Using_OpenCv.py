import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
#'M','J','P','G'
out = cv2.VideoWriter('output1.avi',fourcc,20.0,(640,480))
 
twoout = cv2.VideoWriter('output2.avi',fourcc,60.0,(640,480))
while True:
    ret , frame = cap.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    twoout.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('grey',grey)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
twoout.release()
cv2.destroyAllWindows()


#cap = cv2.VideoCapture("Creating a Snake Game.MKV")
#length = int(cap.get(cv2.Fra))
#print(length)
#cap = cv2.VideoCapture("001 Course Introduction.mp4")
#property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
#length = int(cv2.VideoCapture.get(cap, property_id))
#print( length )