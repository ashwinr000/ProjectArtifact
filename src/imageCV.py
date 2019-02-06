import cv2
import numpy as np

img = cv2.imread("/Users/ashwinr/Downloads/testartifact.jpg", 100)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(grayscale, 80, 200, cv2.THRESH_BINARY)

cv2.imshow("Hello", thresh)
cv2.waitKey(0)