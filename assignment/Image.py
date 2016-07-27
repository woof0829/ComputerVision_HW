import math
import numpy as np
import matplotlib.pyplot as plt
from ImageRelated import ImageRelated
from mlab.releases import latest_release as mtl


class Image(object):
    @staticmethod
    def imagegenerate(Length=525, Width=525, number=15):
        size = Length / number
        angle = float((math.pi / 2) * np.random.rand(1, 1))
        displacement = float(1.5 * size * ((math.sin(angle)) + math.cos(angle)) * np.random.rand(1, 1))
        image = ImageRelated()
        mean_image = image.empty_matrix(number)
        pixel_value = image.exchange_value()
        High = np.round(255 * pixel_value[0])
        Low = np.round(255 * pixel_value[1])
        image_matrix = image.set_value(length=Length, width=Width, angle=angle, location=displacement, H=High, L=Low)
        mean_image = image.mean_value(image=image_matrix, meanimage=mean_image, number=number, size=size)
        gaussian_filter = image.gaussian_2d(shape=(3, 3), sigma=1)
        image_filter = mtl.imfilter(mean_image, gaussian_filter, 'replicate')
        add_noise = np.random.normal(loc=0.0, scale=2.0, size=(number, number))
        image_noise = image_filter + add_noise
        imagepatch = np.uint8(image_noise)
        tem = plt.imshow(imagepatch, cmap="gray", interpolation='nearest')
        plt.show(tem)
        pass




if __name__ == '__main__':
    a = Image()
    a.imagegenerate(Length=525, Width=525, number=15)
