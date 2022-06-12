from matplotlib import pyplot as plt
import argparse
import cv2 as cv
import numpy as np
import math
from random import randint

from polygon import Polygon

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=None, help="path to the input image")
ap.add_argument("-n", "--num", type=int, default=1, help="how many polygons to draw")
args = vars(ap.parse_args())

WIDTH = 1000
HEIGHT = 1000

if args["image"]:

    img = cv.imread(args["image"])
    scale_percent = 30 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
else:
    img = np.zeros((HEIGHT, WIDTH, 3), dtype="uint8")
    
    
def draw_polygon(canvas, shape, x, y):
    pts = shape.generate_vertices(x, y)
    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(canvas,[pts],True,shape.color)
    

# https://math.stackexchange.com/questions/35438/maths-find-vertices-when-1-vertex-and-center-point-is-given-in-polygon

for x in range(args['num']):
    radius = randint(50, 150)
    num_sides = randint(3, 27)
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    r = randint(0, 255) 
    g = randint(0, 255) 
    b = randint(0, 255) 

    bob = Polygon(radius, num_sides, (b, g, r))
    draw_polygon(img, bob, y, x)



# bob = Polygon(250, 4)
# pts = bob.generate_vertices(500, 500)
# draw_polygon(img, bob, 500, 500)
# bob = Polygon(100, 5)
# print(bob)

cv.imshow("Image", img)
cv.waitKey(0)
