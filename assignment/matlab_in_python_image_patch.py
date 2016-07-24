import math
import numpy as np
import matplotlib.pyplot as plt
from Random_angle import GetAngle
from mlab.releases import latest_release as mtl



def imagepatchgenerate(ih, il, angle, location):
    imagearray = 255 * np.random.uniform(0, 1, (201, 201))
    imagearray[:, 101:201] = il
    imagearray[:, 0:100] = ih
    imagearray[:, 100] = (il+ih)/2
    imagetemp = imagearray.flatten(1)
    imagetemp.shape = (201*201, 1)
    standard_minus = np.std(imagetemp, ddof=1)
    d = GetAngle()
    gaussianfilter = d.gaussian_2d((3, 3), standard_minus)
    image = mtl.imfilter(imagearray, gaussianfilter, 'replicate')
    rotatedimage = mtl.imrotate(image, angle, 'bicubic', 'crop')
    localx = location*math.cos(angle)
    localy = location*math.sin(angle)
    translatedimage = mtl.imtranslate(rotatedimage, [[localx, localy]])
    croppedimage = translatedimage[93:108, 93:108]
    gaussiannoise = np.random.normal(loc=0.0, scale=2.0, size=(15, 15))
    image = croppedimage+gaussiannoise
    # e = plt.imshow(translatedimage, cmap=plt.cm.gray)
    # plt.show(e)
if __name__ == '__main__':
    imagepatchgenerate(3, 1, math.pi/3, 3)
