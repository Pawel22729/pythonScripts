#!/usr/bin/python

rodzice, dzieci = (1, 1)
while dzieci < 1000000:
        print 'Ta generacja posiada {0} dzieci'.format(dzieci)
        rodzice, dzieci = (dzieci, rodzice + dzieci)                                                    
