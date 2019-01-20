import imutils
import numpy as np
import cv2
from random import randint

from extract_rectangle import extract_rectangle


def extract_car(img, result):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 50, 255, 1)

    # cv2.imshow('Resultat', thresh)
    # cv2.waitKey(0)

    kernel = np.ones((3, 3), np.uint8)
    # res = cv2.erode(thresh,kernel,iterations = 1)
    # kernel = np.ones((11, 11), np.uint8)
    res = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((3, 3), np.uint8)
    res = cv2.erode(res,kernel,iterations = 3)
    res = cv2.dilate(res,kernel,iterations = 3)



    # cv2.imshow('Resultat', res)
    # cv2.waitKey(0)
    contours, h = cv2.findContours(res, 1, 2)

    areas = [cv2.contourArea(c) for c in contours]
    # print(areas)
    median = 0
    if len(areas) != 0:
        median = np.median(areas)
    mini = 2000
    maxi = 11000
    positions = []
    for index in range(len(contours)):
        if mini > areas[index] or maxi < areas[index]:
            continue
        cnt = contours[index]
        cv2.drawContours(result, [cnt], 0, (0, 0, 200), -1)
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        positions.append((cX, cY))

    return result, positions


if __name__ == "__main__":
    name = "Data/parking_occupied.jpg"

    img = cv2.imread(name)

    res = extract_car(img)

    # res = extract_rectangle(img, res)

    cv2.imshow('Resultat', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
