import PIL
import math
import numpy as np
import matplotlib.pyplot as plt
from Random_angle import GetAngle
from mlab.releases import latest_release as mtl



def imagepatchgenerate(ih, il, angle, location):
    imagearray = 255 * np.random.uniform(0, 1, (11, 11))
    imagearray[:, 6:11] = il
    imagearray[:, 0:5] = ih
    imagearray[:, 5] = (il+ih)/2
    imagetemp = imagearray.flatten(1)
    imagetemp.shape = (121, 1)
    standard_minus = np.std(imagetemp, ddof=1)
    d = GetAngle()
    gaussianfilter=d.gaussian_2d((3, 3), standard_minus)

    e = plt.imshow(gaussianfilter[:,:], cmap=plt.cm.gray)
    # mtl.imshow(gaussianfilter)
    plt.show(e)
    # print gaussianfilter

if __name__ == '__main__':
    imagepatchgenerate(3, 1, 2*math.pi, 2)
