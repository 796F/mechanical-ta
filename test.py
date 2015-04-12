import boto
import numpy
import matplotlib
import cv2

from pudb import set_trace; # set_trace()

print cv2.__version__

img = cv2.imread('images/dino.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()