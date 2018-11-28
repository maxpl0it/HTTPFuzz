from header import Header
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import random

class IfUnmodifiedSince(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "If-Unmodified-Since"
		self.value = self.generate_valid_value()

	def generate_valid_value(self):
		now = datetime.now()
		stamp = mktime(now.timetuple())
		return format_date_time(stamp)

	def mutate_validity(self, value):
		return self.mutate(value)

	def mutate_length(self, value):
		values = list()
		for i in range(0, random.randint(1, 1000)):
			values.append(self.generate_valid_value())
		return value + ',' + ','.join(values)
