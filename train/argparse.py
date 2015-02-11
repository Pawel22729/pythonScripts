#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='testowy parser')
parser.add_argument('--verbose', action='store_true', help='przykladowa pomoc')
parser.add_argument('--liczba', type=int, required=True, help='ilosc czegos')
parser.add_argument('--lista', nargs='*', help='lsta liczb')
parser.add_argument('--defu', default=6, type=int, help='default 6')

args = parser.parse_args()

if args.verbose:
	print("Verbose!")
	print args.liczba
	print "-".join(args.lista)
	print args.defu
else:
	print("Nie Verbose")
