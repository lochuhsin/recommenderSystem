from recommenderSystem.service import parse_file
from datetime import datetime


class tournament_prematch(object):
	def __init__(self):
		self.daily_threshold = 2
		self.daily_sec = 86400
		self.scale_factor = 0.6  # less than 1 but larger than 0, smooth out score nears today

	def predict(self, x: 'ndarray') -> list:
		if x.shape[1] != 2:
			raise ValueError('feature dimension should be (n, 2)')

		x = x.T  # convert to (2, n) to form numpy vectorize computation
		sec = x[0]
		weight = x[1]

		_y = ((self.daily_sec*self.daily_threshold/sec)*weight)**self.scale_factor
		return _y


class tournament_live(object):
	def __init__(self):
		self.init_aging = 2  # aging factor is 2
		self.drop_rate = 0.8  # rate of decay

	def predict(self, x: 'ndarray')-> list:
		if x.shape[1] != 2:
			raise ValueError('feature dimension should be (n, 2)')

		x = x.T
		sec = x[0]
		weight = x[1]

		_y = weight/((sec+self.init_aging)**self.drop_rate)
		return list(_y)
