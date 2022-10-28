import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/kurwamac.jpg')

cv.imshow('wittt',img)


#moving photo
def translate(img ,x ,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> left
# -y --> up
tranlated = translate(img, 100,100)
cv.imshow('translated', tranlated)

#rotating 
def rotate(img, angle ,rotPoint = None):
        (height,width) = img.shape[:2]

        if rotPoint is None:
            rotPoint = (width//2,height//2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width,height)
        return cv.warpAffine(img,rotMat,dimensions)

rotateed = rotate(img, 45)
cv.imshow('rotated', rotateed)

#fliping odwracanie lustrzane 0 - wertukalnie 1- horyzontal -1 - horyzont i wertakularnie
flip = cv.flip(img,0)
cv.imshow('')

cv.waitKey(0)