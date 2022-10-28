import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

ractangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255 ,-1)
circle = cv.circle(blank.copy(), (200,200), 200, 255 ,-1)

cv.imshow('ractanglke',ractangle)
cv.imshow('circle',circle)

#bitwise AND bierze 2 photo i zostawia to co jest tym samym
bitwise_and = cv.bitwise_and(ractangle,circle)
cv.imshow('bitwise and',bitwise_and)

#bitwise Or  jak by dodawanie
bitwise_or = cv.bitwise_or(ractangle,circle)
cv.imshow('bitwise or',bitwise_or)

# bitwise XOR nie wspólne regiony
bitwise_xor = cv.bitwise_xor(ractangle,circle)
cv.imshow('bitwise xor',bitwise_xor)

#bitwise NOT odwraca kolory
bitwise_not = cv.bitwise_not(ractangle)
cv.imshow('ractangle not',bitwise_not)

cv.waitKey(0)