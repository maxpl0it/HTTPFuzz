import random

class Header:
	def __init__(self, params=None):
		self.name = None
		self.value = None
		self.params = params

	def generate_valid_value(self):
		return None

	def mutate_validity(self, value):
		return value

	def mutate_length(self, value):
		return value*100

	def mutate(self, value):
		for i in range(len(value)):
			if not random.randint(0, 10): # 1/10 chance of mutation with this method.
				value = value[:i] + chr(random.randint(0, 255)) + value[i + 1:]
		return value
