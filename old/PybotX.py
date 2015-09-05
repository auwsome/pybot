#import Pybot
#global run
#input=True
code=''


global tts
storageFile = 'PybotLines.py'

def load():
	with open(storageFile) as file:
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
	run = True
	while True:
		try:
			global list1; list1 = load(); print list1
			while run: 
				if loop(): pass
				else: 
					run = False
					input = raw_input('save?')
					if input == 'y': 
						with open(storageFile, 'wb') as file: 
							file.writelines(list1)
		except Exception,e: print str(e)
		input = raw_input('q?');print repr(input)
		if input == 'n\r': run = True
		if input == 'y\r': run = False; break

	
	
# check __main__ to run functions now that defined in any order above
if __name__=="__main__":
	mainLoop()