import random, headerwrapper, requestgenerator, bodygenerator

class RequestFrame:
	def __init__(self, args):
		self.header_mutate = float(args.header_mutate_level) / 10
		self.body_mutate = float(args.body_mutate_level) / 10
		self.request_mutate = float(args.request_mutate_level) / 10
		self.body_type = args.body_type
		self.all_headers = headerwrapper.HeaderWrapper().get_headers()
		self.request = ""

	def generate(self):
		request = self.generate_request()
		body = self.generate_body()
		params = {'request':request, 'body':body}
		headers = self.generate_headers(params)
		compiled_headers = self.compile_headers(headers)
		self.request = request + compiled_headers + "\r\n" + body

	def generate_request(self):
		request = requestgenerator.RequestGenerator()
		if float(random.randint(1, 10))/10 <= self.request_mutate:
			if not random.randint(0, 5):
				request.mutate_length()
			if not random.randint(0, 5):
				request.mutate()
		return request.method + ' ' + request.uri + ' ' + request.http_version + "\r\n"

	def generate_headers(self, params):
		headers = list()
		unused = range(len(self.all_headers))
		for i in range(random.randint(0, len(self.all_headers))):
			index = random.randint(0, len(unused) - 1)
			headers.append(self.all_headers[unused[index]](params=params))
			unused = unused[:index] + unused[index + 1:]
		return headers

	def generate_body(self):
		body = bodygenerator.BodyGenerator(self.body_type)
		if float(random.randint(1, 10))/10 <= self.body_mutate:
			body.mutate()
		return body.body

	def compile_headers(self, header_list):
		compiled = ""
		for header in header_list:
			if float(random.randint(1, 10))/10 <= self.header_mutate:
				if random.randint(0, 1):
					header.value = header.mutate_validity(header.value)
				if random.randint(0, 1):
					header.value = header.mutate_length(header.value)
				if random.randint(0, 1):
					header.value = header.mutate(header.value)
			compiled += header.name + ": " + header.value + "\r\n"
		return compiled
