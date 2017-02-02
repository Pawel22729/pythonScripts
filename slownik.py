#!/usr/bin/python

ceny = {'gruszki': 0.40, 'banany': 0.50}

zakupy = {'gruszki': 1, 'banany': 6}

rachunek = sum(ceny[owoc] * zakupy[owoc] for owoc in zakupy)

print 'Ogolnacena to: $%.2f' % rachunek
