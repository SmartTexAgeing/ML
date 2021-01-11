#!/usr/bin/env python3
import socket
import argparse

parser = argparse.ArgumentParser(description='Transmit from Shell to Shell.')

parser.add_argument('Message', nargs='?', default='Hello', metavar='Message', help='Message')
parser.add_argument('Host', nargs='?', default='192.168.43.165', metavar='IP-Address', help='IP Address')
parser.add_argument('Port', nargs='?', default=40000, metavar='Port', type=int, help='Port')

args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.Host, args.Port))
        s.sendall(bytes(args.Message, 'utf-8'))
s.close()

