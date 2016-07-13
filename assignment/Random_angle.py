# Image patch generate
import math
import numpy as np

class Get_angle(object):
	"""Generate a random angle between 0 to pi/2"""
	#def __init__(self, data):
		#self.data=data
	def get_angle(self):
		angle = math.pi/2 * np.random.random((1,))
		return float(angle)
		pass
		
