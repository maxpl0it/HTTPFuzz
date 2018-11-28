from header import Header
import random

class AcceptEncoding(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Accept-Encoding"
		self.max_types = 10 # Allow this many types
		self.valid_encoding_values = ["*", "aes128gcm", "br", "compress", "deflate", "exi", "gzip", "identity", "pack200-gzip", "x-compress", "x-gzip", "z-std", "bzip2", "lzma", "peerdist", "sdch", "xpress", "xz"]
		self.value = self.generate_valid_value()

	def generate_valid_part(self):
		quality = ""
		if random.randint(0, 1): # Quality modifier
			quality = ";q=" + str(float(random.randint(0,10))/10)
		return self.valid_encoding_values[random.randint(0, len(self.valid_encoding_values) - 1)] + quality

	def generate_valid_value(self):
		values = list()
		for i in range(0, random.randint(1, max(1, self.max_types))):
			values.append(self.generate_valid_part())
		return ','.join(values)

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		values = list()
		for i in range(0, random.randint(1, 1000)):
			values.append(self.generate_valid_part())
		return value + ',' + ','.join(values)
