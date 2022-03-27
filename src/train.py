import os
import os.path
import cv2
import pickle
import numpy as np
from imutils import paths
import face_recognition
from face_recognition.cli import image_files_in_folder
from sklearn import neighbors
from PIL import Image, ImageDraw

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def train(_dir, model_file=None, n_neighbors=None, knn_alg='ball_tree', verbose=False):
    img_dirs = list(paths.list_images('dataset'))

    known_encodings = []
    known_users = []

    for (image, img_dir) in enumerate(img_dirs):
        user = img_dir.split(os.path.sep)[-2]

        image = cv2.imread(img_dir)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        face_locs = face_recognition.face_locations(rgb)

        encodings = face_recognition.face_encodings(rgb, face_locs)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_users.append(user)

    data = {"encodings": known_encodings, "users": known_users}

    knn_clf = neighbors.KNeighborsClassifier(
        n_neighbors=n_neighbors, algorithm=knn_alg, weights='distance')

    knn_clf.fit(known_encodings, known_users)

    if model_file is not None:

        with open(model_file, 'wb') as model:
            pickle.dump(knn_clf, model)

    return knn_clf


if __name__ == "__main__":
    print("Training KNN classifier...")

    classifier = train(
        "dataset", model_file="knn_model.clf", n_neighbors=2)

    print("Training complete")
