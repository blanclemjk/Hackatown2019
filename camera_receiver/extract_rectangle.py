from random import randint

import numpy as np
import cv2


def extract_rectangle(img, res):
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # ret, thresh = cv2.threshold(gray, 127, 255, 1)
    res = cv2.bitwise_not(res)
    # cv2.imshow('Resultat', res)
    # cv2.waitKey(0)
    contours, h = cv2.findContours(res, 1, 2)

    areas = [cv2.contourArea(c) for c in contours]
    median = 0
    if len(areas) != 0:
        median = np.median(areas)
    mini = 7000
    maxi = 14000
    positions = []
    for index in range(len(contours)):
        if mini > areas[index] or maxi < areas[index]:
            continue
        cnt = contours[index]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx)==4:
            cv2.drawContours(img, [cnt], 0, (0, 200, 0), -1)
            M = cv2.moments(cnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            positions.append((cX, cY))

    return img, positions


if __name__ == "__main__":
    name = "Data/test.jpg"

    img = cv2.imread(name)

    res = extract_rectangle(img)

    cv2.imshow('Resultat', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
