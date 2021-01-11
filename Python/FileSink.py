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
            
            if (".txt" in data):
                filename = open(data, 'w')
                while True:
                    # In endless-loop
                    data = conn.recv(1024)
                    if not data:
                        break
                    filename.write(str(data)[2:-1] + '\n')
                    print('Received', repr(data))
                    conn.sendall(b'Received')
                    filename.close()
            else:
                print('Received', repr(data))
            conn.sendall(b'Received')