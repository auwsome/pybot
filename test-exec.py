
#global run
run = True
code=''
input=True
global tts

def load():
	with open('test.py') as file:
		list1 = file.readlines()
	return list1

def loop():
	run=True; tts=False
	code='';i=0
	input = raw_input('yes?\n').strip('\r'); print repr(input)
	for index,item in enumerate(list1):
		try:
			exec(list1[index]);#print i;i=i+1
		except Exception,e: pass#print 'err', str(e)
	return run

def mainLoop():
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
		input = raw_input('q?');print repr(input)
		if input == 'n\r': run = True
		if input == 'y\r': run = False; break

	
	
# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
	mainLoop()