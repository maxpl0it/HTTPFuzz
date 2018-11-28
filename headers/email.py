from header import Header
import random, string

class Email(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_size = 20
		self.name = "Email"
		self.value = self.generate_valid_value()

	def generate_host(self):
		host = ""
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		host += random.choice([".com", ".co.uk", ".in", ".us", ".net", ".org", ".pw", ".co.nz"])
		return host

	def generate_valid_value(self):
		username = ""
		for i in range(random.randint(1, max(1, self.max_size))):
			username += random.choice([i for i in string.ascii_lowercase])
		return username + "@" + self.generate_host()

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		old_size = self.max_size
		self.max_size = 1000
		value = self.generate_valid_value()
		self.max_size = old_size
		return value
