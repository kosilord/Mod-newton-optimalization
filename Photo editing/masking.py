import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')

mack = cv.rectangle(blank, (img.shape[1]//2,img.shape[0]//2), (img.shape[1]//2 + 100,img.shape[0]//2 + 100),255,-1)
cv.imshow('mask',mack)

masked = cv.bitwise_and(img,img,mask=mack)
cv.imshow('masked',masked)
cv.waitKey(0)