from pickletools import uint8
import cv2 as cv
import numpy as np 

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')


blank = np.zeros(img.shape,dtype=u'int8')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny',canny)

""" ret,tresh = cv.threshold(gray, 150, 255,cv.THRESH_BINARY)
cv.imshow('tresz',tresh) """

canny = cv.Canny(gray, 125, 175)
cv.imshow('canny',canny)

#Rarer_tree cos za gunwoi #retr_list wszystkie   chain_approx_none - wszystkie bierze chain_approx_simple- 2 końce
counturs, hierarchies = cv.findContours(canny, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(counturs)} counturs found ')
# cv.imshow('konturki',counturs)

cv.drawContours(blank, counturs, -1,(0,0,255),1)
cv.imshow('conturs',blank)

cv.waitKey(0)
