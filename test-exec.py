
global run
run = True
code=''


list1=[]
with open('test.py') as file:
    list1 = file.readlines()
print list1

loop = "input = raw_input('yes?');\nprint input;\nfor index,item in enumerate(list1):\n\t exec(list1[index]);\n\t if not code == '': list1.append(code); list1.append(''); code = '';\n\t if input == 'undo': list1.pop();input = '';#\n\t if 'prepend ' in input: list1.insert(0, input.lstrip('prepend'));input = ''"

# loop = "input = raw_input('yes?');\nfor index,item in enumerate(list1):\n\t exec(list1[index]);\n\t if not code == '': list1.append(code); list1.append(''); code = '';\n\t if input == 'undo': list1.pop();input = '';\n\t if 'prepend ' in input: print 4"

#loop=''

def loop():
	code='';
	global tts; tts=False
	input = raw_input('yes?'); print input
	for index,item in enumerate(list1):
		exec(list1[index])
		if not code == '': list1.append(code); code = '';
		# if input == 'undo': list1.pop();#input = '';
		if input == 'undo prepend': list1.pop(0);#input = '';
		if 'prepend ' in input: 
			p = input.lstrip('prepend '); list1.insert(0, p); input = '';
		
while run:
	try:
		# while run: exec(loop)
		while run: loop()
		with open('test.py', 'wb') as file: 
			file.writelines(list1)
	except Exception,e: print str(e)
	input = raw_input('?')
	if input == 'q': run = False

	
	
	
	
	
'''	
input = raw_input('yes?');\n
for index,item in enumerate(list1):\n
\t exec(list1[index]);\n
\t print input;\n
\t if not code == '': list1.append(code); list1.append(''); code = '';\n
\t if input == 'undo': list1.pop();input = '';\n
\t if 'prepend ' in input == : input.lstrip('prepend');input = ''
'''