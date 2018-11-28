from header import Header
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import random, string

class Warning(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.max_size = 20
		self.name = "Warning"
		self.value = self.generate_valid_value()

	def generate_valid_warn(self):
		return random.choice([("110", "Response is Stale"), ("111", "Revalidation Failed"), ("112", "Disconnected Operation"), ("113", "Heuristic Expiration"), ("199", "Miscellaneous Warning"), ("214", "Transformation Applied"), ("299", "Miscellaneous Persistent Warning")])

	def generate_host(self):
		host = ""
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		host += random.choice([".com", ".co.uk", ".in", ".us", ".net", ".org", ".pw", ".co.nz"])
		return host

	def generate_pseudonym(self):
		host = ""
		for i in range(random.randint(1, max(10, self.max_size))):
			host += random.choice(string.ascii_lowercase + string.digits + '-')
		return host

	def generate_valid_warn_agent(self):
		return random.choice(['-', self.generate_pseudonym(), self.generate_host()])

	def generate_warn_date(self):
		now = datetime.now()
		stamp = mktime(now.timetuple())
		return '"' + format_date_time(stamp) + '"'

	def generate_valid_value(self):
		warn_code, warn_text = self.generate_valid_warn()
		return warn_code + ' ' + self.generate_valid_warn_agent() + ' "' + warn_text + '"' + (' ' + self.generate_warn_date() if random.randint(0, 1) else '')

	def mutate_validity(self, value):
		return value

	def mutate_length(self, value):
		return value*100
