from header import Header
import random, string

class Upgrade(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Upgrade"
		self.value = self.generate_valid_value()

	def generate_valid_version(self):
		return str(random.randint(0, 10)) + '.' + str(random.randint(0, 9))

	def generate_valid_part(self):
		return random.choice(['HTTP', 'SHTTP', 'IRC', 'RTA', random.choice(string.ascii_uppercase) * random.randint(2, 10)]) + '/' + self.generate_valid_version()

	def generate_valid_value(self):
		return ', '.join([self.generate_valid_part() for i in range(random.randint(1, 10))])

	def mutate_validity(self, value):
		return value

	def mutate_length(self, value):
		return value*100
