import cv2
import numpy as np

"""""
line of code for Ashwin's end, uncomment when coding"
* Received on my end *
"""""
'''
img = cv2.imread("/Users/ashwinr/Downloads/testartifact.jpg", 100)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(grayscale, 80, 200, cv2.THRESH_BINARY)
blur = cv2.blur(img, (10, 10))
cv2.imshow("Hello", blur)
cv2.waitKey(0)
'''

"""""
line of code for Eric's end, uncomment when coding"

"""""
# img = cv2.imread("/Users/erichu/Downloads/8d4bb900b3026aac0024badd9ee8d28e--painted-gourds-french-revolution.jpg", 100)

x = 0