# Image patch generate
import math
import numpy as np
import matplotlib as mpl


class GetAngle(object):
    """Generate a random angle between 0 to pi/2"""

    # def __init__(self, data):
    # self.data=data
    @staticmethod
    def get_angle():
        angle = math.pi / 2 * np.random.random((1,))
        return float(angle)
        pass

    def function(self):
        pass

