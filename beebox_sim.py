#this is a script to test the BeeBox Server

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8088  # Port to listen on (non-privileged ports are > 1023)

print(f"Starting server on {HOST}:{PORT}...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
	    s.bind((HOST, PORT))
	    while(True):
		    s.listen()
		    print("Listining...")
		    conn, addr = s.accept()
		    with conn:
		        print(f"Connected by {addr}")
		        data = conn.recv(1024).decode("utf-8")

		        if not data:
		        	print("ERROR: No data receved")
		        print("Command receved: " + data)
		        
		        #floa = float(23.78)
		        #print(floa)
		        #send = pack('!f', floa)
		        #conn.sendall(send)
		        #print("Sent data... now closing")

		        if data[0] == '1':
		        	print("Receved a zero")
		        	conn.sendall(b"OK")
		        elif data[0] == '2':
		        	print("Receved status request:")
		        	conn.sendall(b"022311")
		        elif data[0] == '3':
		        	print("Receved dataRequest")
		        	conn.sendall(pack("!d", 123.12)) 

	except:
		print("Closing connection...")
		s.close()
		raise


