#David Hermes 
import socket
from struct import pack, unpack
from time import sleep

#This function configures the Beebox with connection window time and debug mode
def configBeebox(ip, port, sleeptime, cap=True, debug=False):

	if cap and sleeptime > 48: #This is a security feature
		raise Exception("Sleep time is capped at 48h, you can stop this by setting cap=False")

	command = "1" + str(int(debug)) + str(sleeptime)

	if connect(ip, port, command) == "NULL":
		return False
	return True

#the status request should give back a few info: connection strenght (02-30), 
#battery voltage (3 numbers), debug mode (0 or 1).
def statusRequest(ip, port):
	rec_data = connect(ip, port, "2") #es. 02(02-30)231(2.31)0(0 o 1)

	if rec_data == "NULL" or len(rec_data) != 6:
		return "NULL"
	return rec_data[0:2], rec_data[2:5], bool(rec_data[5])

#data request gives back the weight in a packed double (py float is a double)
#TODO: try and excepts for data integrity
def dataRequest(ip, port):
	rec_data = connect(ip, port, "3") #es. 02(02-30)231(2.31)0(0 o 1)

	if rec_data == "NULL":
		return "NULL"
	return struct.unpack("!d", rec_data)


#General connection function, it retrys the connection 'retrys' times waiting
#for 10 seconds, this feature maybe is stupid but for ~2 connections per day i think
#it's worth it.
def connect(ip, port, data, retrys=2):

	for retr in range(retrys): #the -1 is only becouse the for goes to 
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			try:
				s.connect((ip, port))
				print("Sending data: " + data) #Data is always a Str so i can concatenate it.
				s.sendall(str.encode(data)) #Encode str in byteform
				response = s.recv(1024)
				if not response:
					raise Exception("FATAL: BeeBox didn't send any data, wtf?")
				print("BeeBox Responded")
				return response

			except TimeoutError:
				print("FATAL: Connection Timeout")
				s.close()
				if retrys == 1: return b"NULL"
				time.sleep(10)
			except:
				print("FATAL: General connection error")
				s.close()
				if retrys == 1: return b"NULL"
				time.sleep(10)


if __name__ == "__main__":
	print("Trying to connect:")
	ip = "127.0.0.1"
	port = 8088
	print(connect(ip, port, "1342").decode("utf-8"))
	print(configBeebox(ip, port, 10))
	print(statusRequest(ip, port))