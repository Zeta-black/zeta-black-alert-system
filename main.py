# main.py

import cv2
import numpy as np
import os

def analyze_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()
    brightness = np.mean(gray)

    if blur_score < 200:
        return "BLURRY"
    elif brightness < 50:
        return "LOW LIGHT"
    else:
        return "CLEAR"

def process_images(folder_path):
    images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg','.png'))]

    for img_name in images:
        path = os.path.join(folder_path, img_name)
        img = cv2.imread(path)

        result = analyze_frame(img)
        print(f"{img_name}: {result}")

if __name__ == "__main__":
    process_images("dataset/")