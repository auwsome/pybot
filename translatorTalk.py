'''
Table of contents

imports 
isD starting definition

'''
print "init translator"
## imports
#import translated
#import nltk
import sys, re, json, operator, string
try:
	import pyttsx
	from Pybot import responseChannel, engine
	# engine.say('test'); engine.runAndWait()
	# responseChannel = 'engine.say(response); engine.runAndWait()'
	# response = 'test'; exec(responseChannel)
except ImportError,e: print str(e)
#from pyDatalog import pyDatalog
'''
from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags'''


global isD; isD = {}
global verbose; verbose = True
## wont exec args as is, args always parsed to something
isD = {
"write"		: { "verb": {"mydef": [["print something"], "scrawl"]  }},
"return"	: { "verb": {"mydef": [["return something"], ""]  }},
"result"	: { "verb": {"mydef": [["result something"], ""]  }},
"shout"		: { "verb": {"mydef": [["write something","write '!!!'"], "yell"]}},
"dict"	: {"noun": {"mydef": "isD"} }, 
"tts"	: {"noun": {"mydef": "True"} },
"verbose"	: {"noun": {"mydef": "True"} }
}; isD0 = isD
#isSD = re.sub("(\w+)", "'"+"\\1"+"'", isS); ## adds quotes around single words
# a.setdefault("somekey",[]).append("bob")
print 'isD: ',isD 

## global variables
global pythonVerbs; pythonVerbsString = 'print,exec,operator.add(something,b)'; pythonVerbs = pythonVerbsString.split(","); print pythonVerbs
global verbsL; verbsString = 'write,make,create'; verbsL = verbsString.split(","); #print verbs
global prepositions; prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")
global functionD; functionD = {}; 

## helper functions
def addQuotes(stringA): return "'"+stringA+"'"
def sliceAt(stringA, slicePoint): return stringA[stringA.index(slicePoint)+len(slicePoint):]
def joins(listA): return "".join(listA)
def joins_(listA): return " ".join(listA)
def splits(stringA): return stringA.split(" ")
def printA(item): print item+":",eval(item)
#def ifNotNoneReturnIt(thing): if thing: return thing;  else: return None
def ifKeyNotNoneReturnIt(dictA,keyA): 
	if keyA in dictA.keys(): return dictA[keyA]  
	else: return None
def ifItemReturnIt(container,index): return container[index] if len(container)>=index else None
def ifKeyReturnValue(keyA, dictA): return ifKeyNotNoneReturnIt(dictA,keyA) ## check if dict has key and return it
#def ifKeyReturnValue(keyA, dictA): return dictA[keyA] if dictA[keyA] in dictA.keys() else None ## check if dict has key and return it
def ifKeyReturnValueD(keyA, dictA=isD): return ifKeyNotNoneReturnIt(dictA,keyA) ## check if dict has key and return it
#def ifKeyReturnValueD(keyA, dictA=isD): return dictA[keyA] if dictA[keyA] in dictA.keys() else None ## check if dict has key and return it
def ifKeysReturnValue(dict0=isD, *args): ## check if dict has key and return it
	value = dict0
	for key in args: 
		value = ifKeyReturnValue(key,isD)#value); ##################
		return value if not isinstance(value, dict) else None
def returnDeepest(): 
	if args[0] in isD.keys():
		if len(args)>1 and args[1] in isD[args[0]].keys():
			if len(args)>2 and args[2] in isD[args[0]][args[1]].keys(): return isD[args[0]][args[1]][args[2]]
			else: return isD[args[0]][args[1]] 
		else: return isD[args[0]]
	else: return None
	#return (isD[args[0]][args[1]][args[2]] if args[2] in isD[args[0]][args[1]].keys() else   (isD[args[0]][args[1]] if args[1] in isD[args[0]].keys() else   (isD[args[0]] if args[0] in isD.keys() else None)))
	#return (3 if 3>3 else   (2 if 2>2 else   (1 if 1>0 else None)))x

	#except Exception as e: print type(e).__name__, e.args
	#
	
## initialization functions
def getFile(file): f = open(file,"rb"); return f.read(); f.close() 
def writeFile(file): f = open(file,"wb"); return f.read(); f.close()
def getFileLines(file): f = open(file,"rb"); return f.readlines(); f.close()
def getInstructions(): return getFileLines("pseudocode.py")
if 'arm' in sys.platform: dName = '/storage/sdcard1/isD.json'
else: dName = "isD.json"
def rememberD(dict1): 
	with open(dName) as json_file: dict1 = json.load(json_file) 
def remindNoodle(): return getFile("noodle.txt")
def remindNoodleJ(): return json.loads("noodle2.py")
def dictionaryNoodle(noodle): 
	for line in noodle: 
		if line.startswith("to"): verbDef = line[:line.index(",")]; functionString = line[line.index(",")+1:]; functionD[verbDef] = functionString
	return functionD
def getInput(): exec('print 1')
#return 1 if n <= 1 else n*f(f,n-1)
# if sys.platform = '': is[write] = (v,)
def saveD(dict1): json.dump(isD, dName)
# class Bunch(object):
  # def __init__(self, adict):
    # self.__dict__.update(adict)
# x = Bunch(isD); print x.write

rememberD(isD)
## main
def main(line):	
	global tts;  global response; 
	response = []
	#if verbose: 
	verbose = False #bool(ifKeysReturnValue("verbose",'noun','mydef')); print 1; printA('verbose'); print verbose
	# if verbose == "False": verbose = False#True#
	# if verbose == "True": verbose = True
	tts = True#bool(ifKeysReturnValue("tts",'noun','mydef'))
	#if isD["verbose"] == {'noun':"True"}:  verbose = True#
	if verbose: print 'verbose', sys.platform; print isD; print 'tts:',tts
## remind verb/function definitions
	noodle = remindNoodle()
	global verbD; verbD = dictionaryNoodle(noodle); #print verbD
	#global isD; #isD = remindNoodleJ(); 
	#line = formatLine(line); 	## parse line
	if line.startswith("#"): return ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); # print line ## clean up line
	if line == '': return #if line: continue
	#line = line.strip("\n").strip("\r"); print line ## clean up line, leave tabs
#### find strings
	'''global strings; strings = re.findall(r"\'(.+?)\'",line); #print strings 
	for index,string in enumerate(strings): ## replace strings with list item
		line = line.replace(line[line.index(string)-1:line.index(string)+len(string)+1], strings[index]) #print 2,strings[index]#'''
	if line and verbose: print '=line: ',line ############
	if not line: return 
#### check for contractions and split imperative clauses
	# if 'and' or 'then' in line:	
		# lineSplit = line.split("and").split("then")
		# line[line.index()]
		# for line in lineSplit:
	#lineList = line.split(" ",",")## split into list
	#line = line.lower() ####
	#lineList = re.split('(\W+)', line); lineList = [i for i in lineList if i != " "] #print lineList ##########
	global lineList; lineList = re.split('(\W)', line); lineList = [i for i in lineList if i != ""]
	if verbose: print '=lineList: ',lineList ########
##################### there is an order of operations: check/set variables, check standard definitions, check conditionals (simple definitions), compute queries, compute imperatives 
	kw = lineList[0]; 
	if verbose: print 'kw=',kw ### imperative, conditional or query must be indicated by first word
	if not kw: print 'no keyword'
	############ check/set for variable definition
	## check for variables as keys
	elif ifKeysReturnValue(line,'noun','mydef'): 
		if verbose: print ifKeysReturnValue(line,'noun','mydef')
		response=[isD[line]['noun']['mydef']]; #response.append(isD[line])
		if response[0] == 'isD': print response; #response[0] = isD
	## set variables as key and values
	elif 'is' in lineList: var = joins(lineList[:lineList.index('is')-1]); assignment = joins(lineList[lineList.index('is')+2:]); print var,"is",assignment; isD[var] = {'noun':{'mydef':assignment}}; exec('if verbose: print isD') in locals(),globals() ## print before assignment
	elif '=' in lineList: var = joins(lineList[:lineList.index('=')-1]); assignment = joins(lineList[lineList.index('=')+2:]); print var,"=",assignment; isD[var] = {'noun':{'mydef':assignment}}; exec('if verbose: print isD') in locals(),globals()  #global var; var = assignment #continue
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
		if verbose: print verb,2,ifKeyReturnValueD(verb)
		if ifKeyReturnValueD(verb): input = raw_input('do you want to add "%s"?' % verb)
		#if not ifKey(verb) or input == 'y': isD[verb] = {'verb': verbDefinitions}
		if not ifKeyReturnValueD(verb) or input == 'y': isD[verb] = {'verb': {'mydef':verbDefinitions}}; print 'entered.. ',isD[verb]
		if verbose: print 1,verbDefinition,2,verbDefinitions,3,isD[verb],4,verb
	############ test verb definitions or instructions
		#input = raw_input('do you want to test {%s}?' % verb)
		#if input == 'y': print 'testing.. ',isD[verb]; exec(
	############ check for conditionals
	#if "if" in line: 
	#if "but only if" in line: 
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
	############ check for query
	elif kw == "what":
		pass
	elif kw in pythonVerbs or (kw in isD.keys() and 'verb' in isD[kw].keys()): 
		imperativeList = lineList
		global args; #args = None
		## parse args
		args = string.join(imperativeList[2:],''); #print('args0: ',args) if verbose else "",
		args = isD[args]['noun']['mydef'] if args in isD.keys() and 'noun' in isD[args].keys() else args
		if verbose: print('args0: ',args) 
		#if strings: something = 'strings[0]'; #print 'o',object1,eval(object1) #############
	############ compute imperative statements - verb + args
		#def computeImperative(verb, *args=None):
		def computeImperative(imperativeList):
			locals().update(globals())
			global args#, response ######??
			if verbose: print imperativeList  ########
			
		############ parse imperative statements - verb + args
		## parse verb
		## sentence structure VO verb-object
			verb = imperativeList[0]
			verbIndex = imperativeList.index(verb); #subject = lineList[:verbIndex]; # print subject ## find if subject
		## parse args
			if args: pass #print('args: ',args) if verbose else "",
			else: #args = string.join(imperativeList[verbIndex+1:],''); #print 'args2: ',args
				args = isD[args]['noun']['mydef'] if args in isD.keys() and 'noun' in isD[args].keys() else string.join(imperativeList[verbIndex+1:],'')
			if verbose: print('args1: ',args) 
			#if args in isD.keys(): args = isD[args]['noun'] if 'noun' in isD[args].keys() 
				#if 'noun' in isD[args].keys(): args = isD[args]['noun']; #print 'args3: ',args
		## join verb and args
			definition = string.join([verb, args],' ');
			if verbose: print 'verb',verb,'args',args,'interp:',definition
		## try execute definition with Python functions and args defined as string above or in definition
			if verb in pythonVerbs:
			## ask to execute
				input = 'y'# raw_input("try: "+definition+" ?")
				if input == 'y':	
					try: 
						interpretation = string.join([verb+"("+args+")"],''); print 'interp:',interpretation 
						exec(interpretation) in globals(), locals();  ################################### not secure
						if tts: response.append(args); globals().update(locals()); #print args; print 1345623,response
						#if tts: response = args; globals().update(locals()); #print args; print 1345623,response
						#if verbose: printA('response[0]')#print 'response',response
					except Exception,e: 
						print 'error exec Python verb: '+str(e)
		## try execute definition with verb definitions and args 
			if verb in isD.keys():
				if type(isD[verb]['verb']['mydef'][0]) is not list: print 'verb is not executable'
		## loop through definitions and execute with args
				for index,definition in enumerate(isD[verb]['verb']['mydef'][0]): 
					if verbose: print index#,definition #############
					if verbose: print '=definition:',definition ###########
					try: 
						definitionL = definition.split(" "); 
						if verbose: print definitionL
						if "=" in definition: pass
						else: computeImperative(definitionL)
					except Exception,e: 
						print 'error exec verb 1: '+str(e)
		computeImperative(imperativeList)
									
	elif kw == 'quit': 
		print 'noodle: ',noodle
		print 'isD: ',isD 
		input = raw_input("save?"); saveD() if input == 'y' else None; exit()
	elif kw not in isD.keys(): print "I don't know how to.. "+kw
	else: print "I don't know what.. "+kw+" ..is"
	#globals().update(locals())
	if response:
		#print 1; printA('response')
		for x,i in enumerate(response):
			if not tts: print i 
			if tts and response: print 'speaking.. ',i; exec(responseChannel) in locals(),globals() 
			response = None
			
			
def saveD(dict1=isD):
	with open("isD.json", 'wb+') as file: file.write(json.dumps(isD, indent=4, sort_keys=True))  ## w+ = wr and overwrite
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
## do input from instructions
	inputList = getInstructions(); #print input
	#for index,line in enumerate(inputList):
		#main(line)
## do input from user
	line=None
	while line != 'q':
		line = raw_input("?"); #print line
		main(line)
	
'''

'''						