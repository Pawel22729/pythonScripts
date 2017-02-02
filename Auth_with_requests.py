#!/usr/bin/python

import requests

url = 'http://plasak.no-ip.org'
user = 'zdjecia'
passw = 'qazxdr'

req = requests.get(url, auth=(user,passw))
print req.text
req.close
