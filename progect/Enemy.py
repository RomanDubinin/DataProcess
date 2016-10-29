class Enemy:
	def __init__(self, position):
		self.position = position

	def move_by(self, vector):
		self.position += vector