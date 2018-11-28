from header import Header
import random

class Accept(Header):
	def __init__(self, params=None):
		Header.__init__(self, params)
		self.name = "Accept"
		self.max_types = 10 # Allow this many types
		self.valid_media_range = {"application":["javascript", "json", "x-www-form-urlencoded", "xml", "zip", "pdf", "sql", "graphsql", "ld+json", "msword", "vnd.openxmlformats-officedocument.wordprocessingml.document", "vnd.ms-excel", "vnd.openxmlformats-officedocument.spreadsheetml.sheet", "vnd.ms-powerpoint", "vnd.openxmlformats-officedocument.presentationml.presentation", "vnd.oasis.opendocument.text", "*"], "audio":["mpeg", "ogg", "*"], "multipart":["form-data", "*"], "text":["css", "html", "csv", "plain", "*"], "image":["png", "jpeg", "gif", "*"], "*":["*"]}
		self.valid_param_range = {"q":[str(float(i)/10) for i in range(11)], "charset":["UTF-8"]}
		self.value = self.generate_valid_value()

	def generate_valid_part(self):
		keys = self.valid_media_range.keys()
		media_type_a = keys[random.randint(0, len(keys) - 1)]
		media_type_b = random.randint(0, len(self.valid_media_range[media_type_a]) - 1)
		accept_params = ""
		if random.randint(0, 1):
			param_keys = self.valid_param_range.keys()
			param_type_a = param_keys[random.randint(0, len(param_keys) - 1)]
			param_type_b = random.randint(0, len(self.valid_param_range[param_type_a]) - 1)
			accept_params = ";" + param_type_a + "=" + self.valid_param_range[param_type_a][param_type_b]
		return media_type_a + "/" + self.valid_media_range[media_type_a][media_type_b] + accept_params

	def generate_invalid_part(self):
		keys = self.valid_media_range.keys()
		values = list()
		for key in keys:
			values += self.valid_media_range[key]
		accept_params = ""
		if random.randint(0, 1):
			param_keys = self.valid_param_range.keys()
			param_values = list()
			for key in param_keys:
				param_values += param_keys[key]
			accept_params = ";" + param_keys[random.randint(0, len(param_keys) - 1)] + "=" + param_values[0, len(param_values) - 1]
		return keys[random.randint(0, len(keys) - 1)] + "/" + values[random.randint(0, len(values) - 1)] + accept_params

	def generate_valid_value(self):
		total = list()
		for i in range(0, random.randint(1, max(1, self.max_types - 1))):
			total.append(self.generate_valid_part())
		return ','.join(total)

	def mutate_validity(self, value):
		total = list()
		for i in range(0, random.randint(1, max(1, self.max_types - 1))):
			total.append(self.generate_valid_part())
		value = ','.join(total)
		return value

	def mutate_length(self, value):
		total = list()
		for i in range(0, random.randint(1, 1000)):
			total.append(self.generate_valid_part())
		value += ',' + ','.join(total)
		return value
