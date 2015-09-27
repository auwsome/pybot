#import translated
import nltk, re, json
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
write: { verb: [[[print]], scrawl]  },
shout: { verb: [[[object1 +'='+ object1+"!"],[write]], yell]},
}'''
isD = {
'write': { 'verb': [[['print something']], 'scrawl']  },
'shout': { 'verb': [[['object1 = object1'],['write something']], 'yell']},
}
isSD = re.sub("(\w+)", "'"+"\\1"+"'", isS); #print isSD
global isD; #isD = eval (isSD); #print isD
#global isD; isD = dict(isSD)
# a.setdefault("somekey",[]).append("bob")
print 'isD: ',isD #,isD['write'][0][0]

global verbsL; verbsString = 'write,make,create'; verbsL = verbsString.split(","); #print verbs
global prepositions; prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")
global functionD; functionD = {}; 

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

def main():	
	## remind verb/function definitions
	noodle = remindNoodle()
	global verbD; verbD = dictionaryNoodle(noodle); #print verbD
	#global isD; #isD = remindNoodleJ(); 
			
	## do and learn from instructions
	input = getInstructions(); #print input
	## do input
	
	for index,line in enumerate(input):
		line = formatLine(line); 
		#if line: print 'line: ',line
		if line == '' or line == None: continue; 
		#if line: continue; 
		print 'line: ',line
		## check for contractions and split imperative clauses
		# if 'and' or 'then' in line:	
			# lineSplit = line.split("and").split("then")
			# line[line.index()]
			# for line in lineSplit:
		#lineList = line.split(" ",",")## split into list
		line = line.lower()
		lineList = re.split('(\W+)', line); #print lineList ##########
		lineList = [i for i in lineList if i != " "]
		############################################# order of operations 
		kw = lineList[0] ### imperative, conditional or query must be indicated by first word
		############ check for variable definition
		## set variables
		# if ' = ' in line: var = line[:line.index(' = ')]; assignment = line[line.index(' = ')+3:]; var = assignment;
		# if ' is ' in line: var = line[:line.index(' is ')]; assignment = line[line.index(' is ')+3:]; var = assignment; #print var,1,assignment;
		if 'is' in lineList: var = joins(lineList[:lineList.index('is')]); assignment = joins(lineList[lineList.index('is')+1:]); print var,"is",assignment ;var = assignment; continue## print before assignment
		if '=' in lineList: var = joins(lineList[:lineList.index('=')]); assignment = joins(lineList[lineList.index('=')+1:]); print var,"is",assignment; var = assignment; continue
		
		############ check for conditionals
		#if "if" in line: 
		#if "but only if" in line: 
		if kw == "if": 
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
			
			'''else: 
			lineList[lineList.index(",")+1:]
			#`for count in verbDefinition.count(","):
			verbDefinition
			#def addVerbDefintion(verb, verbDefinition):
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
		############ check for query
		elif kw == "what":
			pass
					
		else: 
		############ compute imperative
			def computeImperative():
				#print 1,isD.keys(),2,kw #######
				if kw in isD.keys():
					#print 'in keys',isD[kw][0][1] ##########
					if isD[kw]['verb'][0] is not None:
						## sentence structure SVO
						verb = kw; #print 'verb: ',verb, type(isD[kw]['verb'][0][0]); #############
						verbIndex = lineList.index(verb); #subject = lineList[:verbIndex]; # print subject ## find if subject
						if strings: object1 = 'strings[0]'; #print 'o',object1 #############
						else: object1 = lineList[verbIndex+1:];  #print subject,object1
						print 'obj:',object1
						if type(isD[kw]['verb'][0][0]) is list: verbIsExecutable = True
						else: print 'verb is not executable'
						if verbIsExecutable:
							input = 'y'#raw_input("try: "+isD[kw][0][1]+" "+object1+"?")
							if input == 'y':
							
								# def execVerb(verb):	
									# print object1 in globals(), locals()
									# try: 
										# object1 = object1+"!"; print object1
										# exec(verb+" "+object1) in globals(), locals() ################################### not secure
									# except Exception,e: print 'error exec verb: '+str(e)
								#def execVerb(verb):	exec(verb+" "+object1)				
								#exec("def execVerb(verb):\n\t try:\n\t\t exec(verb+" "+object1)\n\t\t except: print 'error exec verb'")
								
								if type(isD[kw]['verb'][0][0]) is list:								
								#if isD[kw]['verb'][0][0][0] is not None:		
									#for x,i in enumerate(isD[kw]['verb'][0][0]): execVerb(isD[kw]['verb'][0][0][x])
									for x,i in enumerate(isD[kw]['verb'][0][0]): 
										print x,i
										try: 
											#object1 = object1+"!"; 
											print verb+" "+object1
											exec(verb+" "+object1) in globals(), locals() ################################### not secure
										except Exception,e: print 'error exec verb: '+str(e)
										#execVerb(isD[kw]['verb'][0][0][x]); #print 'multiple definition verb'	
								# elif type(isD[kw]['verb'][0][0]) is list:	
									# execVerb(isD[kw]['verb'][0][0]); print 'single definition verb', isD[kw]['verb'][0][0]
					else: print "I don't know how to.. "+kw
				else: print "I don't know what.. "+kw+" ..is"
			computeImperative()
			#exit()
	
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

def imperative(lineList):
	#lineList = line.split(" "); 
	#lineList = re.split('(\W+)', line); #print lineList
	kw = lineList[0]
	'''
	#print 1,isD.keys(),2,kw #######
	if kw in isD.keys():
		#print 'in keys',isD[kw][0][1] ##########
		if isD[kw][0][0] == 'v':
			## sentence structure SVO
			verb = kw; #print 'verb: ',verb; #############
			verbIndex = lineList.index(verb); #subject = lineList[:verbIndex]; # print subject ## find if subject
			if strings: object1 = 'strings[0]'; #print 'o',object1 #############
			else: object1 = lineList[verbIndex+1:] #print subject,object1
			input = raw_input("try: "+isD[kw][0][1]+" "+object1+"?")
			if input == 'y':
				try: 
					exec(isD[kw][0][1]+" "+object1)
				except: print 'error exec verb'
	else: print "I don't know how to "+kw
	'''
	'''
	if lineList[0] in verbD.keys():
	## check for verbs (should be only one per imperative clause)
	#for verb in verbD.keys():
		verb = lineList[0]; print 'verbD: ',verb;
		verb = verb.lstrip("to ").strip(" something"); print verb; print verbD[verb]
		if verb in line: instructions = verbD[verb]; params = line[:line.index(verb)+1]; evaluate(instructions, params)
		
	if lineList[0] in verbsL:
		## sentence structure SVO
		verb = lineList[0]; print 'verbL: ',verb;
		verbIndex = lineList.index(verb); #subject = lineList[:verbIndex]; # print subject ## find if subject
		if strings: object1 = [strings[0]]
		else: object1 = lineList[verbIndex+1:] #print subject,object1'''
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
			

#def learn(instruction):
def evaluate(instructionsL):
	#instructionsL = instructions.split(", ")
	for instruction in instructionsL:
		for verb in verbsL:
			if verb in instructionsL: verb1 = verb
		for preposition in prepositions:
			if preposition in instructionsL: preposition1 = preposition;
		if preposition1: 
			object1 = instructionsL[instructionsL.index(verb1):instructionsL.index(preposition1)]
			object2 = instructionsL[instructionsL.index(preposition1):]
		else: object1 = instructionsL[instructionsL.index(verb1):]
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

def addQuotes(string): return "'"+string+"'"
def sliceAt(string, slicePoint): return string[string.index(slicePoint)+len(slicePoint):]
def joins(list): return " ".join(list)
def splits(string): return string.split(" ")
	
# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
	main()
	input = raw_input("")
	
'''

'''						