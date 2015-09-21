#import translated
import nltk, re

from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags

global verbsL; verbsString = 'write,make,create'; verbsL = verbsString.split(","); #print verbs
global prepositions; prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")
global functionD; functionD = {}; 

def getFile(file): f = open(file,"rb"); return f.readlines(); f.close()
def getInstructions(): return getFile("pseudocode.py")
def remindNoodle(): return getFile("noodle.txt")
def dictionaryNoodle(noodle): 
	for line in noodle: 
		if line.startswith("to"): verbDef = line[:line.index(",")]; functionString = line[line.index(",")+1:]; functionD[verbDef] = functionString
	return functionD
def getInput(): exec('print 1')
#return 1 if n <= 1 else n*f(f,n-1)

def main():	
	## remind verb/function definitions
	noodle = remindNoodle()
	global verbD; verbD = dictionaryNoodle(noodle)
	print verbD
			
	## learn instructions
	input = getInstructions(); #print input
	## do input
	
	for index,line in enumerate(input):
		line = formatLine(line); 
		print 'line: ',line
		if line == '' or line == None: continue; 
		## check for contractions and split imperative clauses
		# if 'and' or 'then' in line:	
			# lineSplit = line.split("and").split("then")
			# line[line.index()]
			# for line in lineSplit:
		#lineList = line.split(" ",",")## split into list
		lineList = re.split('(\W+)', line); print lineList
		## order of operations
		## check for conditionals and learn them
		if "if" in line: 
			print line
			conditionalL = lineList[lineList.index('if'):lineList.index(', ')-1]
			conditionL = conditionalL.remove("if"); 
			if conditionList[0] == "I":
				if conditionList[1] == "say":
					command = joins(lineList[2:lineList.index(', ')-1])
					instructionWhole = line[line.index(',')+1:]
					if 'then' in instructionWhole: instructionWhole = instructionWhole.lstrip("then ")
					verbD[command] = instructionWhole
		think(line)	
		
	## store noodle	
	remember(noodle)
		
def formatLine(line):
	## parse line
	if line.startswith("#"): return ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); print line ## clean up line
	#line = line.strip("\n").strip("\r"); print line ## clean up line, leave tabs
	## find strings
	global strings; strings = re.findall(r"\'(.+?)\'",line); #print strings 
	for index,string in enumerate(strings): ## replace strings with list item
		line = line.replace(line[line.index(string)-1:line.index(string)+len(string)+1], strings[index]) #print 2,strings[index]
	return line 

def think(line):
	lineList = line.split(" "); 
	## set variables
	global var
	if ' = ' in line: var = line[:line.index(' = ')]; assignment = line[line.index(' = ')+3:]; var = assignment;
	if ' is ' in line: var = line[:line.index(' is ')]; assignment = line[line.index(' is ')+3:]; var = assignment; #print var,1,assignment;
	
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
		else: object1 = lineList[verbIndex+1:] #print subject,object1
		if verb == 'write': 
			for preposition in prepositions:
				if preposition in lineList:
					#print 3,preposition
					prepositionIndex = lineList.index(preposition)
					object2 = lineList[prepositionIndex+1:]; print object2
					write(object1, preposition, " ".join(object2)); break
			write(" ".join(object1))
		if lineList[0] in functionD.keys():
			something = lineList[1:]

#def learn(instruction):
def evaluate(instructions):
	instructionsL = instructions.split(", ")
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
	
	
def remember(noodle):
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