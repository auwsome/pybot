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
#from pyDatalog import pyDatalog
'''
from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags'''


global isD; 
## wont exec args as is, args always parsed to something
isD = {
'write'		: { 'verb': [['print something'], 'scrawl']  },
'return'		: { 'verb': [['return something'], 'scrawl']  },
'shout'		: { 'verb': [['write something','write "!!!"'], 'yell']},
'write_a'	: { 'verb': [['write a'], 'scrawl']  },
'write_then'	: { 'verb': [["1",  'print something'], 'scrawl']  },
'verbose'	: {'noun': {'def1': False} },
}
isD0 = isD
#isSD = re.sub("(\w+)", "'"+"\\1"+"'", isS); ## adds quotes around single words
# a.setdefault("somekey",[]).append("bob")
print 'isD: ',isD 

## global variables
global pythonVerbs; pythonVerbsString = 'print,operator.add(something,b)'; pythonVerbs = pythonVerbsString.split(","); print pythonVerbs
global verbsL; verbsString = 'write,make,create'; verbsL = verbsString.split(","); #print verbs
global prepositions; prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")
global functionD; functionD = {}; 

## helper functions
def addQuotes(string): return "'"+string+"'"
def sliceAt(string, slicePoint): return string[string.index(slicePoint)+len(slicePoint):]
def joins(list): return "".join(list)
def joins_(list): return " ".join(list)
def splits(string): return string.split(" ")
def ifKey(*args): ## check if dict has key and return it
	if args[0] in isD.keys():
		if args[1] in isD[args[0]].keys():
			if args[2] in isD[args[0]][args[1]].keys(): return isD[args[0]][args[1]][args[2]]
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


## main
def main(line):	
	rememberD(isD)
	#if verbose: 
	print isD
	verbose = ifKey("verbose",'noun','def1')
	if verbose == "False": verbose = False#True#
	if verbose == "True": verbose = True
	#if isD["verbose"] == {'noun':"True"}:  verbose = True#
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
##################### there is an order of operations: set varibles, check standard definitions, check conditionals (simple definitions), compute queries, compute imperatives 
	kw = lineList[0]; 
	if verbose: print 'kw=',kw ### imperative, conditional or query must be indicated by first word
	if not kw: print 'no keyword'
############ check for verb definitions or instructions
	elif kw == "to": 
		verbL = lineList[lineList.index("to"):lineList.index(",")]; #if verbose: print verb; #print verbD[verb]
		if 'something' in verbL: needsParams = True; verb = verbL.remove('something')
		verbDefinition = [lineList[lineList.index(",")+1:]]
		verbDefinitions = [[]]
		[verbDefinitions.append([i]) if i == "," else verbDefinitions[-1].append(i) for i in verbDefinition]
		if isD[verb] is not None: 
			input = raw_input('do you want to add this verb?')
		if isD[verb] is None or input == 'y':
			isD[verb] = verbDefinitions
	############ test verb definitions or instructions
		''' trying to evaluate definition before adding but would need to run through 'think' function 
		def addVerbDefintion(verb, verbDefinition):
			verbDefinition[0] = verb2
			if isD[verb2][0][0] == 'v': continue
			else: print "I don't know how to: "+verb2 
				verbDefined = verbDefinition[0]
			print eval(verbDefined)
			isD[verb] = verbDefined
		addVerbDefintion(verbDefinition)
		if verb in line: 
			instructions = verbD[verb]; params = line[:line.index(verb)+1];
			evaluate(instructions, params)
		evaluate(lineList)'''
	############ check for variable definition
	## set variables
	elif 'is' in lineList: var = joins(lineList[:lineList.index('is')-1]); assignment = joins(lineList[lineList.index('is')+2:]); print var,"is",assignment; isD[var] = {'noun':{'def1':assignment}}; exec('if verbose: print isD') in locals(),globals() ## print before assignment
	elif '=' in lineList: var = joins(lineList[:lineList.index('=')-1]); assignment = joins(lineList[lineList.index('=')+2:]); print var,"=",assignment; isD[var] = {'noun':{'def1':assignment}}; exec('if verbose: print isD') in locals(),globals()  #global var; var = assignment #continue
	
	
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
		args = isD[args]['noun']['def1'] if args in isD.keys() and 'noun' in isD[args].keys() else args
		if verbose: print('args0: ',args) 
		#if strings: something = 'strings[0]'; #print 'o',object1,eval(object1) #############
	############ compute imperative statements - verb + args
		#def computeImperative(verb, *args=None):
		def computeImperative(imperativeList):
			global args ######??
			if verbose: print imperativeList  ########
			
		############ parse imperative statements - verb + args
		## parse verb
		## sentence structure VO verb-object
			verb = imperativeList[0]
			verbIndex = imperativeList.index(verb); #subject = lineList[:verbIndex]; # print subject ## find if subject
		## parse args
			if args: pass #print('args: ',args) if verbose else "",
			else: #args = string.join(imperativeList[verbIndex+1:],''); #print 'args2: ',args
				args = isD[args]['noun']['def1'] if args in isD.keys() and 'noun' in isD[args].keys() else string.join(imperativeList[verbIndex+1:],'')
			if verbose: print('args1: ',args) 
			#if args in isD.keys(): args = isD[args]['noun'] if 'noun' in isD[args].keys() 
				#if 'noun' in isD[args].keys(): args = isD[args]['noun']; #print 'args3: ',args
		## join verb and args
			definition = string.join([verb, args],' ');
			if verbose: print 'interp:',definition
		## try execute definition with Python functions and args defined as string above or in definition
			if verb in pythonVerbs:
			## ask to execute
				input = 'y'# raw_input("try: "+definition+" ?")
				if input == 'y':	
					try: 
						exec(definition) in globals(), locals();  ################################### not secure
					except Exception,e: 
						print 'error exec Python verb: '+str(e)
		## try execute definition with verb definitions and args 
			if verb in isD.keys():
				if type(isD[verb]['verb'][0]) is not list: print 'verb is not executable'
		## loop through definitions and execute with args
				for index,definition in enumerate(isD[verb]['verb'][0]): 
					if verbose: print index#,definition #############
					if verbose: print '=definition:',definition ###########
					try: 
						definitionL = definition.split(" "); 
						if verbose: print definitionL
						if "=" in definition: pass
							# var = joins(definitionL[:definitionL.index('=')]); assignment = joins(definitionL[definitionL.index('=')+1:]); print var,"=",assignment; var = assignment; isD[args]['noun'] = assignment
							# print 11
							# exec('global a') in globals(), locals()
							# print 111
							# print var; print a
						# definition = definitionL + args; print definition def
						else: computeImperative(definitionL)
						# exec(definition) in globals(), locals() ################################### not secure
					except Exception,e: 
						print 'error exec verb 1: '+str(e)
		computeImperative(imperativeList)
									
	elif kw == 'quit': 
		print 'noodle: ',noodle
		print 'isD: ',isD
		#print json.dumps(isD, indent=4, sort_keys=True)
		input = raw_input("save?")
		if input == 'y': 
			saveD(isD)
		## store noodle	
			# append(noodle); 
		exit()
	elif kw not in isD.keys(): print "I don't know how to.. "+kw
	else: print "I don't know what.. "+kw+" ..is"
	#else: print "???"
			
'''		
def formatLine(line):
	## parse line
	if line.startswith("#"): return ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); # print line ## clean up line
	#line = line.strip("\n").strip("\r"); print line ## clean up line, leave tabs
	## find strings
	global strings; strings = re.findall(r"\'(.+?)\'",line); #print strings 
	for index,string in enumerate(strings): ## replace strings with list item
		line = line.replace(line[line.index(string)-1:line.index(string)+len(string)+1], strings[index]) #print 2,strings[index]
	return line 
'''
# def imperative(lineList):
	#lineList = line.split(" "); 
	#lineList = re.split('(\W+)', line); #print lineList
	#kw = lineList[0]
		# if verb == 'write': 
			# for preposition in prepositions:
				# if preposition in lineList:
					##print 3,preposition
					# prepositionIndex = lineList.index(preposition)
					# object2 = lineList[prepositionIndex+1:]; print object2
					# write(object1, preposition, " ".join(object2)); break
			# write(" ".join(object1))
		# if lineList[0] in functionD.keys():
			# something = lineList[1:]
			

# def evaluate(instructionsL):
	#instructionsL = instructions.split(", ")
	# for instruction in instructionsL:
		# for verb in verbsL:
			# if verb in instructionsL: verb1 = verb
		# for preposition in prepositions:
			# if preposition in instructionsL: preposition1 = preposition;
		# if preposition1: 
			# object1 = instructionsL[instructionsL.index(verb1):instructionsL.index(preposition1)]
			# object2 = instructionsL[instructionsL.index(preposition1):]
		# else: object1 = instructionsL[instructionsL.index(verb1):]
		# look up verb function, if includes another verb, look that up - recursive
	
	
# def append(noodle):
	# if functionD != verbD:
		# for key,value in functionD.items():
			# if functionD[key] not in verbD.keys():
				# newInstruction = " ".join(['\n', key, value])
				# with open("noodle.txt", 'ab') as file: file.write(newInstruction)
			# elif verbD[key] != functionD[key]: print 'noodle line not the same'
def saveD(dict1):
	# if isD != isD0:
		# for key,value in isD.items():
			# if isD[key] not in isD.keys():
				# newInstruction = " ".join(['\n', key, value])
	with open("isD.json", 'wb') as file: file.write(newInstruction)
			# elif verbD[key] != functionD[key]: print 'noodle line not the same'
	
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