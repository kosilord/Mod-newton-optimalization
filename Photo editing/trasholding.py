import cv2 as cv


img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')
cv.imshow('img',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thrasholding
threshold,thresh = cv.threshold(gray,150, 255, cv.THRESH_BINARY)
cv.imshow(' simple threshold',thresh)

threshold,thresh_inv = cv.threshold(gray,150, 255, cv.THRESH_BINARY_INV) # odwraca kolory 
cv.imshow('simple threshold with inv ',thresh_inv)

#adaptive thrasholding
""" adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,5) """
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,5,5)

cv.imshow('adaptive thrash',adaptive_thresh)

cv.waitKey(0)
