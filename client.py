from __future__ import print_function
import cv2
from fer import FER
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from datetime import datetime
import time
import json
import cv2
import time
import base64
import requests

addr = 'https://MadDifferentBrowsers-1.adebola121.repl.co'
test_url = addr + '/api/test'

# prepare headers for http request
headers = {'userid': 'user1'}

#takes the webcam when run, does not ask for presaved video
cap = cv2.VideoCapture(0)
#i = 0
emotion_detector = FER()

# used to record the time when we processed last frame
prev_frame_time = 0
# used to record the time at which we processed current frame
new_frame_time = 0

 
while(cap.isOpened()):
    ret, frame = cap.read()
     
    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break
    # time when we finish processing for this frame
    new_frame_time = time.time()
    # Calculating the fps
 
    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
 
    # converting the fps into integer
    fps = int(fps)
 
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
     
    # Save Frame by Frame into disk using imwrite method
    #cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    result = emotion_detector.detect_emotions(frame)

    retval, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')
    
    if result:
        response = requests.post(test_url, data=jpg_as_text, headers=headers)
        
        timestamp = time.time()
        dt_object = datetime.fromtimestamp(timestamp)
        # now = datetime.now()
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        result.append({"DateTime": dt_object})
        result.append({"Frames per second": fps})
        print(result, "\n")
        print(response.text, "\n")
    #i += 1
 
cap.release()
cv2.destroyAllWindows()

# # individual image
# input_image = cv2.imread("smile.jpg")
# emotion_detector = FER()
# # Output image's information
# result = emotion_detector.detect_emotions(input_image)
# print(result)

# vidcap = cv2.VideoCapture('webcam.mov')
# success,image = vidcap.read()
# count = 0
# while success:
#   #cv2.imwrite("images/frame%d.jpg" % count, image)     # save frame as JPEG file
#   #input_image = cv2.imread(image)
#   success,image = vidcap.read()
#   emotion_detector = FER()
#   # Output image's information
#   result = emotion_detector.detect_emotions(image)
#   print(result)
#   count += 1
