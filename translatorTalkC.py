'''
Table of contents

imports 
ISD starting definition

'''
print "init translator"
## imports
#import translated
#import nltk
import sys, re, json, operator, string
try:
	import pyttsx
	#from Pybot import responseChannel, engine
	# engine.say('test'); engine.runAndWait()
	# responseChannel = 'engine.say(response); engine.runAndWait()'
	# response = 'test'; exec(responseChannel)
except ImportError,e: print str(e)
#from pyDatalog import pyDatalog
'''
from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags'''


## global variables
#global pythonVerbsL; pythonVerbsString = 'print,exec,operator.add(something,b)'; pythonVerbsL = pythonVerbsString.split(","); print pythonVerbsL
#global verbsL; verbsString = 'write,make,create'; verbsL = verbsString.split(","); #print verbs
#global prepositions; prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")
global functionD; functionD = {}; #global pythonVerbsL; 
global ISD; ISD = {}; global verbose; verbose = True; global tts; tts = True

## wont exec args as is, args always parsed to something   
# "print"		:{"verb": {"mydef": ["s = eval(args0)","exec print(args0)"]  }},
ISD = {
"execute"				:{"verb": {"mydef": ["exec something"]  }},
"exec"				:{"verb": {"mydef": ["exec(something)"]  }},
#"exec something"	:{"verb": {"mydef": ["exec"]  }},
"print"		:{"verb": {"mydef": ["print(something)"]  }},
"write"		:{"verb": {"mydef": ["print something"]  }},
"speak"		:{"verb": {"mydef": ["exec engine.say(something);engine.runAndWait()"]  }},
"speak"		:{"verb": {"mydef": ["exec engine.say(something)"]  }},
"say"		:{"verb": {"mydef": ["print something", "speak something"]  }},
"shout"		:{"verb": {"mydef": ["write something","write '!!!'"], "otherdef": "yell"  }},    
"save"		:{"verb": {"mydef": ["exec 'saveD()'"]  }},
"responseChannel"		:{"noun": {"mydef": "engine.say(response); engine.runAndWait()"} }, 
"something"		:{"noun": {"mydef": "abc"} },
"tts"		:{"noun": {"mydef": "True"} },
"verbose"	:{"noun": {"mydef": "False"} }, #################
"verbose"	:{"noun": {"mydef": "True"} }, #################
"dict"		:{"noun": {"mydef": "ISD"} }
}; ISD0 = ISD
#isSD = re.sub("(\w+)", "'"+"\\1"+"'", isS); ## adds quotes around single words
# a.setdefault("somekey",[]).append("bob")

## helper functions
def sliceAt(stringA, slicePoint): return stringA[stringA.index(slicePoint)+len(slicePoint):]
def joins(listA): return "".join(listA)
def joins_(listA): return " ".join(listA)
def splits(stringA): return stringA.split(" ")
def enquote(item): return "'"+item+"'"#return "'%s'" % s1;return "'{}'".format(s1)
#l=['a']; print 111,quote(l[0]); s=l[0];print eval('s')
def tryExcept(tryA, exceptA):
	try:
		eval(tryA)
	except Exception, e: eval(ExceptA)
#def ifNotNoneReturnIt(item): return item if item else None  ## only if checking item doesn't throw exception

def forItem(container,operation): 
	for item in container: exec(operation)
def printIf(*args): operation = 'if item: print item'; forItem(args,operation) 
def ifVerbose(*args): return args if verbose else None 
def printIfVerbose(stringOfItem): s = ifVerbose(stringOfItem+"=",eval(stringOfItem)); print s if s else "",
def printV(*args): s = forItem(args,'printIfVerbose(item)') if args[0] else None; exec("eval('s')")
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
#print ifKeyReturnValue('verbose', ISD)
def ifKeyReturnValueISD(keyA, dictA=ISD): return ifKeyNotNoneReturnIt(dictA,keyA) ## check if dict has key and return it
#print ifKeyReturnValueISD('verbose')
def ifKeysReturnValueISD(*args): ## check if dict has key and return it
	def recursion(args):
		value = ISD
		for key in args: value = ifKeyReturnValue(key,value); returned = value if not isinstance(value, dict) else recursion(value)
		return returned
	return recursion(args)
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


def sliceArgs(listA): 
	args = string.join(listA[2:],'')
	if args in ISD.keys() and 'noun' in ISD[args].keys(): args = ISD[args]['noun']['mydef']
	return args
def str2bool(v): return v.lower() in ("yes", "true", "t", "1")
	
## initialization functions
def getFile(file): f = open(file,"rb"); return f.read(); f.close() 
def writeFile(file): f = open(file,"wb"); return f.read(); f.close()
def getFileLines(file): f = open(file,"rb"); return f.readlines(); f.close()
def getInstructions(): return getFileLines("pseudocode.py")
#if 'arm' in sys.platform: dName = '/storage/sdcard1/ISD.json'
#else: 
dName = "ISD.json"
def rememberD(dict1): 
	with open(dName) as json_file: dict1 = json.load(json_file) 
def remindNoodle(): return getFile("noodle.txt")
def remindNoodleJ(): return json.loads("noodle2.py")
def dictionaryNoodle(noodle): 
	for line in noodle: 
		if line.startswith("to"): verbDef = line[:line.index(",")]; functionString = line[line.index(",")+1:]; functionD[verbDef] = functionString
	return functionD
#return 1 if n <= 1 else n*f(f,n-1)
# if sys.platform = '': is[write] = (v,)
def saveD(dict1): json.dump(ISD, dName)
# class Bunch(object):
  # def __init__(self, adict):
    # self.__dict__.update(adict)
# x = Bunch(ISD); print x.write


global response; response = []; global args; args = None
rememberD(ISD)
############ main
def main(line):	
	#locals().update(globals()); 
	#printV('sys.platform','ISD'); printq
	global response ## puts global into locals
	global verbose; global tts; 
	#print 'verbose',ifKeysReturnValueISD("verbose",'noun','mydef')
	verbose = str2bool(ifKeysReturnValueISD("verbose",'noun','mydef'))#verbose = str2bool(ISD['verbose']['noun']['mydef']) 
	tts = str2bool(ifKeysReturnValueISD("tts",'noun','mydef'))#tts = str2bool(ISD['tts']['noun']['mydef'])
	printV('verbose','tts','response','args'); printq()
#### remind verb/function definitions
	noodle = remindNoodle()
	global verbD; verbD = dictionaryNoodle(noodle); #printV('verbD')
	#global ISD; #ISD = remindNoodleJ(); 
	if line.startswith("#"): return ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); # print line ## clean up line
	line = line.replace("quote","'").replace("unquote","'"); # print line ## replace 'quote's
	if line == '': return #if line: continue
	if line and verbose: print '=line: ',line ############
	if not line: return 
#### check for contractions and split imperative clauses
	# if 'and' or 'then' in line:	
		# lineSplit = line.split("and").split("then")
		# line[line.index()]
		# for line in lineSplit:
	#lineList = re.split('(\W+)', line); lineList = [i for i in lineList if i != " "] #print lineList ##########
	lineList = re.split('(\W)', line); lineList = [i for i in lineList if i != ""]
	if verbose: print '=lineList: ',lineList ########
##################### order of operations: check/set variables, check standard definitions, check conditionals (simple definitions), compute queries, compute imperatives 
	#### evaluate words for known definitions ############################################
	for index,item in enumerate(lineList):
		if ifKeysReturnValueISD(item,'noun','mydef'): 
			item = ISD[item]['noun']['mydef']; lineList[index] = item; print 'replaced..',item
			if verbose: print lineList[index] #global item; printV("item","args")
	#### imperative, conditional or query must be indicated by first word
	kw = lineList[0]; 
	if verbose: print 'kw=',kw 
	if not kw: print 'no keyword'
	############ check/set for variable definition
	#### check for variables as keys
	elif ifKeysReturnValueISD(line,'noun','mydef'): 
		if verbose: print ifKeysReturnValueISD(line,'noun','mydef')
		response=[ISD[line]['noun']['mydef']]; #response.append(ISD[line])
		#if response[0] == 'ISD': print response; #response[0] = ISD
	#### set variables as key and values
	elif 'is' in lineList: var = joins(lineList[:lineList.index('is')-1]); assignment = joins(lineList[lineList.index('is')+2:]); print var,"is",assignment; ISD[var] = {'noun':{'mydef':assignment}}; printV('ISD') ## print before assignment
	elif '=' in lineList: var = joins(lineList[:lineList.index('=')-1]); assignment = joins(lineList[lineList.index('=')+2:]); print 'defining..,',var,"=",assignment; ISD[var] = {'noun':{'mydef':assignment}}; print ISD[var]; printV('ISD'); printl()
	############ check for verb definitions or instructions
	elif kw == "to": 
		verbL = lineList[lineList.index("to"):lineList.index(",")]
		if 'something' in verbL: 
			needsParams = True; #verb = verbL.remove('something')
			verb = joins(lineList[lineList.index("to")+2:lineList.index("something")-1])
		else: verb = joins(lineList[lineList.index("to")+2:lineList.index(",")])
		if verbose: print verb, verbL;
		verbDefinition = joins(lineList[lineList.index(",")+2:])
		verbDefinitions = []
		#[verbDefinitions.append([i]) if i == "," else verbDefinitions[-1].append(i) for i in verbDefinition]
		verbDefinitions.append([verbDefinition])
		if verbose: print verb,2,ifKeyReturnValueISD(verb)
		if ifKeyReturnValueISD(verb): input = raw_input('do you want to add "%s"?' % verb)
		#if not ifKey(verb) or input == 'y': ISD[verb] = {'verb': verbDefinitions}
		if not ifKeyReturnValueISD(verb) or input == 'y': ISD[verb] = {'verb': {'mydef':verbDefinitions}}; print 'entered.. ',ISD[verb]
		if verbose: print 1,verbDefinition,2,verbDefinitions,3,ISD[verb],4,verb
	############ check for conditionals
	elif kw == "if": 
		#if verbose: print line
		#conditionalList = lineList[lineList.index('if'):lineList.index(', ')-1]; print conditionalList
		#if verb in conditionalList:
		if lineList[lineList.index('if')+1] == "I":
		#conditionList = conditionalList.remove("if"); print conditionList
		#if conditionList[0] == "I":
			if conditionList[1] == "say":
				command = joins(lineList[2:lineList.index(', ')-1])
				instructionWhole = line[line.index(',')+1:]
				if 'then' in instructionWhole: instructionWhole = instructionWhole.lstrip("then ")
				verbD[command] = instructionWhole
	############ check for ***QUERY***
	elif kw == "what":
		pass
	############ compute ***IMPERATIVE*** statements - verb + args
	elif kw in ISD.keys() and 'verb' in ISD[kw].keys() and 'mydef' in ISD[kw]['verb'].keys(): 
		global args; global count; ## puts local into globals or makes variable global
		imperativeList = lineList; count=0
		#### parse args
		args = sliceArgs(imperativeList)
		if verbose: print 'args0:',; printV('args'); printl()
		#####################################
		def computeImperative(imperativeList):
			global args ## puts global into locals
			global count; count=count+1;
			if count > 7: exit()
			#locals().update(globals()); printV('args'); 
			# def printIfVerbose1(stringOfItem): s = ifVerbose(stringOfItem+"=",eval(stringOfItem)); print s if s else "",
			# def forItem1(container,operation): 
				# for item in container: exec(operation)
			# def printV1(*args): s = forItem1(args,'printIfVerbose1(item)') if args[0] else None; exec("eval('s')") in globals(), locals()
			global response; global tts; global verb; global definition; global checkIfList; 
			if verbose: print('imperativeList:',imperativeList) #printV('imperativeList')
		############ parse imperative statements - verb + args
		######## sentence structure VO verb-object
		#### parse verb
			verb = imperativeList[0]; verbIndex = imperativeList.index(verb); printV('verb')
		#### parse args
			#printV('args')
#"print"		:{"verb": {"mydef": ["exec args0"]  }},
#s = "print 2"; print 4,s; main(s)
			if args: 
			#### copy original args
				global args0; args0 = args; printV('args0')
			#### evaluate args for known definitions
				#global argsL; argsL = imperativeList[verbIndex+2:]; printV('argsL'); printq()
				# for index,item in enumerate(argsL):
					# if ifKeysReturnValueISD(item,'noun','mydef'): 
						# item = ISD[item]['noun']['mydef']; argsL[index] = item; 
						# if verbose: print argsL[index] #global item; printV("item","args")
				#args = joins(argsL); printV('args')
			'''EXECUTE'''
		#### try ___EXECUTE///////\\\\\''''''|||*** definition with Python functions and args defined as string above or in definition
			if False:#verb == 'exec':
				print '\n', 'exec', imperativeList
				#args = sliceArgs(imperativeList)
				args = string.join(imperativeList[2:],'')####################################################
				print 'executing..'+args
				try: 
					interpretation = string.join([verb+"("+args+")"],''); print 'interpretation:',interpretation 
					exec(args) in globals(), locals(); ### not secure(?)
				except Exception,e: print '\n'+'myerror: exec: '+str(e)
		#### try execute definition with verb definitions and args 
			elif verb in ISD.keys(): 
				checkIfList = 'verb is in list form' if not isinstance(ISD[verb]['verb']['mydef'],list) else None; printIf(checkIfList)
			#### join verb and args
				definition = string.join([verb, args],' '); #globals().update(locals()); 
				printV('verb','args','definition')
			#### loop through verb definitions list and execute with original args
				for index,definition in enumerate(ISD[verb]['verb']['mydef']): 
					print '';print index; printV('definition') 
					try: 
						definitionL = definition.split(" "); 
						if verbose: print 3,definitionL
						if "=" in definition: pass
						else: computeImperative(definitionL)
					except Exception,e: print 'myerror: verb: '+str(e)
		computeImperative(imperativeList)
									
	elif kw == 'quit': 
		print 'noodle: ',noodle
		print 'ISD: ',ISD 
		input = raw_input("save?"); saveD() if input == 'y' else None; exit()
	elif kw not in ISD.keys(): print "I don't know how to.. "+kw
	else: print "I don't know what.. "+kw+" ..is"
	#globals().update(locals())
	if response:
		for x,i in enumerate(response):
			response = i; print response; printV('response')
			if tts: print 'speaking.. '; exec(responseChannel) in locals(),globals() 
		response = []
	printl()
	return response
			
			
def saveD(dict1=ISD):
	with open("ISD.json", 'wb+') as file: file.write(json.dumps(ISD, indent=4, sort_keys=True))  ## w+ = wr and overwrite
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
	######## check and set environment
	print sys.platform
	#### win32+'>')"
	# btw, command line needs to have prefix running script with 'python'
	if sys.platform == 'win32': 
		#from bs4 import BeautifulSoup
		#import bs4 as BeautifulSoup
		# dictName = realcwd+'\dict.json'
		# cmdsName = realcwd+'\commands.json'
		prompt='>'
		tts = True
		channel = "engine.say(prompt); engine.runAndWait();input = raw_input(prompt)"
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-25)
		#if tts:	
		responseChannel = 'engine.say(response); engine.runAndWait()'
		storageFile = 'PybotLines.py'
	#### android
	if 'arm' in sys.platform:# == 'linux-armv71': 
		#dictName = '/storage/sdcard1/dict.json'
		#cmdsName = '/storage/sdcard1/commands.json'
		import android 
		#from BeautifulSoup import BeautifulSoup
		#from bs4 import BeautifulSoup
		droid = android.Android(); d = droid
		tts = True
		#channel = 'd.ttsSpeak("yes?"); input = droid.recognizeSpeech(None,None,None).result'
		channel = 'd.ttsSpeak(prompt); input = droid.recognizeSpeech("test",None,None).result'
		channel = "input = raw_input(prompt)"
		args = droid.getIntent().result[u'extras']
		print args
		try: 
			if args: input = args['%avcomm']; print input
		except: pass
		responseChannel = 'droid.ttsSpeak(response);exec("while droid.ttsIsSpeaking().result: pass")'
		#storageFile = realcwd+'/PybotLines.py'
## do input from instructions
	inputList = getInstructions(); #print input
	#for index,line in enumerate(inputList):
		#main(line)
## do input from user
	line=None
	#while line != 'q':
	#response = 'hi'; exec(responseChannel); response = []; 
	prompt = '>'
	s = "exec print(1)"; print 1,s; main(s)
	s = "something = print(1)"; print 2,s; main(s)
	s = "execute something"; print 3,s; main(s)
	s = "print 2"; print 4,s; main(s)
	# s = "something = 'hello'"; print 1,s; main(s)
	# s = "exec print(something)"; print 2,s; main(s)
	# s = "another = 'hey'"; print 3,s; main(s)
	# s = "something1 = print(another)"; print 4,s; main(s)
	# s = "exec something1"; print 5,s; main(s)
	# s = "print 'hello'"; print 6,s; main(s)
	# s = "print something"; print 7,s; main(s)
	
	#main("print hello")
	while not line:
		#line = raw_input("?"); #print line
		exec(channel)
		if input is None: time.sleep(7); print 'input is None';
		else: line = main(input); #print line
	
'''

'''						