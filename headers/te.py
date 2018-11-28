from header import Header
import random

class TE(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "TE"
		self.value = self.generate_valid_value()

	def generate_valid_part(self):
		return random.choice(["compress", "deflate", "gzip", "trailers", "q"])

	def generate_valid_value(self):
		return ', '.join([self.generate_valid_part() for i in range(random.randint(1, 10))])

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		return ', '.join([self.generate_valid_part() for i in range(random.randint(1, 100))])
