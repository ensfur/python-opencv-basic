import cv2
import numpy as np

###
# Draw a line
###
img = np.zeros((512,512,3), np.uint8)

# img = cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)


###
# Draw a rectangle
###
img = np.zeros((512,512,3), np.uint8)

# img = cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle.
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

###
# Draw a circle
###
img = np.zeros((512,512,3), np.uint8)

#To draw a circle, you need its center coordinates and radius
#img = cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

###
# Draw a ellipse
###
img = np.zeros((512,512,3), np.uint8)

#img = cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

###
# Adding Text to image
###
img = np.zeros((512,512,3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

#img = cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
cv2.putText(img,'OpenCV',(10,480), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()