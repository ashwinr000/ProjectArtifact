import csv
import cv2

# Open csv file
csvFile = open('/Users/ashwinr/Downloads/ProjectArtifact/imageData.csv')

# Create writer for csv file
csvFileW = open('/Users/ashwinr/Downloads/ProjectArtifact/imageData.csv', "w")
writer = csv.writer(csvFileW, delimiter=',')

# Write row and column size in each row of csv file
for i in range(17):
    filePath = "/Users/ashwinr/Downloads/test{}.jpg".format(i + 1)
    # print(filePath)
    img = cv2.imread(filePath, 10)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for x in range(len(img)):
        writer.writerow([img[x]])