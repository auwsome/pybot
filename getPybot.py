# from https://raw.githubusercontent.com/auwsome/pybot/master/getPybot.py

import os, sys, urllib2

realcwd = os.path.dirname(os.path.realpath(__file__))

urls=[0]*2; 
urls[0] = 'http://raw.githubusercontent.com/auwsome/pybot/master/Pybot.py'

if sys.platform == 'win32'  : urls[1] = 'https://raw.githubusercontent.com/auwsome/pybot/master/pluginWindows.py'
if sys.platform == 'android': urls[1] = 'https://raw.githubusercontent.com/auwsome/pybot/master/pluginAndroid.py'
if sys.platform == 'darwin' : urls[1] = 'https://raw.githubusercontent.com/auwsome/pybot/master/plugin .py'
if sys.platform == 'linux2' : urls[1] = 'https://raw.githubusercontent.com/auwsome/pybot/master/plugin .py'

print os.name, sys.platform

for i,url in enumerate(urls):
	req = urllib2.Request(url)
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
