import os
import cv2
import dlib
import h5py
import pickle
import imutils
import numpy as np
import argparse as ap
from imutils import face_utils

parser = ap.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the video file")
args = vars(parser.parse_args())

number = 0
frame_count = 0

detector = dlib.get_frontal_face_detector()

user_name = input("Enter user's name: ")

folder_name = "dataset/" + user_name

if os.path.exists(folder_name):
    print("Folder exists")

else:
    os.mkdir(folder_name)

if not args.get("file", False):
    capture = cv2.VideoCapture(0)

else:
    capture = cv2.VideoCapture(args["file"])

while True:

    if frame_count % 5 == 0:

        print("keyframe")

        (grabbed, image) = capture.read()

        if args.get("video") and not grabbed:
            break

        image = imutils.resize(image, width=500)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 1)

        for (i, rect) in enumerate(rects):
            (x, y, w, h) = face_utils.rect_to_bb(rect)

            cro = image[y: y + h, x: x + w]

            out_image = cv2.resize(cro, (108, 108))

            fram = os.path.join(folder_name+"/", str(number) + "." + "jpg")

            number += 1

            cv2.imwrite(fram, out_image)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        frame_count += 1

    else:
        frame_count += 1
        print("redundant frame")

    if number > 51:
        break

    cv2.imshow("output", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
