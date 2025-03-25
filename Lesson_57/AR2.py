import argparse
import cv2
import numpy as np
import imutils
from imutils import paths

ap = argparse.ArgumentParser()
ap.add_argument("-i","--images", type=str, required=True, help="path to input directory of images to stitch")
ap.add_argument("-o","--output", type=str, required=True, help="path to the output image")
args = vars(ap.parse_args())

print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)
print("[INFO] stitching images...")
stitcher = cv2.Stitcher.create() if imutils.is_cv4() else cv2.Stitcher.create()
(status, stitched) = stitcher.stitch(images=images)

if status == 0:
    cv2.imwrite("stitched", stitched)
    cv2.imshow('res', stitched)
    cv2.waitKey(0)
else:
    print(f"[INFO] image failed... {status}")
