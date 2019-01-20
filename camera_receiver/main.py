import json

import numpy as np
import cv2
from scipy.spatial import distance
import time, threading
import urllib.request


from extract_car import extract_car
from extract_rectangle import extract_rectangle
from extract_parking import extract_parking

NB_PARKING_SPOTS = 10
ACCUMULATION = 10
MAX_DIST = 30


def find_parking(show_output):
    cap = cv2.VideoCapture("http://10.200.9.248:8080/video/mjpeg")

    accumulator_free = []
    accumulator_occupied = []

    global available_parking

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
                if dist < MAX_DIST:
                    acc_free[1] += 2
                    pos_found = True
                    break
            if not pos_found:
                accumulator_free.append([pos_free, 1, False, 'f'])
        i = 0
        while i < len(accumulator_free):
            if accumulator_free[i][1] >= ACCUMULATION:
                accumulator_free[i][1] = ACCUMULATION
                accumulator_free[i][2] = True
            elif accumulator_free[i][1] == 0:
                accumulator_free.pop(i)
                continue
            i += 1
        total_spots = 0
        for acc_free in accumulator_free:
            if acc_free[2]:
                cv2.circle(frame_copy, acc_free[0], 30, (0, 200, 0), -1)
                total_spots += 1


        #######

        for acc_occ in accumulator_occupied:
            acc_occ[1] -= 1
        for pos_occ in positions_occupied:
            skip = False
            for acc_free in accumulator_free:
                if distance.euclidean(pos_occ, acc_free[0]) < MAX_DIST * 1.5:
                    skip = True
            pos_found = False
            for acc_occ in accumulator_occupied:
                dist = distance.euclidean(pos_occ, acc_occ[0])
                if dist < MAX_DIST:
                    if skip:
                        acc_occ[1] = 0
                    else:
                        acc_occ[1] += 2
                    pos_found = True
                    break
            if not pos_found:
                accumulator_occupied.append([pos_occ, 1, False, 'o'])
        i = 0
        while i < len(accumulator_occupied):
            if accumulator_occupied[i][1] >= ACCUMULATION:
                accumulator_occupied[i][1] = ACCUMULATION
                accumulator_occupied[i][2] = True
            elif accumulator_occupied[i][1] == 0:
                accumulator_occupied.pop(i)
                continue
            i += 1
        for acc_free in accumulator_occupied:
            if acc_free[2]:
                cv2.circle(frame_copy, acc_free[0], 30, (0, 0, 200), -1)
                total_spots += 1
        if show_output:
            cv2.imshow('frame', frame_copy)

        # if total_spots == NB_PARKING_SPOTS:
        merged_list = accumulator_free + accumulator_occupied
        spots = sorted(merged_list, key=lambda acc: acc[0][0])
        list_up = []
        list_down = []
        for item in spots:
            if item[0][1] < height / 2:
                list_up.append(item)
            else:
                list_down.append(item)
        # spots = sorted(spots, key=lambda acc: acc[0][1])
        available_parking = []
        for s in range(len(list_up)):
            if list_up[s][-1] == 'f':
                available_parking.append(s)

        for s in range(len(list_down)):
            if list_down[s][-1] == 'f':
                available_parking.append(s + 5)
            # print(available_parking)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if show_output:
        cv2.destroyAllWindows()


def send_to_server():
    global available_parking
    print(available_parking)
    try:
        url = "http://35.203.84.127:3000/"
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        body = {'parkings': available_parking}
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)
    except Exception:
        pass
    threading.Timer(1.0, send_to_server).start()


if __name__ == '__main__':
    global available_parking
    available_parking = []
    send_to_server()
    try_again = True
    while try_again:
        try:
            try_again = False
            find_parking(True)
        except AttributeError:
            print("Server not found, trying again ...")
            try_again = True
