#!/usr/bin/env python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8989))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    buf = conn.recv(64)
    if len(buf):
	print buf
	break
