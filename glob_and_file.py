#!/usr/bin/python


import glob
"""dzieki zaimportowaniu /glob/ mozemy dopasowac sobie pliki jakie zostana przez glob.glob() wyszukane"""

pliki = glob.glob('*.py')
for plik in pliki:
	print '     -----' + plik
	
	with open(plik) as f:
		for line in f:
			print '     ' + line.rstrip()
	print
