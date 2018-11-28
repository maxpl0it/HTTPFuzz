from header import Header
import random, string

class Referer(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_size = 30
		self.name = "Referer"
		self.value = self.generate_valid_value()

	def generate_host(self):
		host = ""
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		host += random.choice([".com", ".co.uk", ".in", ".us", ".net", ".org", ".pw", ".co.nz"])
		return host

	def generate_path(self, long=False):
		chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_.'
		uri = list()
		length = random.randint(0, 10)
		for i in range(random.randint(0, length)):
			uri.append(''.join(random.choice(chars) for j in range(random.randint(0, 10))))
		ending = ""
		length = 0
		if random.randint(0, 1):
			ending = "#" + ''.join(random.choice(chars) for j in range(length))
		return '/' + '/'.join(uri) + ending

	def generate_valid_value(self):
		return random.choice(["http://", "https://"]) + self.generate_host() + self.generate_path()

	def mutate_validity(self, value):
		return value

	def mutate_length(self, value):
		backup = self.max_size
		self.max_size = 1000
		domain = self.generate_host()
		self.max_size = backup
		return domain
