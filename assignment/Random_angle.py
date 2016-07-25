# Image patch generate
import math
import numpy as np
import matplotlib.pyplot as mpl


class ImageRelated(object):
    @staticmethod
    def get_angle():
        """
        Generate a random angle between 0 to pi/2

        """
        angle = math.pi / 2 * np.random.random((1,))
        return float(angle)
        pass

    @staticmethod
    def gaussian_2d(shape=(3, 3), sigma=0.5):
        """
        a method of 2D gaussian mask

        """
        m, n = [(ss - 1.) / 2. for ss in shape]
        y, x = np.ogrid[-m:m + 1, -n:n + 1]
        h = np.exp(-(x * x + y * y) / (2. * sigma * sigma))
        h[h < np.finfo(h.dtype).eps * h.max()] = 0
        sumh = h.sum()
        if sumh != 0:
            h /= sumh
        return h

    @staticmethod
    def emptymatrix(x):
        """
        generate empty n*n matrix

        """
        matrix = np.zeros((x, x))
        return matrix

    @staticmethod
    def exchangevalue():
        """
        determine the value for High and Low

        """
        random_number = np.random.rand(1, 2)
        High = random_number[0, 0]
        Low = random_number[0, 1]
        if High < Low:
            temp = High
            High = Low
            Low = temp
            pass
        return [High, Low]

    @staticmethod
    def setvalue(length=0, width=0, angle=math.pi, location=0, H=0, L=0):
        matrix = np.zeros((length, width))
        for i in range(length):
            for j in range(width):
                judgecondition = math.cos(angle) * (j - ((width + 1) / 2)) + math.sin(angle) * (
                    i - ((length + 1) / 2)) - location
                if judgecondition > 0:
                    matrix[j, i] = H
                else:
                    matrix[j, i] = L

        return matrix
    @staticmethod
    def meanvalue(number=0):
        for i in range(number):
            for j in range(number):
                
                pass
            pass

        pass
    

if __name__ == '__main__':
    a = ImageRelated()

