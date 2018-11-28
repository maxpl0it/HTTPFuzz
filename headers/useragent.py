from header import Header
import random, string

class UserAgent(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "User-Agent"
		self.value = self.generate_valid_value()

	def generate_valid_version(self):
		return str(random.randint(0,100)) + ('.' + str(random.randint(0, 1000)) if random.randint(0, 1) else '') + (random.choice(string.ascii_lowercase) + str(random.randint(0, 10000)) if random.randint(0, 1) else '')

	def generate_valid_part(self):
		return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(1, 10))]) + "/" + self.generate_valid_version()

	def generate_valid_value(self):
		return ' '.join([self.generate_valid_part() for i in range(random.randint(1, 5))])

	def mutate_validity(self, value):
		return value

	def mutate_length(self, value):
		return value*100
