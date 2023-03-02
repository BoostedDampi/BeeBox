import socket

class BeeBox:

	def __init__ (self, ip, port=80):
		self.ip = ip
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __connect(self, data="SEND"):
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s
				s.connect((self.ip, self.port))
				s.sendall(str.encode(data))
				response = s.recv(1024)
				if not response:
					raise Exception("FATAL: BeeBox didn't send any data, wtf?")
				return response
		except:
			print("FATAL: Something went wrong with the BeeBox connection")
			raise