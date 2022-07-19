import cv2

#Use the function cv2.imread() to read an image.
img = cv2.imread('photo/gray.jpg')

"""
# Load an color image in bgr
img = cv2.imread('photo/gray.jpg',1)

# Load an color image in grayscale
img = cv2.imread('photo/gray.jpg',0)

# Load an color image in bgra(a => alpha)
img = cv2.imread('photo/gray.jpg',-1)
"""

#Use the function cv2.imshow() to display an image in a window.
cv2.imshow("gray", img)

#Use the function cv2.imwrite() to save an image.
cv2.imwrite("newGray.jpg",img)
