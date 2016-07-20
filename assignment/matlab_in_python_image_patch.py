import cv2
import PIL
import math
import numpy as np
import scipy.ndimage, scipy.misc
import matplotlib.pyplot as plt
from Random_angle import GetAngle

def imagepatchgenerate(ih, il, angle, location):
    imagearray = 255 * np.random.uniform(0, 1, (401, 401))
    imagearray[:, 201:401] = ih
    imagearray[:, 0:200] = il
    imagearray[:, 200] = (il+ih)/2
    imagetemp = imagearray
    standard_minus = np.std(imagetemp)
    d = GetAngle()
    gaussianfilter=d.gaussian_2d((3, 3), standard_minus)
    c = scipy.ndimage.filters.correlate(gaussianfilter, imagetemp)
    b = scipy.misc.imrotate(gaussianfilter, angle, interp="bicubic")
    e = plt.imshow(imagetemp)
    plt.show(e)
imagepatchgenerate(100, 1, 2*math.pi, 2)
