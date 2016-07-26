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
    def empty_matrix(x=0):
        """
        generate empty n*n matrix

        """
        matrix = np.zeros((x, x))
        return matrix

    @staticmethod
    def exchange_value():
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
    def set_value(length=0, width=0, angle=math.pi, location=0, H=0, L=0):
        """
        set value for image matrix 

        """
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
    def mean_value(image=np.zeros((5, 5)), number=4):
        """
        calculate the mean value of the image patch

        """
        for i in range(number):
            for j in range(number):
                temp_image = image[number*(j-1)+1:number*j, number*(i-1)+1:number*i]
                temp_meanvalue = temp_image.flatten(1)
                temp_meanvalue.shape = (number*number, 1)
                mean_value = np.mean(temp_meanvalue)
                meanvalue = np.round(mean_value)
                image[j, i] = meanvalue
                pass
            pass
        pass
        return image

    @staticmethod
    def judge_pixel(thres=0, pixel=0, image=[10, 10], n=0):
        """
        set value for central pixel

        """
        if pixel > thres:
            image[n/2, n/2] = 255
        else:
            image[n/2, n/2] = 0
            pass
        pass

if __name__ == '__main__':
    a = ImageRelated()
