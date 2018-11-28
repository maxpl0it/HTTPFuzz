from header import Header
import random, string

class Via(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_size = 20
		self.name = "Via"
		self.value = self.generate_valid_value()

	def generate_valid_version(self):
		return str(random.randint(0, 10)) + '.' + str(random.randint(0, 9))

	def generate_host(self):
		host = ""
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		host += random.choice([".com", ".co.uk", ".in", ".us", ".net", ".org", ".pw", ".co.nz"])
		return host

	def generate_pseudonym(self):
		host = ""
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		return host

	def generate_valid_part(self):
		return ((random.choice(string.ascii_uppercase) * random.randint(2, 10)) + "/" if random.randint(0, 1) else '') + self.generate_valid_version() + " " + (self.generate_host() + (':' + str(random.randint(0, 65535)) if random.randint(0, 1) else '') if random.randint(0, 1) else self.generate_pseudonym())

	def generate_valid_value(self):
		return ', '.join([self.generate_valid_part() for i in range(random.randint(1, 10))])

	def mutate_validity(self, value):
		return value

	def mutate_length(self, value):
		return value*100
