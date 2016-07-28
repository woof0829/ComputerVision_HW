# edge detection related
import math
import numpy as np
import matplotlib.pyplot as plt
from mlab.releases import latest_release as mtl


class DetectionRelated(object):
    @staticmethod
    def judgepixel(matrix=np.zeros((15, 15)), value1=0, value2=0):
        component_x = [[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]]
        component_y = [[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]]
        gradx = np.abs(mtl.filter2(component_x, matrix, 'same'))
        grady = np.abs(mtl.filter2(component_y, matrix, 'same'))
        grad_temp = np.convolve(gradx, grady)
        grad = grad_temp[value1, value2]
        return [grad, gradx, grady, grad_temp]
        pass

    @staticmethod
    def gradvalue(matrix0=np.zeros((15, 15)), matrix1=np.zeros((15, 15)), value1=0, value2=0, value3=0, value4=0):
        component_x = [[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]]
        component_y = [[-1, -2, -1],
                       [0, 0, 0],
                       [1, 2, 1]]
        gradx = np.abs(mtl.filter2(component_x), matrix0, 'same')
        grady = np.abs(mtl.filter2(component_y), matrix0, 'same')
        grad_0 = np.convolve(gradx, grady)
        grad_1 = matrix1[value1, value2]
        grad_2 = matrix1[value3, value4]
        if matrix1 > grad_1 and matrix1 > grad_2:
            grad = grad_0
        else:
            grad = 0
        return grad
        pass

    @staticmethod
    def processofNMS(matrix=np.zeros((15, 15)), angle=math.pi/2, value0=0, value1=0, value2=0, value3=0):
        """
        Non-maximum suppression process

        """
        if math.pi/8 <= angle < 3*math.pi/8 or 9*math.pi/8 <= angle < 11*math.pi/8:
            matrix[7, 7] = value0
        elif (3*math.pi/8 <= angle < 5*math.pi/8) or (11*math.pi/8 <= angle < 13*math.pi/8):
            matrix[7, 7] = value1
        elif (5*math.pi/8 <= angle < 7*math.pi/8) or (13*math.pi/8 <= angle < 15*math.pi/8):
            matrix[7, 7] = value2
        elif (7*math.pi/8 <= angle < 9*math.pi/8) or (-math.pi/8 <= angle < math.pi/8):
            matrix[7, 7] = value3
            pass
        return matrix[7, 7]

    @staticmethod
    def cannythre(threlow=0, value=0, image=np.zeros((15, 15))):
        threup = 2*threlow
        if value >= threup:
            image[7, 7] = 255
        elif value <= threlow:
            image[7, 7] = 0
        pass

        for i in range(6, 9):
            for j in range(6, 9):
                if not(i == 7 and j == 7):
                    grad = value
                    if grad >= threup:
                        value1 += 1
        if value1 > 0:
            image = 255
        else:
            image = 0
        return image
        pass

if __name__ == '__main__':
    a = DetectionRelated()
    b = DetectionRelated.judgepixel()
