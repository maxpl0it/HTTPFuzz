from header import Header
import random

class ContentLength(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Content-Length"
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		return str(len(self.params['body']))

	def mutate_validity(self, value):
		if random.randint(0, 1):
			return str(random.randint(-1000000, 1000000))
		else:
			return str(float(random.randint(-1000000, 1000000)))

	def mutate_length(self, value):
		total = ""
		for i in range(random.randint(1, 100)):
			total += str(random.randint(0, 9))
		return value + total
