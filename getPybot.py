# from https://raw.githubusercontent.com/auwsome/pybot/master/getPybot.py

import os, sys, urllib2, ssl

realcwd = os.path.dirname(os.path.realpath(__file__))

#urls=[0]*2; 
urls={}; urls['Pybot.py'] = 'http://raw.githubusercontent.com/auwsome/pybot/master/Pybot.py'
#urls['pluginGitHub.py'] = 'http://raw.githubusercontent.com/auwsome/pybot/master/pluginGitHub.py'
if sys.platform == 'win32'  : urls['pluginWindows.py'] = 'https://raw.githubusercontent.com/auwsome/pybot/master/pluginWindows.py'
if sys.platform == 'posix linux-armv71': urls['pluginAndroid.py'] = 'https://raw.githubusercontent.com/auwsome/pybot/master/pluginAndroid.py'
if sys.platform == 'darwin' : urls['plugin.py'] = 'https://raw.githubusercontent.com/auwsome/pybot/master/plugin .py'
if sys.platform == 'linux2' : urls['plugin.py'] = 'https://raw.githubusercontent.com/auwsome/pybot/master/plugin .py'

print os.name, sys.platform
#ssl._create_default_https_context = ssl._create_unverified_context

for url in urls:
	req = urllib2.Request(urls[url])
	#context = ssl._create_unverified_context()
	#gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
	#response = urllib2.urlopen(req, context=gcontext)
	# print response.getcode()
	# print response.headers.getheader('content-type
	try:
		response = urllib2.urlopen(req, context=gcontext)
	except urllib2.HTTPError, e:
		print('HTTP Error', e)
		res = e.fp.read()
		#return json.loads(res), str(e)
	page = response.read()
	#print json.loads(res)
	outfile = os.path.join(realcwd,url)
	with open(outfile, 'w') as file:
		file.write(page)
	print outfile
