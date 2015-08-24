# from https://github.com/auwsome/pybot

import os, sys, subprocess
import csv, json
#import threading
try:
	#import serverSCP as s
except ImportError,e: print str(e)

if sys.platform.system() == 'windows': system = 'windows'
if os.name == 'android': system = 'android'
if os.name == 'posix': system = 'posix'
if sys.platform.system() == 'Linux': system = 'Linux'
print system

global realcwd = os.path.dirname(os.path.realpath(__file__))
global cwd = os.getcwd()
#print 'path= ' realcwd
global dctn={'is':'equals', 'thing':'something', 'quit':'end loop', 'how':'thing', '?':'question mark', ' ':'space'}

def main(input=None, context=None, words=['hi'], commands=[], cmdline=1, server1=0):
	#### command line
	if cmdline==1:
		try: 
			words = sys.argv[1:] # have to prefix running script with 'python'
			input = " ".join(words)
			#print input, words, sys.argv[0:], len(sys.argv)
		except Exception,e: print str(e)
		
	#### MAIN LOOP:
	while input is None:
		response = None
		################### input and convert to list of words
		
		#### server, ie Cortana
		if server1==1:
			try: 
				print 'trying'
				input = str(s.listen())
				print 'done'
			except Exception,e: print 'no server\n'+str(e)
		
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
		if input == 'save': PBcreateBranch(); break
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



def readFiles(system=None):
	################## read-in files
	if system == 'windows': 
		dictName = realcwd+'\dict.json'
		cmdsName = realcwd+'\commands.json'
	if system == 'android': 
		dictName = '/storage/sdcard1/dict.json'
		cmdsName = '/storage/sdcard1/commands.json'
	try: 
		with open(dictName, 'rb') as outfile:
			filedict = json.load(outfile)
			for key, value in filedict.items():
				if not key in dctn.keys(): dctn[key] = value
		with open(cmdsName, 'rb') as outfile:
			commands = json.load(outfile)
	except Exception,e: print system, str(e)
	
def dumpFiles():	
	try:	
		with open(dictName, 'wb') as outfile: ##sqlite to append
			json.dump(dctn, outfile)
	except Exception,e: print str(e)
	
def getFilesRemote(url=None):
	import urllib2
	urls[0] = 'https://raw.githubusercontent.com/auwsome/pybot/master/pluginGitHub.py'
	filenames[0] = 'pluginGitHub.py'
	for url in urls[url]:
		req = urllib2.Request(url1)
		response = urllib2.urlopen(req)
		# print response.getcode()
		# print response.headers.getheader('content-type')
		page = response.read()
		outfile = os.path.join(realcwd,filenames[url])
		with open(outfile, 'w') as file:
			file.write(page)
		print outfile

def PBcreateBranch():	
	getFilesRemote()
	import pluginGitHub
	pluginGitHub.createBranch(NEW_BRANCH_NAME='', HASH_TO_BRANCH_FROM='9b5b208fb7e12c69e33b27f249706a1c540d6c1e', targetuser='auwsome', repo='pybot',
				targetbranch='master', username='auwsome')

# run functions now that defined in any order above
if __name__=="__main__":
	readFiles(system)
	main()
