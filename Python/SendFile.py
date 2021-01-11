#!/usr/bin/env python3
import socket
import argparse

parser = argparse.ArgumentParser(description='Transmit File from Shell to Shell.')

parser.add_argument('File', nargs='?', default='file.txt', metavar='File', help='File')
parser.add_argument('Host', nargs='?', default='192.168.43.165', metavar='IP-Address', help='IP Address')
parser.add_argument('Port', nargs='?', default=50000, metavar='Port', type=int, help='Port')

args = parser.parse_args()

# Open and read files
file1 = open(args.File, 'r')
Lines = file1.readlines()

# Connect to PC
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.Host, args.Port))

        # Send filename
        s.sendall(bytes(args.File, 'utf-8'))
        s.recv(10)

        # Send lines
        for line in Lines:
                s.sendall(bytes(line.strip(), 'utf-8'))
                s.recv(10)
s.close()
