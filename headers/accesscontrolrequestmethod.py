from header import Header
import random

class AccessControlRequestMethod(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Accept-Control-Request-Method"
		self.methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"]
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		return random.choice(self.methods)

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		values = ""
		for i in range(0, random.randint(1, 1000)):
			if random.randint(0, 1):
				values += ' '
			values += self.generate_valid_value()
		return value + values
