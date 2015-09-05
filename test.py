
# if 'i say ' in input: input2 = input.lstrip("i say");keyword = input2.strip(",");command = input.lstrip(",");print input2, keyword, command;input = 'if input == '+keyword+':'+command
input = input.replace('i say', 'input ==')
words = input.split("")
keyword = words(words.index('i say'): words.index(','))
command = ''.join.words(words.index(','): )
print input, keyword, command;
# input = 'if input == '+keyword+':'+command
	
	
if input == 'tts on': tts = True
if input == 'tts off': tts = False

#print input
if input == 'close': run = False
if input == 'q': run = False
code=''
if input == 'code': code = raw_input('enter code>')
if 'if ' in code: list1.append(code)
if 'if ' in input: list1.append(input)
# if 'if ' in input: code = input
if 'while  ' in input: code = input
if ' = ' in input: code = input

if input == 'quit': run = False; print 2
if input == 'undo': list1.pop(); print list1
if input == 'undo prepend': list1.pop(0);#input = '';
if 'prepend ' in input: p = input.lstrip('prepend '); list1.insert(0, p); input = '';
if input == 'list': print list1




if tts: print 2
if input == 'hi': print 'hello'