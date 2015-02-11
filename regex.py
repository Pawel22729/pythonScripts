#!/usr/bin/python

import re
for test_string in ['555-333', '4444-111']:
	if re.match(r'^\d{3}-\d{3}$', test_string):
		print test_string, 'Liczba poprawna!'
	else:
		print test_string, 'Liczba niepoprawna!'
