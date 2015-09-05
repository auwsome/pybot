
#global run
run = True
code=''
input=True

def load():
	with open('test.py') as file:
		list1 = file.readlines()
	return list1


def loop():
	code='';
	run=True
	global tts; tts=False
	input = raw_input('yes?'); print input
	for index,item in enumerate(list1):
		exec(list1[index])
	return run
		
while True:
	try:
		list1 = load(); print list1
		while run: 
			if loop(): pass
			else: 
				run = False
				input = raw_input('save?')
				if input == 'y': 
					with open('test.py', 'wb') as file: 
						file.writelines(list1)
	except Exception,e: print str(e)
	input = raw_input('q?')
	if input == 'n': run = True
	if input == 'y': break
