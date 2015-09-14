import translated
import nltk, re

from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags

verbsString = 'write make create'; verbs = verbsString.split(" "); #print verbs
prepositionsString = 'in into over '; prepositions = prepositionsString.split(" ")

def getInstructions(): with open("pseudocode.py", 'rb') as file: return = file.readlines()
def remindNoodle(): with open("noodle.txt", 'rb') as file: return = file.readlines()
def dictionaryNoodle(noodle): 
	global functionD
	for line in noodle:
		if line.startswith("to"):
			verb = " ".join(line[0:lineList.index(',')-1]); verbs.append(verb)
			functionS = lineList[lineList.index(','):]; functionL = functionS.split(", "); functionD[verbDef] = functionL
			return functionD
def getInput(): exec('print 1')

def main():	
	## remind verb/function definitions
	noodle = remindNoodle()
	global noodleD; noodleD = dictionaryNoodle(noodle)
			
	## learn instructions
	for line in getInstructions():
		print line #'lineList>',lineList
		lineList = formatLine(line); if lineList == '': break
		think(lineList)		
		
	## do input
	# for line in getInput():
		# print line #'lineList>',lineList
		# lineList = formatLine(line); if lineList == '': break
		# think(lineList)		
		
def formatLine(line):
	## parse line
	if line.startswith("#"): break ## ignore comments
	line = line.strip("\n").strip("\r").strip("\t"); print line ## clean up line
	#line = line.strip("\n").strip("\r"); print line ## clean up line, leave tabs
	## find strings
	strings = re.findall(r"\'(.+?)\'",line); #print strings 
	for index,string in enumerate(strings): ## replace strings with list items
		line = line.replace(line[line.index(string)-1:line.index(string)+len(string)+1], strings[index]) #print 2,strings[index]
	lineList = line.split(" "); return LineList #print lineList ## split into list

def think(lineList=lineList):
		## set variables
		if ' = ' in line: var = line[:line.index(' = ')]; assignment = line[line.index(' = ')+3:]; global var; var = assignment;
		if ' is ' in line: var = line[:line.index(' is ')]; assignment = line[line.index(' is ')+3:]; global var; var = assignment; #print var,1,assignment;
			
		## order of operations
		## check for conditionals and store them
		if "if" in lineList: 
			if lineList[0] == "if":
				if lineList[1] == "I":
					if lineList[2] == "say":
						command = lineList[2:lineList.index(',')]
						instructionWhole = lineList[lineList.index(',')+1:]
						if instructionWhole[0] = 'then': instructionWhole = instructionWhole.remove("then")
						noodleD[command] = instructionWhole
		## start with verbs
		#for verb in verbs:
			#if verb in lineList:
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

def addQuotes(string):
	return "'"+string+"'"
def sliceAt(string, slicePoint):
	return string[string.index(slicePoint)+len(slicePoint):]
	
def remember(noodle):
	if functionD != noodleD:
		for key,value in functionD.items():
			for line in getNoodle():
				if 
	
# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
	main()
	input = raw_input("")