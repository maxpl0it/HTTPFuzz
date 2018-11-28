import random, string, json

class BodyGenerator:
	def __init__(self, body_type):
		self.max_length = 500
		self.body_type = body_type
		self.body = self.get_valid_body()

	def generate_junk(self):
		body = ""
		chars = [i for i in string.ascii_uppercase + string.ascii_lowercase + string.digits + '_.']
		for i in range(random.randint(0, self.max_length)):
			body += random.choice(chars)
		return body

	def generate_key(self, depth=None):
		return random.choice([random.choice(range(0, 1000)), ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(1, 10))])])

	def generate_value(self, depth):
		if depth == 0:
			return self.generate_key()
		return random.choice([self.generate_key, self.generate_list, self.generate_dictionary])(depth - 1)

	def generate_list(self, depth):
		if depth == 0:
			return []
		type_of_list = random.choice([self.generate_key, self.generate_dictionary, self.generate_list])
		generated_list = list()
		for i in range(random.randint(0, 10)):
			generated_list.append(type_of_list(depth - 1))
		return generated_list

	def generate_dictionary(self, depth):
		if depth == 0:
			return {}
		json_data = {}
		for part in range(random.randint(0, 10)):
			try:
				json_data[self.generate_key()] = self.generate_value(depth - 1)
			except:
				pass
		return json_data

	def generate_json(self):
		json_data = self.generate_dictionary(5)
		return json.dumps(json_data)

	def get_valid_body(self):
		body = ""
		if random.randint(0, 1): # Decides whether the request will have a body or not (provided no length mutation occurs)
			if self.body_type == 'rand':
				self.body_type = 'junk' if random.randint(0, 1) else 'json'
			if self.body_type == 'junk':
				body = self.generate_junk()
			else:
				body = self.generate_json()
		return body

	def mutate_length(self):
		self.body += self.get_valid_body()

	def mutate(self):
		body = ""
		for i in self.body:
			if random.randint(0, 1):
				body += chr(random.randint(0, 255))
			else:
				body += i
		self.body = body
