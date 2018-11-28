from header import Header
import random

class Expect(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Expect"
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		return "100-Continue"

	def mutate_validity(self, value):
		value = ""
		for i in range(random.randint(0, 20)):
			value += chr(random.randint(0, 255))
		return value

	def mutate_length(self, value):
		return value*random.randint(0, 1000)
