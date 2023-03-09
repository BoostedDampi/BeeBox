import socket
import time
import bb_socket

class BeeBox:

	def __init__ (self, ip, port=80):
		self.ip = ip
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __connect(self, data="STATUS", retry=False):
		try:
			print(f"Starting connection to {self.ip}:{self.port}...")
			return bb_socket.connect(self.ip, self.port, data)

		except TimeoutError as e:
			if(retry):
				print("ERROR: Timeout Error, trying again in 2min...")
				time.sleep(60)
				print("1 Min to retry...")
				time.sleep(60)
				__connect(data, retry=True)
			else:
				print("FATAL: Second Timeout Error:\nThe BeeBox is not connected to internet or the ip/port is wrong")

	def statusReport(self):
		byte_data = __connect("STATUS")
		byte_data = b"weight:24,256 battery:86" #IMPORTANT remove this shit
		



lol = BeeBox("123.123", 8087)
lol.connect()