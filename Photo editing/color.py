import cv2 as cv

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR to HSV 
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to  L*a*B
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

cv.waitKey(0)