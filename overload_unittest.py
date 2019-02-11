#!/urs/bin/env python3

#import requests
import unittest
import argparse
import hashlib
import sys
import os

def fetchRiakFile(url):
    os.system('curl -k -o remoteRiakFile %s' % url)
    md5Remote = hashlib.md5(open('remoteRiakFile', 'rb').read()).hexdigest()
    return md5Remote

def fetchLocalFile(riakFile):
    md5Local = hashlib.md5(open(riakFile, 'rb').read()).hexdigest()
    return md5Local

class TestOne(unittest.TestCase):
    def __init__(self, md5remote, md5local):
        super(TestOne, self).__init__('testone')
        self.md5remote = md5remote
        self.md5local = md5local
    
    def testone(self):
        self.assertEqual(self.md5remote, self.md5local)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-f', '--localFile', required=True)
    args = parser.parse_args()

    suite = unittest.TestSuite()
    try:
        md5remote = fetchRiakFile(args.url)
        md5local = fetchLocalFile(args.localFile)
    except Exception as e:
        print(e)

    suite.addTest(TestOne(md5remote, md5local))
    unittest.TextTestRunner().run(suite)
