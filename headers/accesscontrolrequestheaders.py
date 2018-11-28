from header import Header
import random

class AccessControlRequestHeaders(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Accept-Control-Request-Headers"
		self.max_headers = 10
		self.headers = ["Accept", "Accept-Charset", "Accept-Datetime", "Accept-Encoding", "Accept-Language", "Access-Control-Request-Method", "Access-Control-Request-Headers"]
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		headers_list = list()
		for i in range(random.randint(1, max(1, self.max_headers))):
			headers_list.append(random.choice(self.headers))
		return ', '.join(headers_list)

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		values = list()
		for i in range(0, random.randint(1, 1000)):
			values.append(self.generate_valid_value())
		return value + ', ' + ', '.join(values)
