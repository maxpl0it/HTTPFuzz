from header import Header
import random, string

class Host(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_size = 20
		self.name = "Host"
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		host = ""
		port = ""
		if random.randint(0, 1):
			port = ":" + str(random.randint(0, 65535))
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		host += random.choice([".com", ".co.uk", ".in", ".us", ".net", ".org", ".pw", ".co.nz"])
		return host + port

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		return value*100
