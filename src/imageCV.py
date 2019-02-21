import cv2
import numpy as np


"""
This is Ashwin's side of the code
"""
timg = cv2.imread("<insert file path>", 10)
final = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
img = timg

# Determine average deviation of rgb values in each pixel
deviation = 0
for x in range(len(img)):
    for y in range(len(img[0])):
        deviation += (abs(int(img[x, y, 0]) - int(img[x, y, 1])) + (abs(int(img[x, y, 1]) - int(img[x, y, 2]))) / 2)
deviation = deviation / (len(img) * len(img[0]))
print deviation

# Use deviation to turn only background into black
for x in range(len(img)):
    for y in range(len(img[0])):
        if ((abs(int(img[x, y, 0]) - int(img[x, y, 1])) < deviation) & (abs(int(img[x, y, 1]) - int(img[x, y, 2])) < deviation)):
            img[x, y, 0] = 0
            img[x, y, 1] = 0
            img[x, y, 2] = 0

#grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blur = cv2.blur(grayscale, (5, 5))
#ret, thresh = cv2.threshold(grayscale, 160, 255, cv2.THRESH_BINARY)

# Convert from rgb to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create mask separating background from object
lower = np.array([0, 10, 50])
upper = np.array([255, 250, 250])
mask = cv2.inRange(hsv, lower, upper)

# Find contours in masked image
img_cnt, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img_cnt, contours, -1, (0, 0, 0), 10)

# Draw only the largest rectangle boundary (which will be the image)
rectangle = []
max = 0
for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt)
    if w * h > max:
        max = w * h
        rectangle = [x, y, w, h]
cv2.rectangle(final, (rectangle[0], rectangle[1]), (rectangle[0] + rectangle[2], rectangle[1] + rectangle[3]), (200, 200, 100), 2)

# Crop the image upon the rectangle
newimg = final[(rectangle[1]):(rectangle[1] + rectangle[3]), (rectangle[0]):(rectangle[0] + rectangle[2])]

cv2.imshow("Hello", newimg)
cv2.waitKey(0)


"""
This is Eric's side of the code
"""
# img = cv2.imread("/Users/erichu/Downloads/8d4bb900b3026aac0024badd9ee8d28e--painted-gourds-french-revolution.jpg", 1)
