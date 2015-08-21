
import sys, os, subprocess
import csv, json
import serverSCP as s


#d['say']={'word':'say','action':'print'}
dctn={'is':'equals', 'thing':'something', 'quit':'end loop', 'how':'thing', '?':'question mark', ' ':'space'}

cwd = os.getcwd()
try: 
	with open(cwd+'dict.json', 'rb') as outfile:
		filedict = json.load(outfile)
	for key, value in filedict.items():
		if not key in dctn.keys():
			dctn[key] = value
except Exception,e: print str(e)
try: 
	with open('commands.json', 'rb') as outfile:
		commands = json.load(outfile)
except Exception,e: print str(e)

context=None


while input is not None:
	################## init
	input = ""
	response = None
	
	'''if context is not None: 
		phrase2 = raw_input(str(context)+ ' is ')
		context['action'] = phrase2; context = None
		print dctn[df[0]]['action']
		#confirm = raw_input('confirm?')
		#if confirm == 'y':  context = confirm; context = None; input ="okay"'''
	
	################### input and convert to list of words
	if s.listen(): 
		input = s.listen()
		print input, 'done'
	else: input = raw_input(input+'\n')
	try: words = input.split(' ')
	except: pass
	
	################### direct commands
	if input == 'quit': break
	if input == 'dctn': print dctn; continue
	
	################### keyword based commands
	
	########## definitions
	if 'is' in input and not 'what is' in input and not words[0] == 'is': 
		df= input.split(' is ') #definition 
		try: dctn[df[0]].append(df[1])
		except: dctn[df[0]]=[df[1]]
		if df[1] == 'action':
			dctn[df[0]]={'action':''}
			response = 'how '+ df[0] +"?" 
			context = dctn[df[0]]
		continue
		
	if 'is not' in input: 
		split= input.split(' is not ') #remove definition 
		try: dctn[split[0]].remove(split[1])
		except: pass
		
	if '?' in input:
		q = input.split('?') #question
		print dctn[q[0]]
		response = dctn[q[0]]
	
	########## actions
	if 'e' in input:
		e = input.split('e ') #exec
		try: exec(e[1]); continue
		except Exception,e: print str(e)
	
	if 'do' in input: #action
		try: 
			exec(dctn[words[1]]['action']+' "'+str(''.join(words[2:99]))+'"'); continue
		except Exception,e: print str(e)
		
	if words[0] and words[0] in commands:
		try: 
			vcommand = words[0]
			try: context = words.get([1])
			except: print '1'
			command = commands[vcommand][context]
			pcommand = commands[vcommand]['print']
			print vcommand,words[0],pcommand
			print vcommand,context,command
			if pcommand is not None:
				input = raw_input(pcommand+' "'+str(''.join(words[2:99]))+'"? ')
				if not input == ('y' or 'yes'): break
				exec(pcommand+' "'+str(''.join(words[2:99]))+'"')
			if commands[vcommand]['windows'] is not None or context == 'windows':
				process = subprocess.Popen(commands[vcommand]['windows'], shell=True, stdout=subprocess.PIPE)
				#subprocess.Popen("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True, stdout=subprocess.PIPE)
				process.wait(); print process.returncode
		except Exception,e: print str(e)
		continue
	
	########################### catch unknown words
	for word in words:
		if word not in dctn:  response = 'what is '+ word +"?"
		
	########################### output
	if response is not None: print response	
	
	
with open('dict.json', 'wb') as outfile: ##sqlite to append
	json.dump(dctn, outfile)
# writer = csv.writer(open('dict.csv', 'ab+'))
   
print dctn	   
	   
sys.exit()	   
