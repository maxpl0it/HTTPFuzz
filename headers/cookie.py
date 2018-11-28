from header import Header
import random, string

class Cookie(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_chars = 20
		self.name = "Cookie"
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		total = ""
		chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_.$!'
		while random.randint(0, 1):
			if len(total) > 0:
				total += "; "
			for i in range(random.randint(0, max(1, self.max_chars))):
				total += random.choice(chars)
			total += "="
			for i in range(random.randint(0, max(1, self.max_chars))):
				total += random.choice(chars)
		return total

	def mutate_validity(self, value):
		for i in range(len(value)):
			if not random.randint(0, 10):
				if random.randint(0, 1):
					value = value[:i] + '=' + value[i + 1:]
				else:
					value = value[:i] + ';' + value[i + 1:]
		return value

	def mutate_length(self, value):
		old_max = self.max_chars
		self.max_chars = 1000
		total = self.generate_valid_value()
		self.max_chars = old_max
		return total
