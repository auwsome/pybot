'''
Table of contents

imports 
ISD starting definition

'''
print "init translator"
## imports
import sys, re, json, operator, string
#print("%x" % sys.maxsize, sys.maxsize > 2**32) ## 32 or 64 bit

global functionD; functionD = {}; #global pythonVerbsL; 
global ISD; ISD = {}; global verbose; verbose = True; global tts; tts = True

#global aaa; aaa = 'engine.say(response); engine.runAndWait()'
ISD = {
"execute"	:{"verb": {"mydef": ["exec something"]  }},
"if"		:{"verb": {"mydef": ["something"]  }},
#"print"		:{"verb": {"mydef": ["exec print(something)"]  }},
"print"		:{"verb": {"mydef": ["exec eval(repr(something))"]  }},
"write"		:{"verb": {"mydef": ["print something"]  }},
"scrawl"	:{"verb": {"mydef": ["print something"]  }},
#"speak"		:{"verb": {"mydef": ["print speaking.. something","exec engine.say(something)","response = []"]  }},
#"speak"	:{"verb": {"mydef": ["print speaking.. something","exec droid.ttsSpeak(response)","response = []"]  }},
#responseChannel = 'droid.ttsSpeak(response);exec("while droid.ttsIsSpeaking().result: pass")'

#"speak"		:{"verb": {"mydef": ["print speaking.. something","exec responseChannel","response = []"]  }},
#"speak"		:{"verb": {"mydef": ["print speaking.. something","exec responseChannel","response = []"]  }},
"say"		:{"verb": {"mydef": ["print something", "speak something"]  }},
"sayiftts"	:{"verb": {"mydef": ["if not tts: print something", "if tts: say something"]  }},
"shout"		:{"verb": {"mydef": ["write something","write '!!!'"], "otherdef": "yell"  }},    
"save"		:{"verb": {"mydef": ["exec saveD()"]  }},
"dict"		:{"verb": {"mydef": ["say ISD"]  }},
#"speakifsys":{"verb": {"mydef": ["if sys_platform_win32: responseChannel = aaa","if sys_platform_arm: responseChannel = ''","print responseChannel","speak something"]  }},

"dict"		:{"verb": {"mydef": ["say ISD"]  }},


#"responseChannel"	:{"noun": {"mydef": "engine.say(response)"} }, 
#"responseChannel"	:{"noun": {"mydef": "engine.say(response); engine.runAndWait()"} }, 
"quit"		:{"noun": {"mydef": "False"} },
"sys_platform_win32"	:{"noun": {"mydef": "False"} },
"sys_platform_arm"		:{"noun": {"mydef": "False"} },
"sys_platform_i686"		:{"noun": {"mydef": "False"} },
"tts"		:{"noun": {"mydef": "True"} },
#"tts"		:{"noun": {"mydef": "False"} },
"verbose"	:{"noun": {"mydef": "False"} }, #################
#"verbose"	:{"noun": {"mydef": "True"} }, #################
"str1"		:{"noun": {"mydef": "'abc'"} },
"string1"	:{"noun": {"mydef": "'abc'"} },
"aString"	:{"noun": {"mydef": "'abc'"} },
"variable"	:{"noun": {"mydef": "'abc'"} },
#"response"	:{"noun": {"mydef": "'hi'"} },
"dict"		:{"noun": {"mydef": "ISD"} }
}; ISD0 = ISD

instructionsS = '''
#sayiftts 'hi'
to beep, if sys_platform_win32: exec import winsound; winsound.Beep(2500,300) 
#Freq = 2500 Dur = 100 
#to beep, if sys_platform_win32: exec import winsound; winsound.Beep(2500,300)
beep
# save 
## android ##
to vibrate, if sys_platform_arm: exec droid.vibrate()
#vibrate
# to make toast, if sys_platform_arm: exec droid.makeToast()
#to toast something, if sys_platform_arm: exec droid.makeToast(something)
#toast 'hi'
#to notify, if sys_platform_arm: exec droid.notify('notify',something)
#notify 'hi'

#packagename = 'com.chrome.android'
#classname = 'com.chrome.android.StartActivity'
# classname = None
#to start, if sys_platform_arm: exec droid.startActivity('android.intent.action.MAIN', None, None, None, False, packagename, classname)
#start

#to getInput, if sys_platform_arm: exec droid.getInput()
#getInput
#save
# string1
# print 1
#if sys_platform == win32: 
#speakifsys 'hello'
#speak 'hello'
#say 'hello'
'''

#### helper functions
def sliceAt(stringA, slicePoint): return stringA[stringA.index(slicePoint)+len(slicePoint):]
def joins(listA): return "".join(listA)
def joins_(listA): return " ".join(listA)
def splits(stringA): return stringA.split(" ")
#def enquote(item): return repr(item)#"'"+item+"'"#return "'%s'" % s1;return "'{}'".format(s1)
def tryExcept(tryA, exceptA):
	try:
		exec(tryA)
	except Exception, e: print 'exeception'; exec(exceptA)
def tryExceptPrint(tryA):
	try:
		exec(tryA)
	except Exception, e: print 'exeception',e
#def ifNotNoneReturnIt(item): return item if item else None  ## only if checking item doesn't throw exception
def forItem(container,operation): 
	for item in container: exec(operation)
def ifThenElse(if1,then1,else1): return then1 if if1 else else1
def printIf(*args): operation = 'if item: print item'; forItem(args,operation) 
def ifVerbose(*args): return args if verbose else None 
def printIfVerbose(stringOfItem): s = ifVerbose(stringOfItem+"=",eval(stringOfItem)); print str(s)+"\n" if s else "",
def printv(item): 
	if verbose: print item; response = item; exec(responseChannel)
#def printV(*args): s = forItem(args,'printIfVerbose(item)') if args[0] else None; exec("eval('s')")
def printV(*args): return forItem(args,'printv(item)') if args[0] else None
print "init translator"
#printV('ISD')
print "init translator"
def printl(): print '\n'
def printq(): print ""
def addQuotes(stringA): return "'"+stringA+"'"
def ifKeyNotNoneReturnIt(dictA,keyA): 
	if dictA and keyA in dictA.keys(): return dictA[keyA]  
	else: return None
def ifItemReturnIt(container,index): return container[index] if len(container)>=index else None
def ifKeyReturnValue(keyA, dictA): return ifKeyNotNoneReturnIt(dictA,keyA) ## check if dict has key and return it
def ifKeyReturnValueISD(keyA, dictA=ISD): return ifKeyNotNoneReturnIt(dictA,keyA) ## check if dict has key and return it
def ifKeysReturnValueISD(*args): ## check if dict has key and return it
	def recursion(args):
		value = ISD
		for key in args: value = ifKeyReturnValue(key,value); returned = value if not isinstance(value, dict) else recursion(value)
		return returned
	return recursion(args)
def str2bool(v): return v.lower() in ("yes", "true", "t", "1")
	
#### initialization functions
def getFile(file): f = open(file,"rb"); return f.read(); f.close() 
def writeFile(file): f = open(file,"wb"); return f.read(); f.close()
def getFileLines(file): tryExceptPrint('f = open(file,"rb"); return f.readlines(); f.close()')
def getInstructions(): 
	if getFileLines("pseudocode.py"): return getFileLines("pseudocode.py")
	else: instructionsL = instructionsS.split("\n"); return instructionsL
dName = "ISD.json"
def rememberD(dict1): 
	with open(dName) as json_file: dict1 = json.load(json_file) 
def remindNoodle(): return getFile("noodle.txt")
def remindNoodleJ(): return json.loads("noodle2.py")
def dictionaryNoodle(noodle): 
	for line in noodle: 
		if line.startswith("to"): verbDef = line[:line.index(",")]; functionString = line[line.index(",")+1:]; functionD[verbDef] = functionString
	return functionD
def saveD(dict1): json.dump(ISD, dName)
#import importlib
#def import1(modulename): modulename = importlib.import_module(modulename)




#global response; 
response = []; global args; args = None; global responseChannel
tryExceptPrint('rememberD(ISD)')
############ main
def main(line):	
#### line format first for readlines from file
	if line.startswith("#"): return ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); # print line ## clean up line
	line = line.replace("quote","'").replace("unquote","'"); # print line ## replace 'quote's
	if line == '': return #if line: continue
	lineList = re.split('(\W)', line); lineList = [i for i in lineList if i != ""]
	#locals().update(globals()); 
	#printV('sys.platform','ISD'); printqexecute 
#### verbosity
	#global response ## puts global into locals
	#global verbose; global tts; 
	#print 'verbose',ifKeysReturnValueISD("verbose",'noun','mydef')
	verbose = str2bool(ifKeysReturnValueISD("verbose",'noun','mydef'))#verbose = str2bool(ISD['verbose']['noun']['mydef']) 
	tts = str2bool(ifKeysReturnValueISD("tts",'noun','mydef'))#tts = str2bool(ISD['tts']['noun']['mydef'])
#### verbose print/respond function under each subfunction
	#print 1,eval(repr(verbose)), 2,repr(verbose), 3,verbose; 
	def printv(item): 
		if verbose: response = repr(item)+":"+str(eval(item)); exec(responseChannel) in globals(), locals()
	def printV(*args): 
		for item in args: printv(item)
	#printV('verbose','tts','response','args'); 
	printV('tts'); 
	global args; global args0; 
	global count; ## puts local into globals or makes variable global
	args = ''; args0 = ''
	#s = "print 'line=:',line" if line else None; eval('s')
	#if verbose: print '=lineList:',lineList ########
	printV('line')
	print(lineList) ####
#### remind verb/function definitions
	#noodle = remindNoodle()
	#global verbD; verbD = dictionaryNoodle(noodle); #printv('verbD')
	#global ISD; #ISD = remindNoodleJ(); 
	#if line and verbose: print 'line=:',line ############
	
#### check for contractions and split imperative clauses
##################### order of operations: check and set variables, try to execute, check standard definitions, check conditionals (simple definitions), compute queries, compute imperatives 
	############ check/set for variable definition
	#### check for variables as keys
	if ifKeysReturnValueISD(line,'noun','mydef'): 
		if verbose: print ifKeysReturnValueISD(line,'noun','mydef')
		response = ISD[line]['noun']['mydef']; exec(responseChannel) in globals(), locals(); return 
	#### set variables as key and value
	if 'is' in lineList: 
		var = joins(lineList[:lineList.index('is')-1]); assignment = joins(lineList[lineList.index('is')+2:]); 
		print 'defining..,',var,"is",assignment; ISD[var] = {'noun':{'mydef':assignment}}; print ISD[var]; return 
	if '=' in lineList: 
		var = joins(lineList[:lineList.index('=')-1]); assignment = joins(lineList[lineList.index('=')+2:]); 
		print 'defining..,',var,"=" ,assignment; ISD[var] = {'noun':{'mydef':assignment}}; print ISD[var]; return 
	############ try to execute	
	try: 
		if verbose: print 'trying as is..',line
		response = str(eval(line)); exec(responseChannel) in globals(), locals(); 
		#exec(line) in globals(), locals(); print '\n'; 
		return
	except Exception, exception: 
		if verbose: print 'myerror: cannot exec as is:',str(exception)
	################ imperative, conditional or query must be indicated by first word
	kw = lineList[0]; 
	if verbose: print 'kw:',kw 
	if not kw: print 'no keyword'
	############ check for verb definitions or instructions
	elif kw == "to": 
		verbL = lineList[lineList.index("to"):lineList.index(",")]
		if 'something' in verbL: 
			needsParams = True; #verb = verbL.remove('something')
			verb = joins(lineList[lineList.index("to")+2:lineList.index("something")-1])
		else: verb = joins(lineList[lineList.index("to")+2:lineList.index(",")])
		if verbose: print verb, verbL;
		verbDef = joins(lineList[lineList.index(",")+2:])
		verbDefs = []
		#[verbDefs.append([i]) if i == "," else verbDefs[-1].append(i) for i in verbDef]
		verbDefs.append(verbDef)
		if verbose: print verb,':existing entry:',ifKeyReturnValueISD(verb)
		if ifKeyReturnValueISD(verb): input = raw_input('do you want to add to or replace "%s"?' % verb)
		#if not ifKey(verb) or input == 'y': ISD[verb] = {'verb': verbDefs}
		if not ifKeyReturnValueISD(verb) or input == 'y': ISD[verb] = {'verb': {'mydef':verbDefs}}; print 'entered.. ',verb,':=:',ISD[verb]
		#d if verbose: print verb 1,verbDef,2,verbDefs,3,ISD[verb],4,verb
	############ check for conditionals
	elif kw == "if": pass
		#if verbose: print line
		#conditionalList = lineList[lineList.index('if'):lineList.index(', ')-1]; print conditionalList
		#if verb in conditionalList:
		# if lineList[lineList.index('if')+1] == "I":
		#conditionList = conditionalList.remove("if"); print conditionList
		#if conditionList[0] == "I":
			# if conditionList[1] == "say":
				# command = joins(lineList[2:lineList.index(', ')-1])
				# instructionWhole = line[line.index(',')+1:]
				# if 'then' in instructionWhole: instructionWhole = instructionWhole.lstrip("then ")
				# verbD[command] = instructionWhole
	############ check for ***QUERY***
	elif kw == "what": pass
		
		
	#####################################
	############ compute ***IMPERATIVE*** statements - verb + args
	elif ifKeysReturnValueISD(kw,'verb','mydef'): 
		imperativeList = lineList; count=0
	### parse original args
		args0 = string.join(imperativeList[2:],'')
		# if verbose: print 'args0:',; printv('args')
	#####################################
		def computeImperative(imperativeList):
		#### verbose print/respond function under each subfunction
			def printv(item): 
				if verbose: print item; response = item; exec(responseChannel) in globals(), locals()
			def printvv(stringA): 
				if verbose: ev = eval(stringA); print stringA, ev
		#### break infinite loops at certain depth
			global count; count=count+1; ## puts global into locals
			if count > 7: exit()
			global verb; global args;  global args0; #global definition; global verbDef;)
		############ parse imperative statements - verb + args.. sentence structure VO verb-object
			if verbose: print('imperativeList:',imperativeList) #printv('imperativeList')
		#### parse verb
			verb = imperativeList[0]; verbIndex = imperativeList.index(verb); printv('verb')
		#### parse args
			args = string.join(imperativeList[2:],''); printv('args')
		#### replace variables, i.e. evaluate words for known definitions 
			for index,item in enumerate(imperativeList):
				if ifKeysReturnValueISD(item,'noun','mydef'): 
					item0 = item; item = ISD[item]['noun']['mydef']; 
					if imperativeList[index-1] == "\\": continue ## escape conflicting noun definitions
					if item != 'something': 
						imperativeList[index] = item; print 'defined..',item0,':with:',item; 
						if verbose: print imperativeList[index], imperativeList  
						computeImperative(imperativeList); return
		#### try execute if verb = exec
			if verb == 'exec':
			#### execute if definition is not recursive
				execArgs = args; print 'executing..',execArgs
				try: 
					exec(execArgs) in globals(), locals(); ### not secure(?)
				except NameError, exception: 
					execArgs = repr(execArgs); print 'trying..', execArgs
					try: 
						exec(execArgs) in globals(), locals(); ### not secure(?)
					except Exception,exception: print 'myerror: exec2: '+str(exception)
				except Exception, exception: print 'myerror: myexec: '+str(exception)
				return
		#### try execute definition with verb definitions and args 
			if verb in ISD.keys(): 
			#### execute if not multiple
				if len(ISD[verb]['verb']['mydef']) == 1: 
					printv('single')
				#### evaluate conditionals
					if verb == 'if':
						printv('if'); condition = joins(imperativeList[2:imperativeList.index(":")]); print 'condition:', repr(condition), '..is..', eval(condition)
						if eval(condition): definitionL = imperativeList[imperativeList.index(":")+3:]; print 'eval',definitionL; computeImperative(definitionL); return
						else: print 'not'; return
				#### define..	
					verbDef = ISD[verb]['verb']['mydef'][0]; print 'verbDef:', verbDef #printvv('verbDef')
				#### replace 'something' in definitions
					if 'something' in verbDef: 
						if verb in ['print','write','speak','say']: 
							if not args[0] in ["'",'"']: args = repr(args)
						verbDef = verbDef.replace("something",args); print 'replaced verbDef "something" with', args
				#### recurse if definition is recursive
					print 'recurse'; verbDefL = re.split('(\W)', verbDef); 
					computeImperative(verbDefL); return 
			#### loop through multiple verb definitions and execute with original args
				if len(ISD[verb]['verb']['mydef'])>1:
					
					print 'multiple'
					for index,verbDef in enumerate(ISD[verb]['verb']['mydef']): 
						print index, verbDef#printvv('definition') #if verbose: print 3,definitionL
					#### replace 'something' in definitions
						if 'something' in verbDef: 
							verbDef = verbDef.replace("something",args0); print 'replaced verbDef "something" with', args0
						verbDefL = re.split('(\W)', verbDef); verbDefL = [i for i in verbDefL if i != ""] 
						try: 
							computeImperative(verbDefL); 
						except Exception,e: print 'myerror: multiple '+str(e)
						
					return response
			
		computeImperative(imperativeList)
	#####################################
	
		
	elif kw == 'quit': 
		print 'noodle: ',noodle
		print 'ISD: ',ISD 
		input = raw_input("save?"); saveD() if input == 'y' else None; exit()
	elif kw not in ISD.keys(): print "I don't know how to.. "+kw
	else: print "I don't know what.. "+kw+" ..is"
	printl()
	#return response
	return None
			
def saveD(dict1=ISD):
	d = json.dumps(ISD, indent=4, sort_keys=True)
	with open("ISD.json", 'wb+') as file: file.write(d)  ## w+ = wr and overwrite
	#if verbose: pass
	print json.dumps(dict1)
	
def write(sequence, preposition=False, object2=False):
	fileName=''
	globals().update(locals())
	if object2:
		# check for filename
		if 'file named' in object2:
			fileName = sliceAt(object2,'file named '); print fileName
		if fileName: pass
		else: fileName = 'temp.txt'
	if preposition: 
		if preposition == 'in': fileMode = 'wb'
		if preposition == 'into': fileMode = 'ab'
		if preposition == 'over': fileMode = 'wb'
		if isinstance(sequence,list):
			with open(fileName, fileMode) as file: file.writelines(sequence)
		if isinstance(sequence,str):
			with open(fileName, fileMode) as file: file.write(sequence)
	else: print sequence #'sequence>',sequence	


	
# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
######## check for command line args
	input = None
	print sys.argv
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
		ISD['sys_platform_win32'] = {'noun':{'mydef':'True'}}
		# main('sys_platform_win32 = True')
		# main('sys_platform_arm = False')
		#tryS = 'try:\n\t'+'import pyttsx\n'+'except ImportError,e: print str(e)'; exec(tryS)
		try:
			import pyttsx
		except ImportError,e: print str(e)
		#engine.say('test'); engine.runAndWait()
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-25)
		
		prompt='>'
		channel = "engine.say(prompt); engine.runAndWait();input = raw_input(prompt)"
		#if tts:	
		
		if tts: responseChannel = 'print response; engine.say(response); engine.runAndWait()'
		else: responseChannel = 'print response'
		#storageFile = 'PybotLines.py'
		#from bs4 import BeautifulSoup
		#import bs4 as BeautifulSoup'
	#### android
	if 'arm' in sys.platform:# == 'linux-armv71': 
		ISD['sys_platform_arm'] = {'noun':{'mydef':'True'}}
		# main('sys_platform_arm = True')
		# main('sys_platform_win32 = False')
		import android 
		#from BeautifulSoup import BeautifulSoup
		#from bs4 import BeautifulSoup
		droid = android.Android(); d = droid
		prompt = ''
		#channel = 'd.ttsSpeak("yes?"); input = droid.recognizeSpeech(None,None,None).result'
		channel = 'd.ttsSpeak(prompt); input = droid.recognizeSpeech("test",None,None).result'
		channel = "input = raw_input(prompt)"
		args = droid.getIntent().result[u'extras']; print args
		try: 
			if args: input = args['%avcomm']; print input
		except: pass
		if tts: responseChannel = 'print response; droid.ttsSpeak(response); exec("while droid.ttsIsSpeaking().result: pass")'
		else: responseChannel = 'print response'
		#storageFile = realcwd+'/PybotLines.py'
## do input from instructions
	inputList = getInstructions(); #print input
	for index,line in enumerate(inputList):
		main(line)
## do input from user
	result=None
	#while line != 'q':
	#response = 'hi'; exec(responseChannel); response = []; 
	#main("say hello")
	while result:
		#line = raw_input("?"); #print line
		quit = str2bool(ifKeysReturnValueISD("quit",'noun','mydef'))
		tts = str2bool(ifKeysReturnValueISD("tts",'noun','mydef'))
		if not input: exec(channel);
		else: print 'input:',input
		if input is None: time.sleep(7); print 'input is None';
		else: 
			result = main(input); input = None

		
		
		
		

'''
from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags'''	

#import translated
#import nltk
#from pyDatalog import pyDatalog

## global variables
#global pythonVerbsL; pythonVerbsString = 'print,exec,operator.add(something,b)'; pythonVerbsL = pythonVerbsString.split(","); print pythonVerbsL
#global verbsL; verbsString = 'write,make,create'; verbsL = verbsString.split(","); #print verbs
#global prepositions; prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")	

# def sliceArgs(listA): 
	# args = string.join(listA[2:],'')
	# if args in ISD.keys() and 'noun' in ISD[args].keys(): args = ISD[args]['noun']['mydef']
	# return args

#isSD = re.sub("(\w+)", "'"+"\\1"+"'", isS); ## adds quotes around single words
# a.setdefault("somekey",[]).append("bob")

##To get your call to work, you'll need to use dictionary unpacking like this: func(**{MyEnum.X.name: 1})		
#print 111, ifKeysReturnValue('verbose','noun','mydef')
# def ifKeysReturnValue(*args, **kwargs): ## check if dict has key and return it
	##for key, value in kwargs.items(): print key, value
	# def recursion(args):
		# if isinstance(args[0],dict): value = args[0]; args = args[1:]; print value
		# for key in args: value = ifKeyReturnValue(key,value); returned = value if not isinstance(value, dict) else recursion(value)
		# return returned
	# return recursion(args)
# print 222, ifKeysReturnValue(ISD,'verbose','noun','mydef',d='ISD')

# class Bunch(object):
  # def __init__(self, adict):
    # self.__dict__.update(adict)
# x = Bunch(ISD); print x.write

#return 1 if n <= 1 else n*f(f,n-1)
# if sys.platform = '': is[write] = (v,)

	#globals().update(locals())
	# if response:
		# for x,i in enumerate(response):
			# response = i; print response; printV('response')
			# if tts: print 'speaking.. '; exec(responseChannel) in locals(),globals() 
		# response = []

	
'''

'''						