# from https://github.com/auwsome/pybot

#try:
import os, sys, subprocess
import csv, json
import serverSCP as s
#import threading
#except Exception,e: print str(e)


dctn={'is':'equals', 'thing':'something', 'quit':'end loop', 'how':'thing', '?':'question mark', ' ':'space'}

readFiles()


################## init vars
context=None
words=['hi']
commands=[]
######### switches
cmdline=1
server1=1

#### command line
if cmdline==1:
	try: 
		words = sys.argv[1:] # have to prefix running script with 'python'
		input = " ".join(words)
		#print input, words, sys.argv[0:], len(sys.argv)
	except Exception,e: print str(e)

while True:
	response = None
	################### input and convert to list of words
	
	#### server, ie Cortana
	if server1==1:
		try: 
			print 'trying'
			input = str(s.listen())
			print 'done'
		except Exception,e: print '1'+str(e)
	
	#### text input from terminal
	if not input: 
		input = raw_input('>')
		try: words = input.split(' ')
		except: pass
	
	#### set context(s)
	'''if context: 
		phrase2 = raw_input(str(context)+ ' is ')
		context['action'] = phrase2; context = None
		print dctn[df[0]]['action']
		#confirm = raw_input('confirm?')
		#if confirm == 'y':  context = confirm; context = None; input ="okay"'''
	
	
	################### direct commands
	if input == 'quit': break
	if input == 'dctn': print dctn; continue
	
	################### keyword based commands
	
	########## definitions
	# if 'is' in input and not 'what is' in input and not words[0] == 'is': 
		# df= input.split(' is ') #definition 
		# try: dctn[df[0]].append(df[1])
		# except: pass #dctn[df[0]]=[df[1]]
		# if df[1] == 'action':
			# dctn[df[0]]={'action':''}
			# response = 'how '+ df[0] +"?" 
			# context = dctn[df[0]]
		# continue
		
	if 'is not' in input: 
		split= input.split(' is not ') #remove definition 
		try: dctn[split[0]].remove(split[1])
		except: pass
		
	if '?' in input:
		q = input.split('?') #question
		print dctn[q[0]]
		response = dctn[q[0]]
	
	########## actions
	if 'e' in input:
		exec1 = input.split('e ') #exec
		try: exec(exec1[1]); continue
		except Exception,e: print str(e)
	
	if 'do' in input: #action
		try: 
			exec(dctn[words[1]]['action']+' "'+str(''.join(words[2:99]))+'"'); continue
		except Exception,e: print str(e)
		
	if words[0] and words[0] in commands:
		try: 
			vcommand = words[0]
			try: context = words.get([1])
			except: print '1'
			command = commands[vcommand][context]
			pcommand = commands[vcommand]['print']
			print vcommand,words[0],pcommand
			print vcommand,context,command
			if pcommand is not None:
				input = raw_input(pcommand+' "'+str(''.join(words[2:99]))+'"? ')
				if not input == ('y' or 'yes'): break
				exec(pcommand+' "'+str(''.join(words[2:99]))+'"')
			if commands[vcommand]['windows'] is not None or context == 'windows':
				process = subprocess.Popen(commands[vcommand]['windows'], shell=True, stdout=subprocess.PIPE)
				#subprocess.Popen("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True, stdout=subprocess.PIPE)
				process.wait(); print process.returncode
		except Exception,e: print '3'+str(e)
		continue
	
	########################### catch unknown words
	for word in words:
		if word not in dctn:  response = 'what is '+ word +"?"
		
	########################### output
	if response: print response	
	
	if 'hi' in input: print 'hello'
	input=None


		
dumpFiles()   
print dctn	   
	   
sys.exit()	   



def readFiles():
	################## read-in files
	cwd = os.getcwd()
	realcwd = os.path.dirname(os.path.realpath(__file__))
	#print 'path= ' realcwd

	try: 
		dictNameWindows = realcwd+'\dict.json'
		dictNameAndroid = '/storage/sdcard1/dict.json'
		cmdsNameWindows = realcwd+'\commands.json'
		cmdsNameAndroid = '/storage/sdcard1/commands.json'
	except: pass

	try: 
		with open(dictNameWindows, 'rb') as outfile:
			filedict = json.load(outfile)
			for key, value in filedict.items():
				if not key in dctn.keys(): dctn[key] = value
		with open(cmdsNameWindows, 'rb') as outfile:
			commands = json.load(outfile)
	except Exception,e: print 'windows='+str(e)

	try: 
		with open(dictNameAndroid, 'rb') as outfile:
			filedict = json.load(outfile)
			for key, value in filedict.items():
				if not key in dctn.keys(): dctn[key] = value
		with open(cmdsNameAndroid, 'rb') as outfile:
			commands = json.load(outfile)
	except: pass #Exception,e: print 'android='+str(e)
	
def getFilesRemote():
	import os, urllib2

	realcwd = os.path.dirname(os.path.realpath(__file__))

	urls[0] = 'http://raw.githubusercontent.com/auwsome/pybot/master/Pybot.py'
	urls[0] = 'http://raw.githubusercontent.com/auwsome/pybot/master/sendPybot.py'

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

def dumpFiles():	
	try:	
		with open(dictNameWindows, 'wb') as outfile: ##sqlite to append
			json.dump(dctn, outfile)
		with open(dictNameAndroid, 'wb') as outfile: ##sqlite to append
			json.dump(dctn, outfile)
		# writer = csv.writer(open('dict.csv', 'ab+'))
	except Exception,e: print str(e)

def sendFiles():	
	createBranch(NEW_BRANCH_NAME='', HASH_TO_BRANCH_FROM='9b5b208fb7e12c69e33b27f249706a1c540d6c1e', targetuser='auwsome', repo='pybot',
				targetbranch='master', username='auwsome')

def createBranch(NEW_BRANCH_NAME=None, HASH_TO_BRANCH_FROM=None, targetuser=None, repo=None,
				targetbranch=None, username=None, password=None, baseurl='https://api.github.com'):
				
	import urllib, urllib2, json
	import getpass, base64

	if username is None:
		username = raw_input('Username: ')
	if password is None:
		password = getpass.getpass()
	if targetuser is None:
		username = raw_input('targetuser: ')
	if repo is None:
		repo = raw_input('repo: ')
	if NEW_BRANCH_NAME is None:
		repo = raw_input('NEW_BRANCH_NAME: ')

	data = {
	  "ref": 'refs/heads/'+NEW_BRANCH_NAME,
	  "sha": HASH_TO_BRANCH_FROM
	}
	#data = {"ref": "refs/heads/test4", "sha": "9b5b208fb7e12c69e33b27f249706a1c540d6c1e"}
	#print data
	datajson = json.dumps(data)
	#print datajson

	#suburl = 'repos/{user}/{repo}/pulls'.format(user=targetuser, repo=repo)
	suburl = 'repos/%s/%s/git/refs/heads' % (targetuser, repo)
	url = urllib.basejoin(baseurl, suburl)
	#print url
	
	req = urllib2.Request(url)
	#req.add_data(datajson)
	req = urllib2.Request("https://api.github.com/repos/%s/%s/git/refs" % (username, repo))

	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	req.add_header("Authorization", "Basic "+base64string) 
	#token = <token> ###########################################
	#req.add_header("Authorization", "token %s" % token)
	
	result = urllib2.urlopen(req, datajson)
	result = json.loads('\n'.join(result.readlines()))
	print result
	
	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
		print('HTTP Error', e)
		res = e.fp.read()
		return json.loads(res), str(e)
	res = response.read()
	return json.loads(res)

	

