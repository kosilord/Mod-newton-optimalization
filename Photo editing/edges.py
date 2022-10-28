import numpy as np
import cv2

img = cv2.imread('C:/Users/kosil/Desktop/lab0-3/kurwamac.jpg')

#resize
resized = cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow('resized',resized)

grey_img = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

cv2.imshow('bottle',img) # orginal photo

blur_grey = cv2.GaussianBlur(grey_img,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow('blur',blur_grey)

canny = cv2.Canny(blur_grey,150,175)
cv2.imshow('canny',canny)

#daileting image
dilated = cv2.dilate(canny,(3,3),iterations=2)
cv2.imshow('dilated',dilated)

#eroding
# eroded = cv2.erode(dilated,(3,3),iterations=3)
# cv2.imshow('erodet',eroded)

#croping
croped = img[50:200,60:400]



cv2.waitKey(0)