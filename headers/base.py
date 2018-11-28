from header import Header
import random

class Base(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = None
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		return None

	def mutate_validity(self, value):
		return value

	def mutate_length(self, value):
		return value*100
