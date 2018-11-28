from header import Header
import random, string

class Forwarded(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_size = 10
		self.name = "Forwarded"
		self.value = self.generate_valid_value()

	def generate_ipv4(self):
		port = ""
		if random.randint(0, 1):
			port = ":" + str(random.randint(0, 65535))
		return '.'.join([str(random.randint(0, 255)) for i in range(4)]) + port

	def generate_ipv6(self):
		port = ""
		if random.randint(0, 1):
			port = ":" + str(random.randint(0, 65535))
		ip = ':'.join([''.join([random.choice([i for i in string.hexdigits[:16].upper()]) for i in range(4)]) for i in range(4)])
		if random.randint(0, 1):
			ip += ':' + ':'.join([''.join([random.choice([i for i in string.hexdigits[:16].upper()]) for i in range(4)]) for i in range(4)])
		else:
			ip += '::'
		return "\"[" + ip + "]" + port + "\""

	def generate_obfuscated_id(self):
		id = ""
		for i in range(random.randint(1, max(1, self.max_size))):
			id += random.choice(string.ascii_lowercase + string.digits + '_.')
		return id

	def generate_unknown(self):
		return "unknown"

	def generate_host(self):
		host = ""
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		host += random.choice([".com", ".co.uk", ".in", ".us", ".net", ".org", ".pw", ".co.nz"])
		return host

	def generate_valid_value(self):
		total = list()
		if random.randint(0, 1):
			total.append("by=" + random.choice([self.generate_ipv4, self.generate_ipv6, self.generate_obfuscated_id, self.generate_unknown])())
		if random.randint(0, 1):
			total.append("for=" + random.choice([self.generate_ipv4, self.generate_ipv6, self.generate_obfuscated_id, self.generate_unknown])())
		if random.randint(0, 1):
			total.append("host=" + self.generate_host())
		if random.randint(0, 1):
			if random.randint(0, 1):
				total.append("proto=http")
			else:
				total.append("proto=https")
		return '; '.join(total)

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		old_length = self.max_size
		self.max_size = 1000
		value = self.generate_valid_value()
		self.max_size = old_length
		return value
