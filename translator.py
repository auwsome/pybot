'''
Table of contents

imports 
isD starting definition

'''
## imports
#import translated
import nltk, re, json, operator
#from pyDatalog import pyDatalog

from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags

# isS = '''{
# write: { verb: [print, scrawl]  },
# shout: [(v,[[object1 = object1+"!"],[write]])],
# }'''
# isD = {
# 'write' :[  ('v','print'), ('v','scrawl')  ],
# }
isS = '''{
write: { verb: [[[print something]], scrawl]  },
shout: { verb: [[[object1 +'='+ object1+"!"],[write]], yell]},
'write'		: { 'verb': [["something = strings[0] if strings else lineList[verbIndex+1:[lineList.index(',') if lineList.index(',') else None]]",  'print something'], 'scrawl']  },

# }'''
# isD = {
# 'write'		: { 'verb': [["something = joins(lineList[verbIndex+1:])",'print something'], 'scrawl']  },
# 'write_string'	: { 'verb': [['something = strings[0]','write something'], 'scrawl']  },
# 'write_then'	: { 'verb': [["something = lineList[verbIndex+1:[lineList.index(',') if lineList.index(',') else None]]",  'print something'], 'scrawl']  },
# 'shout'		: { 'verb': [['something = strings[0]+"!"','write something'], 'yell']},
# }
isD = {
'write'		: { 'verb': [['print something'], 'scrawl']  },
'write_string'	: { 'verb': [['something = strings[0]','write something'], 'scrawl']  },
'write_then'	: { 'verb': [["something = lineList[verbIndex+1:[lineList.index(',') if lineList.index(',') else None]]",  'print something'], 'scrawl']  },
'shout'		: { 'verb': [['something = "!"','write something'], 'yell']},
}
isSD = re.sub("(\w+)", "'"+"\\1"+"'", isS); #print isSD
global isD; #isD = eval (isSD); #print isD
#global isD; isD = dict(isSD)
# a.setdefault("somekey",[]).append("bob")
print 'isD: ',isD #,isD['write'][0][0]

## global variables
global pythonVerbs; pythonVerbsString = 'print,operator.add(something,b)'; pythonVerbs = pythonVerbsString.split(","); print pythonVerbs
global verbsL; verbsString = 'write,make,create'; verbsL = verbsString.split(","); #print verbs
global prepositions; prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")
global functionD; functionD = {}; 

## helper functions
def addQuotes(string): return "'"+string+"'"
def sliceAt(string, slicePoint): return string[string.index(slicePoint)+len(slicePoint):]
def joins(list): return " ".join(list)
def splits(string): return string.split(" ")

## initialization functions
def getFile(file): f = open(file,"rb"); return f.readlines(); f.close()
def getInstructions(): return getFile("pseudocode.py")
def remindNoodle(): return getFile("noodle.txt")
#def remindNoodleJ(): return json.loads("noodle2.py")
def dictionaryNoodle(noodle): 
	for line in noodle: 
		if line.startswith("to"): verbDef = line[:line.index(",")]; functionString = line[line.index(",")+1:]; functionD[verbDef] = functionString
	return functionD
def getInput(): exec('print 1')
#return 1 if n <= 1 else n*f(f,n-1)
# if sys.platform = '': is[write] = (v,)

## main
def main():	
## remind verb/function definitions
	noodle = remindNoodle()
	global verbD; verbD = dictionaryNoodle(noodle); #print verbD
	#global isD; #isD = remindNoodleJ(); 
			
## do and learn from instructions
	input = getInstructions(); #print input
## do input
	
	for index,line in enumerate(input):
		#line = formatLine(line); 	## parse line
		if line.startswith("#"): continue ## ignore comments
		line = line.strip("\n").strip("\r").strip("\t"); # print line ## clean up line
		if line == '': continue #if line: continue
		#line = line.strip("\n").strip("\r"); print line ## clean up line, leave tabs
	#### find strings
		global strings; strings = re.findall(r"\'(.+?)\'",line); #print strings 
		for index,string in enumerate(strings): ## replace strings with list item
			line = line.replace(line[line.index(string)-1:line.index(string)+len(string)+1], strings[index]) #print 2,strings[index]
		#if line: print '=line: ',line ############
		if not line: continue 
	#### check for contractions and split imperative clauses
		# if 'and' or 'then' in line:	
			# lineSplit = line.split("and").split("then")
			# line[line.index()]
			# for line in lineSplit:
		#lineList = line.split(" ",",")## split into list
		line = line.lower()
		#lineList = re.split('(\W+)', line); lineList = [i for i in lineList if i != " "] #print lineList ##########
		def think(line):
			global lineList; lineList = re.split('(\W+)', line); lineList = [i for i in lineList if i != " "]
			print '=lineList: ',lineList ########
		##################### there is an order of operations: set varibles, check standard definitions, check conditionals (simple definitions), compute queries, compute imperatives 
			kw = lineList[0]; #print kw ### imperative, conditional or query must be indicated by first word
			if not kw: print 'no keyword'
		############ check for verb definitions or instructions
			elif kw == "to": 
				verbL = lineList[lineList.index("to"):lineList.index(",")]; #print verb; #print verbD[verb]
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
			elif 'is' in lineList: var = joins(lineList[:lineList.index('is')]); assignment = joins(lineList[lineList.index('is')+1:]); print var,"is",assignment ;var = assignment; #continue## print before assignment
			elif '=' in lineList: var = joins(lineList[:lineList.index('=')]); assignment = joins(lineList[lineList.index('=')+1:]); print var,"is",assignment; var = assignment; #continue
			
			############ check for conditionals
			#if "if" in line: 
			#if "but only if" in line: 
			elif kw == "if": 
				#print line
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
			elif kw in isD.keys() or kw in pythonVerbs: 
				imperativeList = lineList
				global something; something = None
				## parse args
				if strings: something = 'strings[0]'; #print 'o',object1,eval(object1) #############
			############ compute imperative statements - verb + args
				#def computeImperative(verb, *args=None):
				def computeImperative(imperativeList):
					global something ######??
						
				############ parse imperative statements - verb + args
				## parse verb
				## sentence structure VO verb-object
					verb = imperativeList[0]
					verbIndex = imperativeList.index(verb); #subject = lineList[:verbIndex]; # print subject ## find if subject
				## parse args
					if something: pass
					else: something = joins(imperativeList[verbIndex+1:])
				## join verb and args
					definition = joins([verb, something]); print 'def:',definition
				## try execute definition with Python functions and args defined as string above or in definition
					if verb in pythonVerbs:
					## ask to execute
						input = 'y'# raw_input("try: "+definition+" ?")
						if input == 'y':	
							try: 
								exec(definition) in globals(), locals() ################################### not secure
							except Exception,e: 
								print 'error exec Python verb: '+str(e)
				## try execute definition with verb definitions and args 
					if verb in isD.keys():
						if type(isD[verb]['verb'][0]) is not list: print 'verb is not executable'
				## loop through definitions and execute with args
						for index,definition in enumerate(isD[verb]['verb'][0]): 
							print index#,definition #############
							print '=definition:',definition ###########
							try: 
								definitionL = definition.split(" ")
								if "=" in definition: var = joins(definitionL[:definitionL.index('=')]); assignment = joins(definitionL[definitionL.index('=')+1:]); print var,"is",assignment; var = assignment;
								# definition = definitionL + args; print definition
								else: computeImperative(definitionL)
								# exec(definition) in globals(), locals() ################################### not secure
							except Exception,e: 
								print 'error exec verb 1: '+str(e)
				computeImperative(imperativeList)
											
			elif kw not in isD.keys(): print "I don't know how to.. "+kw
				#exit()
			else: print "I don't know what.. "+kw+" ..is"
			#else: print "???"
		think(line)
			
	print 'noodle: ',noodle
	input = 'n'#raw_input("save?")
	if input == 'n': exit()
	## store noodle	
	append(noodle)
		
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
	
	
def append(noodle):
	if functionD != verbD:
		for key,value in functionD.items():
			if functionD[key] not in verbD.keys():
				newInstruction = " ".join(['\n', key, value])
				with open("noodle.txt", 'ab') as file: file.write(newInstruction)
			elif verbD[key] != functionD[key]: print 'noodle line not the same'
	
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
	main()
	input = raw_input("")
	
'''

'''						