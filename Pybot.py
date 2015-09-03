# from https://github.com/auwsome/pybot
print 'init'
import os, sys, subprocess, time
import csv, json, urllib2
import mechanize
from BeautifulSoup import BeautifulSoup #bs4
#import threading
# try:
	# import serverSCP as s
# except ImportError,e: print str(e)




# vars
global realcwd; realcwd = os.path.dirname(os.path.realpath(__file__))
global cwd; cwd = os.getcwd()
#print 'path= ' realcwd
global dctn; dctn={'is':'equals', 'thing':'something', 'quit':'end loop', 'how':'thing', '?':'question mark', ' ':'space'}
global commands; commands = []
global input; input = "hi"
global args; args = None
global context; context = None
global prompt; prompt = 'test'
global channel; channel = 'raw_input('+prompt+'<>)'
print sys.platform
global dictName, cmdsName
global serverCheck; serverCheck = 0
global cmdline; 
if sys.platform == 'win32': 
	dictName = realcwd+'\dict.json'
	cmdsName = realcwd+'\commands.json'
	#### command line have to prefix running script with 'python'
	



global droid, d, tts 
######## check and set environment
if True or 'arm' in sys.platform:# == 'linux-armv71': 
	dictName = '/storage/sdcard1/dict.json'
	cmdsName = '/storage/sdcard1/commands.json'
	import android 
	from BeautifulSoup import BeautifulSoup
	droid = android.Android(); d = droid
	tts = True
	args = droid.getIntent().result[u'extras']
	print args
	#if args['%avcomm']: input = args['%avcomm']; print input

if tts: 
	channel = 'd.ttsSpeak("yes?"); input = droid.recognizeSpeech(None,None,None).result'
else: channel = 'input = raw_input(prompt)'

#### server, ie Cortana
if serverCheck==1:
	try: 
		print 'trying'
		input = str(s.listen())
		print 'done'
	except Exception,e: print 'no server\n'+str(e)

if sys.argv[1:]:
	try: 
		args = sys.argv[1:]
		if args: cmdline=1
		print args
		input = " ".join(args)
		print input, sys.argv[0:], len(sys.argv)
	except Exception,e: print str(e)







#input=""
print input
#############
def main(input=input, *args):
	response='hi'; choose=True; choice=""; YorN=None; words = ['']; more=0; next=0; link=0
	global droid, prompt

	#### MAIN LOOP:
	while response is not "":
	
		################### input and convert to list of words
		print 'input1='+input, "response1="+response #, "choice="+choice
		
		while input == "" or input == 'nospeech' or input is None:
			#input = droid.recognizeSpeech().result
			if not response: print 'noresponse'; exec(channel)# input = droid.recognizeSpeech().result#exec(channel)
			if choose: print 'choose'; prompt = 'choose'; exec(channel)#choice = droid.recognizeSpeech().result; input="choose"#exec(channel)
			if not choose and response: prompt = response+'>'; exec(channel); choice = input#input = droid.recognizeSpeech().result #  exec(channel)
			
			if input is None: time.sleep(7);  input="";  #print 2 #exec(channel)
			else: print "input2=",input;
		 
		#exec('print 2')
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
		if input == 'quit': response = ""
		if input == 'save': PBcreateBranch(); break
		if input == 'dctn': response = str(dctn); print response, dctn; continue
		if input == "hi": response = 'hello'
		if prompt == 'anything else? (yes/no)>':
			if YorN == 'yes': pass
			if YorN == 'no': break
		if input == "cancel voice": tts = False
		
		################### keyword based commands
		
		########## definitions
		if ' is ' in input and not 'what is ' in input and not words[0] == 'is': 
			df = input.split(' is ') #definition 
			try: dctn[df[0]] = df[1]
			except: print 'error, not entered' #dctn[df[0]]=[df[1]]
			if df[1] == 'action':
				dctn[df[0]]={'action':''}
				response = 'how '+ df[0] +"?" 
				context = dctn[df[0]]
			response = 'okay'
			#continue
			
		if ' is not ' in input: 
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
			query = input.replace('search ','')
			print "searching "+query
			from pygoogle import pygoogle
			g = pygoogle(query)
			g.pages = 1
			results = g.__search__(); #print str(results)
			choose=True; 
			response = results[link]['content']; #response = repr(response)
			response.encode('ascii')
			#response.encode('ascii', 'ignore'); 
			
		##################################################################################################################################	
		if choose:
			print 'chooseTrue'
			if choice == 'next': 
				next = next+1
			if choice == 'link':
				link=link+1; print 'link=',link
				response = results[link]['content']; #response = repr(response)
				response.encode('ascii', "ignore")
			if choice == 'go': 
				url = 'https://en.wikipedia.org/wiki/Cheese'#"http://www.wikipedia.org"
				#results[link]["url"]
				br = mechanize.Browser()
				br.set_handle_robots(False)
				br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
				#cj = cookielib.LWPCookieJar()
				#br.set_cookiejar(cj)
				br.set_handle_equiv(True)
				br.set_handle_redirect(True)
				#br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

				page = br.open(url); 
				html = page.read(); #print html
				soup = BeautifulSoup(html)#, "html.parser"); 
				#print soup
				VALID_TAGS = ['p','span']		#, 'ul', 'li', 'br']'div',
				paras=soup.p #findAll('p', text=True)
				#paras=soup.findAll("p","div")
				#print "paras",paras
				para=[]
				for i in paras:
					para.append(i.string)
				print 'para',para[:10]
				para = filter(None, para)
				#VALID_TAGS = ['p','span']		#, 'ul', 'li', 'br']'div',
				#[for i in paras]
				#paras = [i.text.encode('ascii',"ignore") for i in soup.findAll(VALID_TAGS)] ################## removes <p>s
				paras = filter(None, paras)
				#paras = [i.replace('\n','.').replace('\r','.') for i in paras] 
				#paras = [i.replace('(','parens').replace(')','parens').replace('[','bracket').replace(']','bracket') for i in para] 
				#print paras[:10]
				 
				response="".join(para)
				#input = raw_input('pause')
			
			
			
		######## actions
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
					#subprocess.Popen("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True, stdout=subprocess.PIPE)
					process.wait(); print process.returncode
			except Exception,e: print '3'+str(e)
			continue
		
		########################### catch unknown words
		# if words[0]:
			# for word in words:
				# word.strip('?')
				# if word not in dctn and 'is' not in input:  response = 'what is '+ word +"?"
			
		
		
		########################### output
		if response: print 'endresponse=',response
		else: prompt = 'anything else? (yes/no)>'
		
		if choose:
			print 'choose = ', choose
			if choice == 'cancel'	: choose = False
			if choice == 'more'		: more = more+1
			
			print 'choice = ', choice
			
			
			
		if os.name == 'posix': 
			tts = True #sys.platform == 'linux-armv71':
			ttsResponse = 'droid.ttsSpeak(response)'
			ttsWait = 'while droid.ttsIsSpeaking().result: pass'
			span = 16; responseChunks = [response.split(" ")]

		if tts: 
			print "chunking"
			if len(response.split(' ')) > span: 
				responseList = response.split(' ')
				#responseChunks = [" ".join(responseList[i:i+span]) for i in range(0, len(responseList)-span, span)]
				i = 0; chunk = [];
				for item in responseList:
					if i < span:
						chunk.append(item); i=i+1
					elif i==span:
						#print chunk
						responseChunks.append(chunk); i=0; chunk=[]
				else: pass
			response=" ".join(responseChunks[more]);print response
			print 'speaking', responseChunks; 
			exec(ttsResponse) ; exec(ttsWait) 
			
		print "endinput="+input
		input=""

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