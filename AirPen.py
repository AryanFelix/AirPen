import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,150)

# Stylus Color Codes
colors = [[0,16,84,255,187,255],
          [154,179,90,230,146,255],
          [73,91,130,255,141,255],
          [25,38,82,255,87,255],
          [99,107,166,255,143,255]
          ]

colorNames = {0 : "Orange", 1:  "Pink", 2 : "Green", 3 : "Yellow", 4 : "Blue"}

# Colors for Drawing
colorValues = [[0,45,255], [243,0,255], [0,255,39], [0,220,255], [255,165,0]]
points = []

def findColor(img, colors, colorValues, colorNames):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    val = 0
    newpoints = []
    for i, color in enumerate(colors):
        lower = np.array(color[::2])
        upper = np.array(color[1::2])
        mask = cv2.inRange(imgHSV,lower,upper)
        a, b = getContours(mask)
        cv2.circle(imgResult, (a,b), 10, colorValues[val], cv2.FILLED)
        if a!=0 and b!=0:
            newpoints.append([a,b,val])
        val = val + 1
        #cv2.imshow(colorNames[i], mask)
    return newpoints

def getContours(img):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
    return (x+w//2), y

def draw(points, colorValues):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 10, colorValues[point[2]], cv2.FILLED)

while True:
    success, temp = cap.read()
    imgResult = temp.copy()
    newpoints = findColor(temp, colors, colorValues, colorNames)
    if len(newpoints)!=0:
        for newp in newpoints:
            points.append(newp)
    if len(points)!=0:
        draw(points, colorValues)
    final = cv2.flip(imgResult,1)
    cv2.imshow("Video", final)
    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break