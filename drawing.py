from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

from polygon import Polygon

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=None, help="path to the input image")
ap.add_argument("-s", "--sides", type=int, default=4, help="number of sides to draw")
ap.add_argument("-c", "--color", type=str, default="blue", help="color for the shape")
args = vars(ap.parse_args())

# image = cv2.imread('/home/pacrob/Pictures/reference/Lena/DSC08204.JPG')


print(args)

if args["image"]:

    image = cv2.imread(args["image"])
else:
    image = np.zeros((300, 300, 3), dtype="uint8")


bob = Polygon(5, "green")
print(bob)

cv2.imshow("Image", image)
cv2.waitKey(0)
