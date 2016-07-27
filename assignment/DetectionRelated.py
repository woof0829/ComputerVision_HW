# edge detection related
import math
import numpy as np
import matplotlib.pyplot as plt
from mlab.releases import latest_release as mtl


class DetectionRelated(object):
    @staticmethod
    def centralpixel(matrix=np.zeros((15, 15)), value1=0, value2=0):
        component_x = [[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]]
        component_y = [[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]]
        gradx = np.abs(mtl.filter2(component_x, matrix, 'same'))
        grady = np.abs(mtl.filter2(component_y, matrix, 'same'))
        grad = np.convolve(gradx, grady)
        return grad
        pass


if __name__ == '__main__':
    a = DetectionRelated()
    b = DetectionRelated.centralpixel()
    print b
