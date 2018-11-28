from header import Header
import random

class Range(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Range"
		self.value = self.generate_valid_value()

	def generate_valid_part(self):
		left = None
		right = None
		if random.randint(0, 1):
			left = str(random.randint(0, 10000))
		if random.randint(0, 1):
			right = str(random.randint(0, 10000))
		return ("" if left is None else left) + "-" + ("" if right is None else right)

	def generate_unit(self):
		return "bytes"

	def generate_valid_value(self):
		return self.generate_unit() + "=" + ','.join([self.generate_valid_part() for i in range(random.randint(1,5))])

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		return value*100
