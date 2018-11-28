import random

class MaxForwards:
	def __init__(self, params=None):
		self.name = "Max-Forwards"
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		return str(random.randint(0, 255))

	def mutate_validity(self, value):
		return random.choice(["", "-"]) + str(random.randint(0, 100000000000))

	def mutate_length(self, value):
		return value*100

	def mutate(self, value):
		for i in range(len(value)):
			if not random.randint(0, 10): # 1/10 chance of mutation with this method.
				value = value[:i] + chr(random.randint(0, 255)) + value[i + 1:]
		return value
