from header import Header
from authorization import Authorization
import random

class ProxyAuthorization(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Proxy-Authorization"
		self.auth = Authorization()
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		return self.auth.generate_valid_value()

	def mutate_validity(self, value):
		return self.auth.mutate_validity(value)

	def mutate_length(self, value):
		return self.auth.mutate_length(value)
