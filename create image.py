import cv2
import numpy as np

###
#Create a black image.
###

blackImg = np.zeros((512,512,3), np.uint8)

###
#Create a white image.
###

whiteImg = np.ones((512,512,3), np.uint8)*255

###
#Create a red image.
###

blackImg2 = np.zeros((512,512,3), np.uint8)
blackImg2[:,:] = [0,0,255]
redImg = blackImg2


###
#change color of a part in the image
###

img = np.zeros((512,512,3), np.uint8)

#spr => starting point of row
#epr => endpoint of row (not included endpoint)
#spc => starting point of column
#epc => endpoint of column (not included endpoint)
#img[spr:epr, spc:epc]
img[100:350, 300:500] = [255,255,255]

#use imshow() function to see images.

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
