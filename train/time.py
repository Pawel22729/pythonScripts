#!/usr/bin/python

from time import localtime

aktywnosc = {8: 'Spanie',
	9: 'Dojazd',
	17: 'Praca',
	18: 'Dojazd',
	20: 'Jedzenie',
	22: 'Odpoczynek'}

czas_teraz = localtime()
godzina = czas_teraz.tm_hour

for czas_aktywnosci in sorted(aktywnosc.keys()):
	if godzina < czas_aktywnosci:
		print aktywnosc[czas_aktywnosci]
		break	
else:
	print 'Nieznana akcja lub spanie!'

