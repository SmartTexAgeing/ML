#!/usr/bin/env python3

import socket
import time

HOST = '192.168.43.165'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	while True:
		s.sendall(b'Hello, world')
		data = s.recv(1024)
		print('Received', repr(data))
		time.sleep(0.25)
s.close()

