#!/usr/bin/env python3
import socket
import argparse

parser = argparse.ArgumentParser(description='Transmit File from Shell to Shell.')
parser.add_argument('Host', nargs='?', default='192.168.43.165', metavar='IP-Address', help='IP Address')
parser.add_argument('Port', nargs='?', default=50000, metavar='Port', type=int, help='Port')

args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((args.Host, args.Port))
	while True:
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			data = conn.recv(1024)
			filename = open(data, 'w')
			conn.sendall(b'Received')

			while True:
				# In endless-loop
				data = conn.recv(1024)
				filename.write(str(data)[2:-1] + '\n')
				if not data:
					break
				print('Received', repr(data))
				conn.sendall(b'Received')
			filename.close()

