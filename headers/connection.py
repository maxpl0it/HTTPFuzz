from header import Header
import random, string

class Connection(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Connection"
		self.maximum = 10
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		return random.choice(["Close", "Keep-Alive", "Upgrade"])

	def mutate_validity(self, value):
		chars = [ i for i in string.ascii_uppercase + string.ascii_lowercase + string.digits + '_.']
		for i in range(random.randint(0, max(0, self.maximum))):
			value += random.choice(chars)
		return value

	def mutate_length(self, value):
		return value*random.randint(0, 1000)
