from header import Header
import random, hashlib, base64

class ContentMD5(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Content-MD5"
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		hash = hashlib.md5()
		hash.update(self.params['body'])
		return base64.b64encode(hash.digest())

	def mutate_validity(self, value):
		total = ""
		for i in range(random.randint(1, 30)):
			total += chr(random.randint(0, 255))
		return base64.b64encode(total)

	def mutate_length(self, value):
		total = ""
		for i in range(random.randint(1, 100)):
			total += str(random.randint(0, 9))
		return value + total
