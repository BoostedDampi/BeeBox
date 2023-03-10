import socket
import time
import BMConnect

class BeeBox:

	def __init__ (self, ip, port=80):
		self.ip = ip
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	

	def statusReport(self):
		byte_data = __connect("STATUS")
		byte_data = b"weight:24,256 battery:86" #IMPORTANT remove this shit
		



lol = BeeBox("123.123", 8088)
lol.connect()