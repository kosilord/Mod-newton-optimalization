import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')
b,g,r = cv.split(img)
blank = np.zeros(img.shape[:2],dtype='uint8')

# cv.imshow('orginal',img)
# cv.imshow('blue',b)
# cv.imshow('greeen',g)
# cv.imshow('red',r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

# cv.imshow('blue',blue)
# cv.imshow('greeen',green)
# cv.imshow('red',red)

merged = cv.merge([b,g,r])
cv.imshow('marged',merged)


cv.waitKey(0)