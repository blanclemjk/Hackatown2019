import imutils
import numpy as np
import cv2
from random import randint

from extract_car import extract_car
from extract_rectangle import extract_rectangle


def extract_parking(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, 1)

    # cv2.imshow('Resultat', thresh)
    # cv2.waitKey(0)

    kernel = np.ones((3, 3), np.uint8)
    # res = cv2.erode(thresh,kernel,iterations = 1)
    # kernel = np.ones((11, 11), np.uint8)
    res = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_DILATE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_DILATE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_DILATE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_DILATE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_DILATE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_DILATE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_ERODE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_ERODE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_ERODE, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_ERODE, kernel)


    # cv2.imshow('Resultat', res)
    # cv2.waitKey(0)
    # sobelx = cv2.Sobel(res, cv2.CV_8U, 1, 0, ksize=5)
    #
    # cv2.imshow('Resultat', sobelx)
    # cv2.waitKey(0)
    #
    # kernel = np.ones((7, 3), np.uint8)
    # res = cv2.morphologyEx(sobelx, cv2.MORPH_OPEN, kernel)
    #
    # cv2.imshow('Resultat', res)
    # cv2.waitKey(0)
    contours, hierarchy = cv2.findContours(res, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(res, (x, y), (x + w, y + h), (255,255,255), 20)

        # cv2.drawContours(img, [cnt], 0, (randint(0,255), randint(0,255), randint(0,255)), -1)

    return res


if __name__ == "__main__":
    name = "Data/parking_occupied.jpg"

    img = cv2.imread(name)

    res = extract_parking(img)

    res = extract_rectangle(img, res)
    res = extract_car(img, res)

    cv2.imshow('Resultat', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
