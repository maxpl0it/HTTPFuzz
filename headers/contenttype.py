from header import Header
import random

class ContentType(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Content-Type"
		self.max_types = 10 # Allow this many types
		self.valid_media_range = {"application":["javascript", "json", "x-www-form-urlencoded", "xml", "zip", "pdf", "sql", "graphsql", "ld+json", "msword", "vnd.openxmlformats-officedocument.wordprocessingml.document", "vnd.ms-excel", "vnd.openxmlformats-officedocument.spreadsheetml.sheet", "vnd.ms-powerpoint", "vnd.openxmlformats-officedocument.presentationml.presentation", "vnd.oasis.opendocument.text", "*"], "audio":["mpeg", "ogg", "*"], "multipart":["form-data", "*"], "text":["css", "html", "csv", "plain", "*"], "image":["png", "jpeg", "gif", "*"], "*":["*"]}
		self.value = self.generate_valid_value()

	def generate_valid_part(self):
		keys = self.valid_media_range.keys()
		media_type_a = keys[random.randint(0, len(keys) - 1)]
		media_type_b = random.randint(0, len(self.valid_media_range[media_type_a]) - 1)
		return media_type_a + "/" + self.valid_media_range[media_type_a][media_type_b]

	def generate_invalid_part(self):
		keys = self.valid_media_range.keys()
		values = list()
		for key in keys:
			values += self.valid_media_range[key]
		return keys[random.randint(0, len(keys) - 1)] + "/" + values[random.randint(0, len(values) - 1)]

	def generate_valid_value(self):
		return self.generate_valid_part()

	def mutate_validity(self, value):
		return self.generate_valid_part()

	def mutate_length(self, value):
		left = ""
		right = ""
		for i in range(random.randint(1, 1000)):
			left += chr(random.randint(0, 255))
		for i in range(random.randint(1, 1000)):
			right += chr(random.randint(0, 255))
		return left + "/" + right
