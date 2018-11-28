from header import Header
import random, string

class IfRange(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_tags = 3
		self.max_tag_size = 10
		self.name = "If-Range"
		self.value = self.generate_valid_value()

	def generate_valid_part(self):
		tag = "\""
		if random.randint(0, 1):
			tag = "W/" + tag
		chars = [j for j in string.ascii_lowercase + string.digits + '-']
		for i in range(random.randint(0, max(1, self.max_tag_size))):
			tag += random.choice(chars)
		return tag + "\""

	def generate_valid_value(self):
		if random.randint(0, 1):
			return "*"
		total = list()
		for i in range(random.randint(0, max(1, self.max_tags))):
			total.append(self.generate_valid_part())
		return ', '.join(total)

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		old_size = self.max_tag_size
		old_count = self.max_tags
		self.max_tag_size = 1000
		self.max_tags = 1000
		part = self.generate_valid_value()
		self.max_tag_size = old_size
		self.max_tags = old_count
		return value*100
