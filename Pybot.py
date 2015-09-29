# from https://github.com/auwsome/pybot
print 'init'
import os, sys, subprocess, time, re
import csv, json, urllib2, urlparse
import mechanize
try:
	import pyttsx
	import translator
	import serverSCP as s
except ImportError,e: print str(e)

#import PybotX as pbx
global tts

#### vars
global realcwd; realcwd = os.path.dirname(os.path.realpath(__file__))
global cwd; cwd = os.getcwd()
print 'path= ',realcwd
global dctn; dctn={'is':'equals', 'thing':'something', 'quit':'end loop', 'how':'thing', '?':'question mark', ' ':'space'}
global commands; commands = []
global input; input = "hi"
global args; args = None
global context; context = None
global prompt; prompt = 'test'
global channel; channel = 'raw_input('+prompt+'<>)'
tts = False
global dictName, cmdsName
global serverCheck; serverCheck = 0
global cmdline; 
global droid, d; droid=None





if sys.argv[1:]:
	try: 
		args = sys.argv[1:]
		if args: cmdline=1
		print args
		input = " ".join(args)
		print input, sys.argv[0:], len(sys.argv)
	except Exception,e: print str(e)
######## check and set environment
print sys.platform
#### win32+'>')"
# btw, command line needs to have prefix running script with 'python'
if sys.platform == 'win32': 
	from bs4 import BeautifulSoup
	#import bs4 as BeautifulSoup
	dictName = realcwd+'\dict.json'
	cmdsName = realcwd+'\commands.json'
	prompt='p>'
	tts = True
	channel = "input = raw_input(prompt)"
	engine = pyttsx.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-25)
	if tts:	responseChannel = 'engine.say(response); engine.runAndWait()'
	storageFile = 'PybotLines.py'
#### android
if 'arm' in sys.platform:# == 'linux-armv71': 
	dictName = '/storage/sdcard1/dict.json'
	cmdsName = '/storage/sdcard1/commands.json'
	import android 
	#from BeautifulSoup import BeautifulSoup
	from bs4 import BeautifulSoup
	droid = android.Android(); d = droid
	tts = True
	#channel = 'd.ttsSpeak("yes?"); input = droid.recognizeSpeech(None,None,None).result'
	channel = 'd.ttsSpeak("yes?"); input = droid.recognizeSpeech().result'
	args = droid.getIntent().result[u'extras']
	print args
	try: 
		if args: input = args['%avcomm']; print input
	except: pass
	responseChannel = 'droid.ttsSpeak(response);exec("while droid.ttsIsSpeaking().result: pass")'
	storageFile = realcwd+'/PybotLines.py'
#if os.name == 'posix': 
#### server, ie Cortana
if serverCheck==1:
	try: 
		print 'trying'
		channel = "input = str(s.listen())"
		print 'success'
	except Exception,e: print 'no server\n'+str(e)


	
	

	
	
#input=""
#print input
def main(input=input, *args):
	response=None; choose=False; choice=""; YorN=None; words = ['']; link=0; more=0;  more2=0;  more3=0; doChunk=True; responseChunks=[]
	url='https://en.wikipedia.org/wiki/Main_Page'
	global droid, prompt, tts
	exec('with open(storageFile) as file: list1 = file.readlines()')
	#### MAIN LOOP:
	#while response is not "":
	while True:
		try:
			################### input and convert to list of words
			print 'input1=',repr(input), "response1=",response #, "choice=",choice
			
			while input == "" or not input or input is None:
				# input = droid.recognizeSpeech().result
				# if not response: print 'noresponse'; input = droid.recognizeSpeech().result#exec(channel)
				# if choose: print 'choose'; prompt = choice; choice = droid.recognizeSpeech().result; input="choose"#exec(channel)
				# if not choose and response: input = droid.recognizeSpeech().result # prompt = response+'>'; exec(channel)
				if not response: prompt = '>'; exec(channel)
				#if not choose: prompt = '>'; exec(channel)
				if choose: print 'choose'; prompt = choice; exec(channel); choice = input.strip('\r'); input = ''; print choice; break
				#print 1
				if input is None: time.sleep(7); print 'input is None'; input=""; exec(channel)
				#else: print "input2=",input;
				
			input = input.strip('\r')
				
			try: exec(input)
			except Exception,e: print 'can\'t exec', str(e)
			#if input == 'set': continue
			# if input == 'loop': response = mainLoop()
			
			# run=True; tts=False
			# global response; reponse = True
			# code='';i=0
			# input = raw_input('yes?\n').strip('\r'); print repr(input)
			#input = input.strip('\r'); print repr(input)
			for index,item in enumerate(list1):
				try:
					exec(list1[index]);#print i;i=i+1
				except Exception,e: pass#print 'err', str(e)

			
			try: words = input.split(' ')
			except: pass
			
			#### set context(s)
			'''if context: 
				phrase2 = raw_input(str(context)+ ' is ')
				context['action'] = phrase2; context = None
				print dctn[df[0]]['action']
				#confirm = raw_input('confirm?')
				#if confirm == 'y':  context = confirm; context = None; input ="okay"'''
			
			################# direct commands
			# if input == 'quit': response = ""
			if input == 'quit' or input == 'q' or input == 'end' or input == 'exit': break
			if input == 'load': exec('with open(storageFile) as file: list1 = file.readlines()')
			if input == 'dump': exec('with open(storageFile, "wb") as file: file.writelines(list1)')
			if input == 'save': PBcreateBranch(); break
			if input == 'dctn': response = str(dctn); print response, dctn; continue
			if input == 'done':	choose = False
			if input == 'a': 
				line = raw_input("?")
				response = translator.main(line)
			
			# print 3################### keyword based commands
			
			######## parsing phrase
			if ' is ' in input and not 'what is ' in input and not words[0] == 'is': 
				df = input.split(' is ') #definition 
				try: dctn[df[0]] = df[1]
				except: print 'error, not entered' #dctn[df[0]]=[df[1]]
				if df[1] == 'action':
					dctn[df[0]]={'action':''}
					response = 'how '+ df[0] +"?" 
					context = dctn[df[0]]
				response = 'okay'
				
			if ' is not ' in input: 
				split= input.split(' is not ') #remove definition 
				try: dctn[split[0]].remove(split[1])
				except: pass
			
			###### question
			if '?' in input:	
				input = input.strip('?') 
				if 'what is' in input:
					q = input.split('what is ') 
					# print dctn[q[1]]
					if q[1] in dctn: response = dctn[q[1]]
					else: 
						try: input = "search "+q[1]
						except: response = q[1]+' is not known'
					
			###### google
			if 'search' in input:
				try:
					query = input.replace('search ','')
					print "searching.. "+query
					from pygoogle import pygoogle
					g = pygoogle(query)
					g.pages = 1
					results = g.__search__(); 
					#choose=True; 
					response = results[link]['content']; #response = repr(response)
					response = response.encode('ascii', 'ignore').replace('\n','')
					url = list(results[link]['url'])[0]; print url
					# response.encode('ascii', 'ignore'); 
					doChunk=False
				except Exception,e: print str(e)
				# print str(results)
				print response
				
			# print 5######## browse
			if choose:
				print 'chooseTrue'
				if choice == 'next': 
					link=link+1; print 'link=',link
					response = results[link]['content']; #response = repr(response)
					response.encode('ascii')
				print choice
				if choice == 'go':  
					try: 
						response = " ".join(go(url))
					except Exception,e: print str(e); input = raw_input('pause')
			if choose:
				print 'choose = ', choose
				print 'choice = ', choice
				if choice == 'cancel': choose = False
				
			###### actions
			if 'e' in input:
				exec1 = input.split('e ') #exec
				try: exec(exec1[1]); continue
				except Exception,e: print str(e)
			
			if 'do' in input: #action
				try: 
					exec(dctn[words[1]]['action']+' "'+str(''.join(words[2:99]))+'"'); continue
				except Exception,e: print str(e)
			
			print 'words=',words	
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
						# subprocess.Popen("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True, stdout=subprocess.PIPE)
						process.wait(); print process.returncode
				except Exception,e: print '3'+str(e)
				continue
			
			########################### catch unknown words
			# if words[0]:
				# for word in words:
					# word.strip('?')
					# if word not in dctn and 'is' not in input:  response = 'what is '+ word +"?"
					# if word not in dctn and 'is' not in input:  response = 'what is '+ word +"?"
				
			
			#print 7########################### output
			##if response: print 'endresponse=',response
			##else: prompt = 'anything else? (yes/no)>'
			
			if input == 'go': response = go(url); doChunk=True
			# if input == 'links': linksD=goLinks(); response = " ".join(linksD.keys()); doChunk=True; #choose = True
			if input == 'links': linksD=goLinks(url); responseChunks = linksD.keys();response=responseChunks; doChunk=True; #choose = True
			#if choice == 'more' or choice == 'and' or choice == 'm' or input == 'more' or input == 'm' or input == 'and': 
			if input == 'more' or input == 'm' or input == 'and': 
				for item in responseChunks: 
					if isinstance(item,list): nested = True
					else: nested = False
				if nested: 
					l1 = [item for sublist in responseChunks for item in sublist]
				#print 'l1',l1
					if l1[more]: response = l1[more]
				else: reponse = responseChunks[more]
				# while True:
					# if responseChunks[more]: 
						# if len(responseChunks[more]) > 1: 
							# if responseChunks[more][more2]:
								# if len(responseChunks[more][more2]) > 1: 
									# if responseChunks[more][more2][more3]: 
										# if len(responseChunks[more][more2][more3]) > 1: 
											# response = responseChunks[more][more2][more3]; print 1
											# more3 = more3+1; break
									# response = responseChunks[more][more2]; print 2
									# more2 = more2+1; break
						# response = responseChunks[more]; print 1
						# more = more+1; break
					# print 'no more'; response = 'no more'; break		
				more = more+1
				
			if input == 'repeat': response=responseChunks[more]
			if input == 'repeat last': response=responseChunks[more-1]
			if 'link ' in input: 
				link = input.replace('link ', '') #  list = input.split(" "); sub = [list.index("link"):list.index(",")]
				for k,v in linksD.items():
					if link in k:  url = v
				print url; response = go(url); doChunk=True
			
				
			#print 8 ################# chunking starts with objects, lists
			if tts and response and doChunk and len(response) > 50: 
				print 'chunking'
				responseChunks = chunk(response)
				print 'rc',responseChunks[0:50] #################
				response=responseChunks[0]
				# while True:
					# if responseChunks[more]: 
						# if len(responseChunks[more]) > 1: 
							# if responseChunks[more][more2]:
								# if len(responseChunks[more][more2]) > 1: 
									# if responseChunks[more][more2][more3]: 
										# if len(responseChunks[more][more2][more3]) > 1: 
											# response = responseChunks[more][more2][more3];break
									# response = responseChunks[more][more2];break
							# response = responseChunks[more];break
				# if any(isinstance(i, list) for i in response):
					# response=responseChunks[0][more]
				# else:
					# response=responseChunks[0]
				doChunk=False
				
			# print "endinput="+input
			input=""
			print response[0:500]
			if tts: 
				print 'speaking'; 
				exec(responseChannel) 
			if not choose: response = ''
			print 9 
		except Exception,e: 
			print 'main='+str(e)
			input = raw_input(prompt)

	dumpFiles() 
	print dctn	 
	sys.exit()	   

def chunk(response=''):
	#### takes list, returns list
	span = 16; chunked=[]
	#print 1,response
	#### splitypets on .
	#if isinstance(response, str):
	for index,sentences in enumerate(response):
		#responseSentences = response.replace('No.','number').replace('.','.!@#').split('!@#')
		#print repr(sentences)
		#split = sentences.split(".")
		response[index] = sentences.replace('No.','number').replace('. ','. !@#').split('!@#')
		#print response[index]
		#time.sleep(1)
		for phrases in chunked:
			#### splits on , 
			phrases = phrases.replace(',',',!@#').split('!@#'); #print phrases
			#### splits large clauses
			for clause in phrases:
				clauseWords = clause.split(" ")
				clause = splitChunks(clauseWords, span)
			print phrases
	#print 'rb',response
	#### and then joins small clauses
	for index,fragment in enumerate(response):
		for index,clause in enumerate(fragment):
			if len(clause) < span:
				small = clause
				try:
					smallR = phrases[index+1]
					if smallR is not None and len(smallR.split(" ")) < span and len(small.split(" "))+len(smallR.split(" ")) < span:
							#print smallR
						joined = ' '.join([small, smallR])
						phrases[index] = joined
						phrases.remove(smallR)
				except Exception,e: pass#print '4'+str(e)
			#print responseSentences
					
	#print 'r2',response
	#### returns list
	return response
			
def splitChunks(chunkList, span=16):
	#### checks and splits large clauses
	i=0; chunk=[]; chunks=[]
	if len(chunkList) > span:
		for word in chunkList:
			if i < span: chunk.append(word); i=i+1; 
			if i == span: chunks.append(" ".join(chunk)); i=0; chunk=[]
		chunks.append(" ".join(chunk)) # append last one
	return chunks

def combineChunks(chunkList, span=16):
	#### checks and joins small clauses
	for i in splitClauses:
		if len(i) < span:
			small = clause
			try:
				smallR = phrases[index+1]
				if smallR is not None and len(smallR.split(" ")) < span and len(small.split(" "))+len(smallR.split(" ")) < span:
						#print smallR
					joined = ' '.join([small, smallR])
					phrases[index] = joined
					phrases.remove(smallR)
			except Exception,e: print '4'+str(e)
	combinedClauses = splitClauses	
	return combinedClauses
	
def go(url='https://en.wikipedia.org/wiki/Main_Page'):#'http://www.google.com'):
	print 'going to.. ',url
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]  
	page = br.open(url); 
	response = page.read(); #print response[0:100]
	soup = BeautifulSoup(response, "html.parser"); 
	#paras=soup.p #findAll('p', text=True)
	#<b><a href="/wiki/Caesar_Hull" title="Caesar Hull">Caesar Hull</a></b>
	VALID_TAGS = ['p','span','b']# ,'b','li',
	paras = [i.text.encode('ascii',"ignore") for i in soup.find_all(VALID_TAGS)] ################## removes <p>s  .replace('-',' hyphen ')
	paras = filter(None, paras)
	paras = [i.replace('\n','.').replace('\r','.').replace('&quot;','"') for i in paras] 
	# paras = [i.replace('(','parens ').replace(')',' parens').replace('[','bracket').replace(']','bracket') for i in paras] 
	print 'p0:20', paras[0:20],'\n'
	#input = raw_input('pause')
	return paras

def goLinks(url='https://en.wikipedia.org/wiki/Main_Page'):#'http://www.google.com'):
	print 'going to.. ',url
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]  
	page = br.open(url); 
	response = page.read(); #print response[0:100]
	soup = BeautifulSoup(response, "html.parser"); 
	#paras=soup.p #findAll('p', text=True)
	#<b><a href="/wiki/Caesar_Hull" title="Caesar Hull">Caesar Hull</a></b>
	links={};VALID_TAGS = ['a']		#, 'ul', 'li', 'br']'div',
	paras = [i.get('href') for i in soup.find_all(VALID_TAGS)] ################## , html=True
	for link in soup.findAll('a'):
		if link.get('title') is not None:
			title = link.get('title').encode('ascii',"ignore"); #print title
			fullurl = urlparse.urljoin(url, link.get('href')).encode('ascii',"ignore"); #print fullurl
			links[title]=fullurl
			
		# if fullurl.startswith(inputURL):
			# if (fullurl not in resultUrl):
				# resultUrl[fullurl] = False
	# resultUrl[url] = True       # set as crawled
	paras = filter(None, paras)
	#print paras[0:20]
	linksL = list(links)
	print 'linksD=',linksL[0:20]
	#input = raw_input('pause')
	return links



def load():
	with open(storageFile) as file:
		list1 = file.readlines()
	return list1

def loop():
	run=True; tts=False
	global response; reponse = True
	code='';i=0
	input = raw_input('yes?\n').strip('\r'); print repr(input)
	#input = input.strip('\r'); print repr(input)
	for index,item in enumerate(list1):
		try:
			exec(list1[index]);#print i;i=i+1
		except Exception,e: pass#print 'err', str(e)
	return response

def mainLoop():
	global response; reponse = True
	while True:
		try:
			global list1; list1 = load(); print list1[0:3]
			while reponse: 
				if loop(): return response
				#if main(): pass
				else: 
					run = False
					input = raw_input('save?')
					if input == 'y': 
						with open(storageFile, 'wb') as file: 
							file.writelines(list1)
		except Exception,e: print str(e)
		input = raw_input('q?');print repr(input)
		if input == 'n\r': run = True
		if input == 'y\r': run = False; break



		
		
		

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