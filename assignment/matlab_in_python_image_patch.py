import PIL
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Random_angle import GetAngle

def imagepatchgenerate(ih, il, angle, location):
    imagearray = 255 * np.random.uniform(0, 1, (401, 401))
    imagearray[:, 201:401] = ih
    imagearray[:, 0:200] = il
    imagearray[:, 200] = (il+ih)/2
    imagetemp = imagearray
    standard_minus = np.std(imagetemp)
    print standard_minus
    d = GetAngle()
    gaussianfilter=d.gaussian_2d((3, 3), standard_minus)
    print gaussianfilter
    b = plt.imshow(imagetemp)
    plt.show(b)
imagepatchgenerate(3, 1, math.pi/2, 2)
