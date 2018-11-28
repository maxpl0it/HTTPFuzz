from header import Header
import random, base64, string

class Authorization(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Authorization"
		self.max_length = 20
		self.value = self.generate_valid_value()

	def generate_basic_auth(self):
		username = ""
		password = ""
		chars = [i for i in string.ascii_uppercase + string.ascii_lowercase + string.digits + '_.']
		for i in range(random.randint(0, max(1, self.max_length))):
			username += random.choice(chars)
		for i in range(random.randint(0, max(1, self.max_length))):
			password += random.choice(chars)
		return "Basic " + base64.b64encode(username + ":" + password)

	def generate_valid_value(self):
		return random.choice([self.generate_basic_auth])()

	def mutate_validity(self, value):
		return self.value

	def mutate_length(self, value):
		current_max = self.max_length
		self.max_length = 1000
		value = self.generate_basic_auth()
		self.max_length = current_max
		return value

	def mutate(self, value):
		if random.randint(0, 1):
			for i in range(len(value)):
				if not random.randint(0, 10): # 1/10 chance of mutation with this method.
					value = value[:i] + chr(random.randint(0, 255)) + value[i + 1:]
		else:
			auth = ""
			for i in range(random.randint(0, max(1, 1000))):
				auth += chr(random.randint(0, 255))
			value = "Basic " + base64.b64encode(auth)
		return value
