import math
import numpy as np
import matplotlib.pyplot as plt
from ImageRelated import ImageRelated
from mlab.releases import latest_release as mtl

Length, Width, number = 525, 525, 15
size = Length/number
angle = float((math.pi/2)*np.random.rand(1, 1))
displacement = float(1.5*size*((math.sin(angle))+math.cos(angle))*np.random.rand(1, 1))
image = ImageRelated()
image_matrix = image.empty_matrix(Length)
mean_image = image.empty_matrix(number)
filter_image = image.empty_matrix(number)
noise_image = image.empty_matrix(number)
_image_ = image.empty_matrix(number)
image_small = image.empty_matrix(size)
# return a list with two number descending sorted
pixel_value = image.exchange_value()
High = np.round(255*pixel_value[0])
Low = np.round(255*pixel_value[1])
image_matrix = image.set_value(length=Length, width=Width, angle=angle, location=displacement, H=High, L=Low)
mean_image = image.mean_value(image=image_matrix, meanimage=mean_image, number=number, size=size)





