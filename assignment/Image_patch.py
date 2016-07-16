from Random_angle import GetAngle
import math
import numpy as np
import PIL
d = GetAngle()
print(math.sin(d.get_angle()))
print(d.gaussian_2d((5, 5), 1))

