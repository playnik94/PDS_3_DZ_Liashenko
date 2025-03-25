from __future__ import print_function
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser(description='path of the images')
ap.add_argument("image",type=str, help="path to input image")
args = vars(ap.parse_args())
photo = cv2.imread(args["image"])
photo = cv2.resize(photo, (700, 900))

def adjust_gamma(image, gamma=1.0):
    inv_gamma = 1.0 / gamma
    table = np.array([(( i / 255) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

for gamma in np.arange(0.0, 3.5, 0.5):
    if gamma == 1:
        continue

    gamma = gamma if gamma > 0 else 0.1
    adjusted = adjust_gamma(photo, gamma=gamma)
    cv2.putText(adjusted, f"g={gamma}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("image", np.hstack([photo, adjusted]))
    cv2.waitKey(0)

