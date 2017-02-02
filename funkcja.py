#!/usr/bin/python

def funkcja(name):
	print 'Hello %s' % name


funkcja('Pawel')
funkcja('Ola')

wpisaneImie = raw_input('Imie do wypisania: ')

funkcja(wpisaneImie)
