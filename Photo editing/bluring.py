import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')

cv.imshow('img',img)

#averaging
avrage = cv.blur(img, (3,3))
cv.imshow('average',avrage)

#gaudsian blur to samo co na górze tylko z wagami
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gausian blur', gaussian)

#medianBlur
median = cv.medianBlur(img, 3)
cv.imshow('median',median)

#bilateral apllays bluring but dont take edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilat',bilateral)

cv.waitKey(0)