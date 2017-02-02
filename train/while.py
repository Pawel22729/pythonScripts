#!/usr/bin/python

from random import randint #importowanie funkcji randint()


losowaLiczba = randint(1,50)
print 'Losowanie zakonczone!'
print 'Jaka liczba zostala wylosowana? (przedzial od 1 do 50)'

podanaLiczba = int(raw_input('Podaj liczbe: '))

while podanaLiczba != losowaLiczba:


	if podanaLiczba > losowaLiczba:
		print 'Podana liczba jest za duza!'
	elif podanaLiczba < losowaLiczba:
		print 'Podana liczba jest za mala!'
	
	podanaLiczba = int(raw_input('Podaj ponownie liczbe: '))

print 'Poprawna odpowiedz!'
