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

verbsString = 'write make create '; verbs = verbString.split(" ")
prepositionsString = 'into over'; prepositions = prepositionsString.split(" ")



with open("pseudocode.txt", 'rb') as file: 
	list1 = file.readlines(file)

def main():
	for line in list1:
		# remove determinants or just don't use them
		for verb in verbs:
			if verb in line:
				#sentence structure SVO
				SO = line.split(verb); subject = SO[0]; object1 = SO[1]
				if verb == 'write': 
					for preposition in prepositions:
						if preposition in line:
							PO = line.split(preposition); object2 = PO[1]
							if preposition == 'in':
								write(object1, file=object2)
							if preposition == 'into':
								write(object1, into=True, file=object2)
							if preposition == 'over':
								write(object1, into=True, file=object2, over=True)
						else: write(object1)

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
		else print line

def write(sequence, into=False, file=False):
	if into: 
		if file == 'file': fileMode = 'wb'
		if into: fileMode = 'ab'
		if over: fileMode = 'wb'
		if isinstance(sequence,lst):
			with open(File, fileMode) as file: file.writelines(sequence)
		if isinstance(sequence,str):
			with open(File, fileMode) as file: file.write(sequence)
	else: print sequence	


	
# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
	readFiles()
	main()