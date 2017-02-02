#!/usr/bin/python

import threading
import time
import glob
import os

l = glob.glob("*.txt")

def loop(x):
	 f = file(x, 'r+') 
	 print '%s' % ''.join(map(str,f.readlines()))
	 f.close()

for i in range(len(l)):
	t = threading.Thread(target=loop, args = (l[i],))
	t.start()
