#!/usr/bin/python

import sys

plik = sys.argv[1]

def czytaj(plik):
	file = open(plik, 'r')
	for i in file:
		if 'su' in i:
			print i

czytaj(plik)
