#!/usr/bin/env python3
import socket

HOST = '192.168.43.165'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

print('Starting Socket on Address 192.168.43.165:65432')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	while True:
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			while True:
				# In endless-loop	
				data = conn.recv(1024)
				if not data:
					break
				conn.sendall(data)

