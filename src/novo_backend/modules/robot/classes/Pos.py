class Pos:
	def __init__(self, x: int, y: int, z: int, r: int):
		self.x = x
		self.y = y
		self.z = z
		self.r = r

	def offset_z(self, offset: int):
		return Pos(self.x, self.y, self.z + offset, self.r)