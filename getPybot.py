# from https://raw.githubusercontent.com/auwsome/pybot/master/getPybot.py

import os, urllib2

realcwd = os.path.dirname(os.path.realpath(__file__))

url1 = 'http://raw.githubusercontent.com/auwsome/pybot/master/Pybot.py'
#urls[1] = 'http://raw.githubusercontent.com/auwsome/pybot/master/sendPybot.py'
#for url in urls[url]:

req = urllib2.Request(url1)
response = urllib2.urlopen(req)
# print response.getcode()
# print response.headers.getheader('content-type
try:
	response = urllib2.urlopen(req)
except urllib2.HTTPError, e:
	print('HTTP Error', e)
	res = e.fp.read()
	#return json.loads(res), str(e)
page = response.read()
#print json.loads(res)

outfile = os.path.join(realcwd,'Pybot.py')
with open(outfile, 'w') as file:
	file.write(page)
print outfile
