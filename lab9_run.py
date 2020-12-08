import keras
from keras.models import load_model
import numpy as np
import cv2
from adafruit_motorkit import MotorKit

model = load_model()

kit = MotorKit()
cap = cv2.VideoCapture(0)

While True:
    ret, frame = cap.read()
    #image_processing start
    
    #resize to model input
    #flatten to array
    #adjust to correct array size for model input
    
    #image_processing end
    result = model.predict(image_processing_frame)
    if result == 'label': #If there is "obstacle", execute steer-and-return-to-track-sequence
        #motor_control start
          
        #steer left - 30 deg
        #move a little
        #steer right - 30 deg
        #move a little
        #steer right - 30 deg
        #move a little
        #steer left - 30 deg
        
        #motor_control end
    else: #If there is not "obstacle" in sight, continue moving forward
        break

#Where to insert [auto-steering]??????

# motor_release
cap.release()
cv2.destroyAllWindows()