import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/kosil/Desktop/lab0-3/cipa.png')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2RGB)

#grayscale histogram
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('numbers of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)