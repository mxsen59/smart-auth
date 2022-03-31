import os
import cv2
import h5py
import dlib
import pickle
import imutils
import numpy as np
import argparse as ap
import face_recognition
from imutils import face_utils
from PIL import Image, ImageDraw

parser = ap.ArgumentParser()
parser.add_argument("-f", "--file", help="path to the video file")
args = vars(parser.parse_args())

with open("knn_model.clf", "rb") as model:
    knn_clf = pickle.load(model)

if not args.get("file", False):
    capture = cv2.VideoCapture(0)

else:
    cv2.VideoCapture(args["file"])

while True:
    (grabbed, image) = capture.read()

    if args.get("file") and not grabbed:
        break

    img = image[:, :, ::-1]

    face_locs = face_recognition.face_locations(img)

    if len(face_locs) != 0:
        face_encs = face_recognition.face_encodings(
            img, known_face_locations=face_locs)

        closest_distances = knn_clf.kneighbors(face_encs, n_neighbors=1)

        is_matches = [closest_distances[0][index][0] <=
                      0.4 for index in range(len(face_locs))]

        predictions = [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(
            knn_clf.predict(face_encs), face_locs, is_matches)]

        for user, (top, right, bottom, left) in predictions:

            if user not in "unknown":
                os.popen(
                    'xscreensaver-command -deactivate')

            cv2.rectangle(image, (left, bottom),
                          (right, top), (0, 255, 0), 2)

            cv2.putText(image, "{}".format(user), (left-10, top-10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

    else:
        os.popen('xscreensaver-command -activate')

    # cv2.imshow("output", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()

cv2.destroyAllWindows()
