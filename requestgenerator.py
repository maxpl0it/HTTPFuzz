import random, string

class RequestGenerator:
	def __init__(self):
		self.valid_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"]
		self.valid_http_versions = ["1.0", "1.1", "2"]
		self.method = self.get_valid_method()
		self.uri = self.get_valid_uri()
		self.http_version = self.get_valid_http_version()

	def get_valid_method(self):
		return self.valid_methods[random.randint(0, len(self.valid_methods) - 1)]

	def get_valid_uri(self, long=False):
		if not random.randint(0, 30) and not long:
			return '*'
		chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_.'
		uri = list()
		if long:
			length = random.randint(0, 1000)
		else:
			length = random.randint(0, 10)
		for i in range(random.randint(0, length)):
			uri.append(''.join(random.choice(chars) for j in range(random.randint(0, 10))))
		ending = ""
		length = 0
		if random.randint(0, 1):
			ending = "#" + ''.join(random.choice(chars) for j in range(length))
		return '/' + '/'.join(uri) + ending

	def get_valid_http_version(self):
		return "HTTP/" + self.valid_http_versions[random.randint(0, len(self.valid_http_versions) - 1)]

	def mutate_length(self):
		self.uri = self.get_valid_uri(long=True)

	def mutate(self):
		if not random.randint(0, 2):
			for i in range(len(self.method)):
				if not random.randint(0, 10): # 1/10 chance of mutation with this method.
					self.method = self.method[:i] + chr(random.randint(0, 255)) + self.method[i + 1:]

		if not random.randint(0, 2):
			for i in range(len(self.uri)):
				if not random.randint(0, 10): # 1/10 chance of mutation with this method.
					self.uri = self.uri[:i] + chr(random.randint(0, 255)) + self.uri[i + 1:]

		if not random.randint(0, 2):
			for i in range(len(self.http_version)):
				if not random.randint(0, 10): # 1/10 chance of mutation with this method.
					self.http_version = self.http_version[:i] + chr(random.randint(0, 255)) + self.http_version[i + 1:]
