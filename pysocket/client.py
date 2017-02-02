#!/usr/bin/python

import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(('localhost', 8989))
cli.send('hello')
