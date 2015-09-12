import translated
import nltk, re
#nltk.download('punkt')
#nltk.download('maxent_treebank_pos_tagger')
#pypm install numpy
#tagdict = load('help/tagsets/upenn_tagset.pickle'); tagdict.keys()
#http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
#text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
#nltk.pos_tag(text)

#sentence structure SVO

from textblob import TextBlob
blob = TextBlob("write test into a file")
blob.tags

verbsString = 'write make create '; verbs = list(verbString)
prepositionString

with open("pseudocode.txt", 'rb') as file: 
	list1 = file.readlines(file)
	
for line in list1:
	tagged = nltk.pos_tag(line); print tagged
	#verbs = [a[1] for (a, b) in tagged if b[1] == 'VB']
	verbs = [a for (a, b) in tagged if b == 'VB']
	if verbs: 
		#print verb
		for verb in verbs:
			if verb == 'write':
				if pre
				re.findAll('(.*) computer(.*)')
	if 'into a file' in line:
		
	if 'write' in line:
		line = line.replace('write','print')
		if 'write into' in line:
		elif print in line: list2 = list(line); list2[1] = "'"+list[1]; list2[-1] = list2[-1]+"'"; line = " ".join(list2)
	else print line

	
	
	

with open(storageFile, 'wb') as file: 
	file.writelines(list1)