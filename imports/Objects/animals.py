class Dog():
	def __init__(self, name, weight, height):
		self.name = name
		self.weight = weight
		self.height = height
	def dump_json(self):
		x = {
			"name": self.name,
			"weight": self.weight,
			"height": self.height,
        }
		return x