import numpy as np
import cv2
from scipy.spatial import distance

from extract_car import extract_car
from extract_rectangle import extract_rectangle
from extract_parking import extract_parking

cap = cv2.VideoCapture("http://10.200.21.209:8080/video/mjpeg")

accumulator_free = []
accumulator_occupied = []

while(True):
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    frame = frame[0:height, 0:2*(width//3)]
    frame_copy = frame.copy()
    res = extract_parking(frame)
    res, positions_free = extract_rectangle(frame, res)
    res, positions_occupied = extract_car(frame, res)
    for acc_free in accumulator_free:
        acc_free[1] -= 1
    for pos_free in positions_free:
        pos_found = False
        for acc_free in accumulator_free:
            dist = distance.euclidean(pos_free, acc_free[0])
            if dist < 10:
                acc_free[1] += 2
                pos_found = True
                break
        if not pos_found:
            accumulator_free.append([pos_free, 1, False])
    i = 0
    while i < len(accumulator_free):
        if accumulator_free[i][1] >= 5:
            accumulator_free[i][1] = 5
            accumulator_free[i][2] = True
        elif accumulator_free[i][1] == 0:
            accumulator_free.pop(i)
            continue
        i += 1
    for acc_free in accumulator_free:
        if acc_free[2]:
            cv2.circle(frame_copy, acc_free[0], 30, (0, 200, 0), -1)


    #######

    for acc_free in accumulator_occupied:
        acc_free[1] -= 1
    for pos_free in positions_occupied:
        pos_found = False
        for acc_free in accumulator_occupied:
            dist = distance.euclidean(pos_free, acc_free[0])
            if dist < 10:
                acc_free[1] += 2
                pos_found = True
                break
        if not pos_found:
            accumulator_occupied.append([pos_free, 1, False])
    i = 0
    while i < len(accumulator_occupied):
        if accumulator_occupied[i][1] >= 5:
            accumulator_occupied[i][1] = 5
            accumulator_occupied[i][2] = True
        elif accumulator_occupied[i][1] == 0:
            accumulator_occupied.pop(i)
            continue
        i += 1
    for acc_free in accumulator_occupied:
        if acc_free[2]:
            cv2.circle(frame_copy, acc_free[0], 30, (0, 0, 200), -1)

    cv2.imshow('frame', frame_copy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()