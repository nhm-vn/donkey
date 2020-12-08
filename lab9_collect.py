import cv2
import time

cap = cv2.VideoCapture(0)
camera_list = []

while True:
    t = time.time()
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(30) & 0xFF
    
    if key = ord('q'):
        break
    else:
        camera_list.append(frame)
        time.sleep(0.03)
        
#camera_list then save to where location?????

cap.release()
cv2.destroyAllWindows()