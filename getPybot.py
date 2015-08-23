

import os, urllib2

realcwd = os.path.dirname(os.path.realpath(__file__))

urls[0] = 'http://raw.githubusercontent.com/auwsome/pybot/master/Pybot.py'

for url in urls[url]:
	req = urllib2.Request(url1)
	response = urllib2.urlopen(req)
	# print response.getcode()
	# print response.headers.getheader('content-type')
	page = response.read()

	outfile = os.path.join(realcwd,'temp.py')
	with open(outfile, 'w') as file:
		file.write(page)
	print realcwd+'temp.py'
