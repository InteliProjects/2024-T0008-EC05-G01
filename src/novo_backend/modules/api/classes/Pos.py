import pydantic

class Pos(pydantic.BaseModel):
	x: float
	y: float
	z: float
	r: float

	def toDict(self):
		return {
			"x": self.x,
			"y": self.y,
			"z": self.z,
			"r": self.r
		}