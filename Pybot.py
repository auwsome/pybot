# from https://github.com/auwsome/pybot

import os, sys, subprocess
import csv, json
#import threading
try:
	import serverSCP as s
except ImportError,e: print str(e)

# vars
global realcwd; realcwd = os.path.dirname(os.path.realpath(__file__))
global cwd; cwd = os.getcwd()
#print 'path= ' realcwd
global dctn; dctn={'is':'equals', 'thing':'something', 'quit':'end loop', 'how':'thing', '?':'question mark', ' ':'space'}
global commands; commands = []
global input; input = None
global args; args = None
global context; context = None

print sys.platform
global dictName, cmdsName
if sys.platform == 'win32': 
	dictName = realcwd+'\dict.json'
	cmdsName = realcwd+'\commands.json'
	#### command line have to prefix running script with 'python'
	try: 
		args = sys.argv[1:] 
		input = " ".join(args)
		#print input, words, sys.argv[0:], len(sys.argv)
	except Exception,e: print str(e)
	global cmdline; 
	if args: cmdline=1
	global serverCheck; serverCheck = 0
if sys.platform == 'android': 
	dictName = '/storage/sdcard1/dict.json'
	cmdsName = '/storage/sdcard1/commands.json'
	import pluginAndroid

#### server, ie Cortana
if serverCheck==1:
	try: 
		print 'trying'
		input = str(s.listen())
		print 'done'
	except Exception,e: print 'no server\n'+str(e)
	
	
def main(*args):
	response='hi';input='';choice=None;YorN=None
	#### MAIN LOOP:
	while response is not None:
		################### input and convert to list of words
		
		#### text input
		if not response: input = raw_input('>')
		#print 1
		if response: input = raw_input(response+'\n>')
		if choice: choice = raw_input('choose>')
		if YorN: YorN = raw_input(response+' (y/n)\n>')
		#if input == 'y' or 'yes': input = response
		#print 2
		# if input is None: 
			# prompt = response+'>'
			# input = raw_input('>')
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
		if input == 'quit': response = None	
		if input == 'save': PBcreateBranch(); break
		if input == 'dctn': response = str(dctn); print response, dctn; continue
		if 'hi' in input: response = 'hello'
		
		################### keyword based commands
		
		########## definitions
		if 'is' in input and not 'what is' in input and not words[0] == 'is': 
			df= input.split(' is ') #definition 
			try: dctn[df[0]] = df[1]
			except: print 'error, not entered' #dctn[df[0]]=[df[1]]
			if df[1] == 'action':
				dctn[df[0]]={'action':''}
				response = 'how '+ df[0] +"?" 
				context = dctn[df[0]]
			response = 'okay'
			#continue
			
		if 'is not' in input: 
			split= input.split(' is not ') #remove definition 
			try: dctn[split[0]].remove(split[1])
			except: pass
		
		######## question
		if '?' in input:	
			input = input.strip('?') 
			if 'what is' in input:
				q = input.split('what is ') 
				#print dctn[q[1]]
				if q[1] in dctn: response = dctn[q[1]]
				else: 
					try: input = "search "+q[1]
					except: response = q[1]+' is not known'
				
		######## google
		if 'search' in input:
			input = input.replace('search ','')
			print "searching "+input
			from pygoogle import pygoogle
			g = pygoogle(input)
			g.pages = 1
			#print '*Found %s results*'%(g.get_result_count())
			#print g.search_page_wise()#g.get_urls()
			#g.display_results()
			print g.display_results()
			#response = g.display_results()
			choose=True
		if choice:
			print response[choice]
		
		######## actions
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
			word.strip('?')
			if word not in dctn and 'is' not in input:  response = 'what is '+ word +"?"
			
		########################### output
		#if response: print response	
		if response is None: YorN = raw_input('anything else?')	
		print "input="+input
		

	dumpFiles() 
	print dctn	 
	sys.exit()	   



def readFiles():
	try: 
		with open(dictName, 'rb') as outfile:
			filedict = json.load(outfile)
			for key, value in filedict.items():
				if not key in dctn.keys(): dctn[key] = value
		with open(cmdsName, 'rb') as outfile:
			commands = json.load(outfile)
			#print commands
	except Exception,e: print sys.platform, str(e)
	
def dumpFiles():	
	try:	
		with open(dictName, 'wb') as outfile: ##sqlite to append
			json.dump(dctn, outfile)
	except Exception,e: print str(e)
	
def getFilesRemote(url=None):
	import urllib2
	urls={}; urls['pluginGitHub.py'] = 'http://raw.githubusercontent.com/auwsome/pybot/master/pluginGitHub.py'
	for url in urls:
		req = urllib2.Request(urls[url])
		response = urllib2.urlopen(req)
		# print response.getcode()
		# print response.headers.getheader('content-type')
		page = response.read()
		outfile = os.path.join(realcwd,url)
		with open(outfile, 'w') as file:
			file.write(page)
		print outfile

def PBcreateBranch():	
	getFilesRemote()
	import pluginGitHub
	pluginGitHub.createBranch(NEW_BRANCH_NAME='', HASH_TO_BRANCH_FROM='9b5b208fb7e12c69e33b27f249706a1c540d6c1e', targetuser='auwsome', repo='pybot',
				targetbranch='master', username='auwsome')

# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
	readFiles()
	main()
