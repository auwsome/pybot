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
"exec"		:{"verb": {"mydef": [""]  }},
"execute"	:{"verb": {"mydef": ["exec something"]  }},
"if"		:{"verb": {"mydef": ["something"]  }},
#"exec something"	:{"verb": {"mydef": ["exec"]  }},
"print"		:{"verb": {"mydef": ["exec print(something)"]  }},
"write"		:{"verb": {"mydef": ["print something"]  }},
"scrawl"	:{"verb": {"mydef": ["print something"]  }},
"speak"		:{"verb": {"mydef": ["exec engine.say(something);engine.runAndWait()"]  }},
"say"	:{"verb": {"mydef": ["print something", "speak something"]  }},
"sayiftts"		:{"verb": {"mydef": ["if not tts: print something", "if tts: say something"]  }},
"shout"		:{"verb": {"mydef": ["write something","write '!!!'"], "otherdef": "yell"  }},    
"save"		:{"verb": {"mydef": ["exec 'saveD()'"]  }},
"dict"		:{"verb": {"mydef": ["say ISD"]  }},
"responseChannel"	:{"noun": {"mydef": "engine.say(response)"} }, 
#"responseChannel"	:{"noun": {"mydef": "engine.say(response); engine.runAndWait()"} }, 
"something"	:{"noun": {"mydef": "abc"} },
"tts"		:{"noun": {"mydef": "True"} },
#"tts"		:{"noun": {"mydef": "False"} },
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
def enquote(item): return repr(item)#"'"+item+"'"#return "'%s'" % s1;return "'{}'".format(s1)
#l=['a']; print 111,quote(l[0]); s=l[0];print eval('s')
def tryExcept(tryA, exceptA):
	try:
		eval(tryA)
	except Exception, e: eval(ExceptA)
#def ifNotNoneReturnIt(item): return item if item else None  ## only if checking item doesn't throw exception

def forItem(container,operation): 
	for item in container: exec(operation)
def ifThenElse(if1,then1,else1): return then1 if if1 else else1
def printIf(*args): operation = 'if item: print item'; forItem(args,operation) 
def ifVerbose(*args): return args if verbose else None 
def printIfVerbose(stringOfItem): s = ifVerbose(stringOfItem+"=",eval(stringOfItem)); print str(s)+"\n" if s else "",
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
#### line format first for readlines from file
	if line.startswith("#"): return ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); # print line ## clean up line
	line = line.replace("quote","'").replace("unquote","'"); # print line ## replace 'quote's
	if line == '': return #if line: continue
	lineList = re.split('(\W)', line); lineList = [i for i in lineList if i != ""]
	if verbose: print '=lineList:',lineList ########
	#locals().update(globals()); 
	#printV('sys.platform','ISD'); printq
#### verbosity
	global response ## puts global into locals
	global verbose; global tts; 
	#print 'verbose',ifKeysReturnValueISD("verbose",'noun','mydef')
	verbose = str2bool(ifKeysReturnValueISD("verbose",'noun','mydef'))#verbose = str2bool(ISD['verbose']['noun']['mydef']) 
	tts = str2bool(ifKeysReturnValueISD("tts",'noun','mydef'))#tts = str2bool(ISD['tts']['noun']['mydef'])
	printV('verbose','tts','response','args'); #printq()
#### remind verb/function definitions
	noodle = remindNoodle()
	global verbD; verbD = dictionaryNoodle(noodle); #printV('verbD')
	#global ISD; #ISD = remindNoodleJ(); 
	#if line and verbose: print 'line=:',line ############
	s = "print 'line=:',line" if line else None; eval('s')
#### check for contractions and split imperative clauses
##################### order of operations: check/set variables, evaluate words,  check standard definitions, check conditionals (simple definitions), compute queries, compute imperatives 
	############ check/set for variable definition
	#### check for variables as keys
	if ifKeysReturnValueISD(line,'noun','mydef'): 
		if verbose: print ifKeysReturnValueISD(line,'noun','mydef')
		response=[ISD[line]['noun']['mydef']]; return
	#### set variables as key and values
	if 'is' in lineList: 
		var = joins(lineList[:lineList.index('is')-1]); assignment = joins(lineList[lineList.index('is')+2:]); 
		print 'defining..,',var,"is",assignment; ISD[var] = {'noun':{'mydef':assignment}}; print ISD[var]; printV('ISD'); printl(); return 
	if '=' in lineList: 
		var = joins(lineList[:lineList.index('=')-1]); assignment = joins(lineList[lineList.index('=')+2:]); 
		print 'defining..,',var,"=" ,assignment; ISD[var] = {'noun':{'mydef':assignment}}; print ISD[var]; printV('ISD'); printl(); return 
	#### imperative, conditional or query must be indicated by first word
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
	elif kw == "what": pass
		
		
		
		
	#####################################
	############ compute ***IMPERATIVE*** statements - verb + args
	#elif kw in ISD.keys() and 'verb' in ISD[kw].keys() and 'mydef' in ISD[kw]['verb'].keys(): 
	elif ifKeysReturnValueISD(kw,'verb','mydef'): 
		global args; global count; ## puts local into globals or makes variable global
		imperativeList = lineList; count=0
	#### parse args
		args = string.join(imperativeList[2:],'') #args = sliceArgs(imperativeList)
		if verbose: print 'args0:',; printV('args')#; printl()
	#### evaluate words for known definitions ############################################
		for index,item in enumerate(imperativeList):
			if ifKeysReturnValueISD(item,'noun','mydef'): 
				item0 = item; item = ISD[item]['noun']['mydef']; 
				if imperativeList[index-1] == "\\": continue
				if item != 'something': imperativeList[index] = item; print 'defined1..',item0,':with:',item
				if verbose: print imperativeList[index] #global item; printV("item","args")
	#####################################
		def computeImperative(imperativeList):
	#### evaluate words for known definitions ############################################
			for index,item in enumerate(imperativeList):
				if ifKeysReturnValueISD(item,'noun','mydef'): 
					item0 = item; item = ISD[item]['noun']['mydef']; 
					if imperativeList[index-1] == "\\": continue
					if item != 'something': imperativeList[index] = item; print 'defined2..',item0,':with:',item
					if verbose: print imperativeList[index] #global item; printV("item","args")
			def printv(stringA): 
				if verbose: print stringA
			def printvv(stringA): 
				if verbose: ev = eval(stringA); print stringA, ev
		#### break infinite loops at certain depth
			global count; count=count+1; ## puts global into locals
			if count > 7: exit()
			global verb; global args; #global definition; global verbDef;
			if verbose: print('imperativeList:',imperativeList) #printV('imperativeList')
		#### parse verb
			verb = imperativeList[0]; verbIndex = imperativeList.index(verb); printV('verb')
		#### parse args
			#### copy original args
			global args0; args0 = args; #printV('args0')
			#if args: args0 = args;
		#### try execute definition with verb definitions and args 
		############ parse imperative statements - verb + args ## sentence structure VO verb-object
			if verb in ISD.keys(): 
			#### execute if not multiple defintion and therefore loop
				if len(ISD[verb]['verb']['mydef']) == 1: 
					printv('single')
				#### evaluate conditionals
					if verb == 'if':
						printv('if'); condition = joins(imperativeList[2:imperativeList.index(":")]); print 'condition:', condition, '..is..', eval(condition)
						if eval(condition): definitionL = imperativeList[imperativeList.index(":")+2:]; print 'eval',definitionL; computeImperative(definitionL)
						else: print 'not'; return
				#### replace 'something' in definitions
					if 'something' in verbDef: 
						verbDef = verbDef.replace("something",args); print 'replaced "something" with', args
					#### recurse if definition is recursive
					if verb != 'exec':
					
					#### define..	
						verbDef = ISD[verb]['verb']['mydef'][0]; print 'verbDef:', verbDef #printvv('verbDef')
						print 'recurse'; verbDefL = re.split('(\W)', verbDef); computeImperative(verbDefL)
						
					if verb == 'exec':
					#### execute if definition is not recursive
						print 'executing..',verbDef ## this will fail if verbDef is not defined because of multiple definitions	
						try: 
							print repr(verbDef)
							#exec(repr(verbDef)) in locals()
							exec(verbDef) in globals(), locals(); ### not secure(?)
						except NameError, exception: 
							verbDef = verbDef.replace(args,repr(args)); print 'trying..', verbDef
							try: 
								exec(verbDef) in globals(), locals(); ### not secure(?)
							except Exception,exception: print 'myerror: exec2: '+str(exception)
						except Exception, exception: print 'myerror: myexec: '+str(exception)
			#### loop through verb definitions list and execute with original args
				if len(ISD[verb]['verb']['mydef'])>1:
					print 'multiple'
					for index,definition in enumerate(ISD[verb]['verb']['mydef']): 
						print index; #printvv('definition') #if verbose: print 3,definitionL
						definitionL = re.split('(\W)', definition); definitionL = [i for i in definitionL if i != ""] 
						try: 
							computeImperative(definitionL)
						except Exception,e: print 'myerror: multiple '+str(e)
		computeImperative(imperativeList)
	#####################################
						

		
	elif kw == 'quit': 
		print 'noodle: ',noodle
		print 'ISD: ',ISD 
		input = raw_input("save?"); saveD() if input == 'y' else None; exit()
	elif kw not in ISD.keys(): print "I don't know how to.. "+kw
	else: print "I don't know what.. "+kw+" ..is"
	#globals().update(locals())
	# if response:
		# for x,i in enumerate(response):
			# response = i; print response; printV('response')
			# if tts: print 'speaking.. '; exec(responseChannel) in locals(),globals() 
		# response = []
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
		try:
			import pyttsx
		except ImportError,e: print str(e)
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-25)
		#engine.say('test'); engine.runAndWait()
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
	for index,line in enumerate(inputList):
		main(line)
## do input from user
	line=None
	#while line != 'q':
	#response = 'hi'; exec(responseChannel); response = []; 
	prompt = '>'
	#main("say hello")
	while not line:
		#line = raw_input("?"); #print line
		exec(channel)
		if input is None: time.sleep(7); print 'input is None';
		else: line = main(input)
	
'''

'''						