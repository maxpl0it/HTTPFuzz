from header import Header
import random

class CacheControl(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Cache-Control"
		self.value = self.generate_valid_value()

	def generate_max_age(self):
		return "max-age=" + str(random.randint(-100000, 100000))

	def generate_max_stale(self):
		if random.randint(0, 1):
			return "max-stale=" + str(random.randint(-100000, 100000))
		else:
			return "max-stale"

	def generate_min_fresh(self):
		return "min-fresh=" + str(random.randint(-100000, 100000))

	def generate_no_cache(self):
		return "no-cache"

	def generate_no_store(self):
		return "no-store"

	def generate_no_transform(self):
		return "no-transform"

	def generate_only_if_cached(self):
		return "only-if-cached"

	def generate_valid_value(self):
		return random.choice([self.generate_max_age, self.generate_max_stale, self.generate_min_fresh, self.generate_no_cache, self.generate_no_store, self.generate_no_transform, self.generate_only_if_cached])()

	def mutate_validity(self, value):
		if '=' in value and random.randint(0, 1):
			value = value.split('=')[0] + '='
		elif '=' not in value and random.randint(0, 1):
			value = value + '='
		return value

	def mutate_length(self, value):
		return value + ''.join([str(random.randint(0, 1000)) for i in range(1000)])
