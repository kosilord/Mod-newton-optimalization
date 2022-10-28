import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

# Sobel 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
sobel_combined = cv.bitwise_or(sobelx,sobely)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('Sobel cały',sobel_combined)
#canny

canny = cv.Canny(gray,150,175)
cv.imshow('cany',canny)
cv.waitKey(0)