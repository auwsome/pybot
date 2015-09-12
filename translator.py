import translated
import nltk, re
#nltk.download('punkt')
#nltk.download('maxent_treebank_pos_tagger')
#pypm install numpy
#tagdict = load('help/tagsets/upenn_tagset.pickle'); tagdict.keys()
#http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
#text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
#nltk.pos_tag(text)
# re.findAll('(.*) computer(.*)')

from textblob import TextBlob
blob = TextBlob("write 'hello, how are you?' into a file")
blob.tags

verbsString = 'write ,make ,create '; verbs = verbsString.split(","); print verbs
prepositionsString = 'in ,into ,over '; prepositions = prepositionsString.split(",")



with open("pseudocode.txt", 'rb') as file: 
	list1 = file.readlines()

def main():
	for line in list1:
		line = line.strip("\n").strip("\r").strip("\t").split(" "); print line
		# remove determinants or just don't use them
		for verb in verbs:
			print verb, line
			#if verb in line:
			if 'write' in line:
				#sentence structure SVO
				#SO = line.split(verb); subject = SO[0]; object1 = SO[1]
				SO = line.split(verb); subject = SO[0]; object1 = SO[1]
				if verb == 'write': 
					for preposition in prepositions:
						print preposition
						if preposition in line:
							PO = line.split(preposition); object2 = PO[1]
							write(object1, preposition, object2)
						else: write(object1)
			else: print line

'''
	blob = TextBlob(line)
	tagged = nltk.pos_tag(line); print tagged
	#verbs = [a[1] for (a, b) in tagged if b[1] == 'VB']
	verbs = [a for (a, b) in tagged if b == 'VB']
	prepositions = [a for (a, b) in tagged if b == 'IN']
	prepositions = [a for (a, b) in tagged if b == 'IN']
	if verbs: 
		#print verb
		for verb in verbs:
			if verb == 'write':
				for preposition in prepositions:
					if preposition == 'into':
						
			else: 
				prompt = "how do i ",verb; exec(channel) 
				#input = 
'''				
				
		# if 'into a file' in line:
		# if 'write' in line:
			# line = line.replace('write','print')
			# if 'write into' in line:
			# elif print in line: list2 = list(line); list2[1] = "'"+list[1]; list2[-1] = list2[-1]+"'"; line = " ".join(list2)

def write(sequence, preposition=False, object2=False):
	if object2:
		# check for filename
		if 'file named' in object2:
			fileName = addQuotes(sliceAt(object2,'file named '))
	if preposition: 
		if preposition == 'in': fileMode = 'wb'
		if preposition == 'into': fileMode = 'ab'
		if preposition == 'over': fileMode = 'wb'
		if isinstance(sequence,list):
			with open(fileName, fileMode) as file: file.writelines(sequence)
		if isinstance(sequence,str):
			with open(fileName, fileMode) as file: file.write(sequence)
	else: print sequence	

def addQuotes(string):
	return "'"+string+"'"
def sliceAt(string, slicePoint):
	return string[string.index(slicePoint)+len(slicePoint):]
	
# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
	main()
	input = raw_input("")