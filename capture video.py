###
# Capture video from camera
###
'''
import cv2
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    # ret => bool, frame => image
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow("frame", frame)

    #press "q" to end the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''

###
# Read video and playing the video 
###
'''
import cv2

cap = cv2.VideoCapture("video/Time Clock.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
'''

###
# Capture video from camera and saving the video 
###

import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#VideoWriter (filename, fourcc, double fps, Size frameSize, bool isColor=true)
out = cv2.VideoWriter('output.mp4',fourcc, 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()