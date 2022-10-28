import numpy as np
from glob import glob

import cv2
import matplotlib.pylab as plt

plt.style.use('ggplot')

cat_files = glob('C:/Users/kosil/Desktop/lab0-3/cipa.png')
dog_files = glob('C:/Users/kosil/Desktop/lab0-3/cipa2.png')

#img_mpl = plt.imread(cat_files[10])
img_cv22 = cv2.imread(cat_files[0])
img_cv2 = cv2.imread(dog_files[0])

dupa = cv2.subtract(img_cv2,img_cv22) #odejmowanie obrazów

plt.imshow(dupa)
plt.show()
pierwotny = cv2.cvtColor(img_cv22, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img_cv22, cv2.COLOR_BGR2GRAY)
dupaa = cv2.cvtColor(dupa,cv2.COLOR_BGR2GRAY)

low_threshold = 25
high_threshold = 100
edges = cv2.Canny(gray, low_threshold, high_threshold)
dupa_end = cv2.Canny(dupaa,low_threshold,high_threshold)

# plt.imshow(dupa_end,cmap='gray')
# plt.show()

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 15  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 100  # minimum number of pixels making up a line
max_line_gap = 10  # maximum gap in pixels between connectable line segments
line_image = np.copy(dupa_end) * 0  # creating a blank to draw lines on


# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(dupa_end, rho, theta, threshold, np.array([]),
                    min_line_length, max_line_gap)
if lines is not None:
    for i in range(0,len(lines)):
        l = lines[i][0]
        cv2.line(pierwotny,(l[0], l[1]), (l[2], l[3]), (255,0,0), 3, cv2.LINE_AA)

# for line in lines:
#     for x1,y1,x2,y2 in line:
#         cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),5)
# huiiijj = cv2.cvtColor(dupaa, cv2.COLOR_GRAY2BGR)
# end = cv2.add(pierwotny, huiiijjj)
plt.imshow(pierwotny)
plt.show()
