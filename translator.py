import translated
import nltk, re

from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags

global functionD; verbsString = 'write,make,create'; global verbs; verbs = verbsString.split(","); #print verbs
prepositionsString = 'in into over '; prepositions = prepositionsString.split(" ")

def getInstructions(): with open("pseudocode.py", 'rb') as file: return = file.readlines()
def remindNoodle(): with open("noodle.txt", 'rb') as file: return = file.readlines()
def dictionaryNoodle(noodle): for line in noodle: if line.startswith("to"): verbDef = line[:line.index(',')-1]; functionString = line[line.index(',')+1:]; functionD[verbDef] = functionString
def getInput(): exec('print 1')

def main():	
	## remind verb/function definitions
	noodle = remindNoodle()
	dictionaryNoodle(noodle); global noodleD; noodleD = functionD
			
	## learn instructions
	input = getInstructions()
	## do input
	
	for line in input:
		line = formatLine(line); if line == '': break; print line 
		## check for contractions and split imperative clauses
		if 'and' or 'then' in line:	
		lineSplit = line.split("and").split("then")
		for line in lineSplit:
		lineList = line.split(" ")## split into list
		## order of operations
			## check for conditionals and learn them
			if "if" in line: 
				conditionalL = lineList[lineList.index('if'):lineList.index(',')-1]
				conditionL = conditionalL.remove("if"); 
					if conditionList[0] == "I":
						if conditionList[1] == "say":
							command = joins(lineList[2:lineList.index(',')-1])
							instructionWhole = line[line.index(',')+1:]
							if 'then' in instructionWhole = : instructionWhole = instructionWhole.lstrip("then ")
							noodleD[command] = instructionWhole
			think(line)	
		
	## store noodle	
	remember(noodle)
		
def formatLine(line):
	## parse line
	if line.startswith("#"): break ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); print line ## clean up line
	#line = line.strip("\n").strip("\r"); print line ## clean up line, leave tabs
	## find strings
	strings = re.findall(r"\'(.+?)\'",line); #print strings 
	for index,string in enumerate(strings): ## replace strings with list items
		line = line.replace(line[line.index(string)-1:line.index(string)+len(string)+1], strings[index]) #print 2,strings[index]
	return line 

def think(line):
	lineList = line.split(" "); 
	## set variables
	if ' = ' in line: var = line[:line.index(' = ')]; assignment = line[line.index(' = ')+3:]; global var; var = assignment;
	if ' is ' in line: var = line[:line.index(' is ')]; assignment = line[line.index(' is ')+3:]; global var; var = assignment; #print var,1,assignment;
		
	## check for verbs (should be only one per imperative clause)
	for verb in noodle.keys():
		verb = verb.lstrip("to ").strip(" something")
		if verb in line:
			instructions = noodle[verb]; params = [:line.index(verb)+1]; evaluate(instructions, params)
		
	if lineList[0] in verbs:
		## sentence structure SVO
		#verbIndex = lineList.index(verb); subject = lineList[:verbIndex]; # print subject ## find if subject
		if strings: object1 = [strings[0]]
		else: object1 = lineList[verbIndex+1:] #print subject,object1
		if verb == 'write': 
			for preposition in prepositions:
				if preposition in lineList:
					#print 3,preposition
					prepositionIndex = lineList.index(preposition)
					object2 = lineList[prepositionIndex+1:]; print object2
					write(object1, preposition, " ".join(object2)); break
			write(" ".join(object1)); break
		if lineList[0] in functionD.keys():
			something = lineList[1:]

#def learn(instruction):
def evaluate(instructions):
	instructionsL = instructions.split(", ")
	for instruction in instructionsL:
		for verb in verbs:
			if verb
	
	
def remember(noodle):
	if functionD != noodleD:
		for key,value in functionD.items():
			if functionD[key] not in noodleD.keys():
				newInstruction = " ".join(['\n', key, value])
				with open("noodle.txt", 'ab') as file: file.write(newInstruction)
			elif noodleD[key] != functionD[key]: print 'noodle line not the same'
	
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