#!/usr/bin/python -u

import os
import yaml
import shutil
import time
import tempfile
import re
import distutils.core
import subprocess

class Conf(object):
    def __init__(self, app):
	    self.app = app

    def createTemp(self):
            configDir = '/home/pls/configs/'
            path = configDir+self.app
            tmp = tempfile.mkdtemp()
	    subprocess.call('cp -r '+path+'/* '+tmp, shell=True)
	    return os.path.abspath(tmp)

    def findFiles(self):
	    config_files = []
	    path = self.createTemp()
	    for dirpath, dirnames, filenames in os.walk(path):
		    for name in filenames:
		   	    f = os.path.join(dirpath,name)
			    abso = os.path.abspath(f)			
		    	    config_files.append(abso)
            return config_files

    def findMaster(self):
            masterDir = '/home/pls/masterfiles/'
	    placeholders = []
	    f = open(masterDir+self.app, 'r')
	    for line in f:
		tmp = line.split(':')
		placeholders.append(tmp)
	    return placeholders
    

    def prepare(self):
    	    files = self.findFiles()
	    #masters = self.findMaster()
	    tmp = self.createTemp()
	    print files
	    #print masters
	    print tmp    

	   	

#regx = re.findall('{{(.*?)}', line)
#re.findall(':\s(.*$)', master)
#{{(.*?)}		
#{{[a-zA-Z0-9_-]*}}	
#                temp = tempfile.mkdtemp()


bbb = Conf('cinbox')
bbb.prepare()
#files = bbb.findFiles()
#masters = bbb.findMaster()
#print files
#print masters
