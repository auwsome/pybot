#print 1
exec(input)
words = input.split(" "); #print "words=",words
if 'i say ' in input: keyword = ' '.join(words[words.index('say')+1:words.index(',')]); #print keyword
if 'i say ' in input: command = ' '.join(words[words.index(','):]); #print command
#print 2

if 'i say ' in input: input = input.replace('i say ', 'input == "').replace(' ,', '" :')
# if 'i say ' in input: input = input.replace(',', ':')
print "input=",input
if 'i say ' in input: list1.append(input)
# if 'i say ' in input: input = 'if input == '+keyword+':'+command


if input == 'list': print list1
if input == 'tts on': tts = True
if input == 'tts off': tts = False
if input == 'close': run = False
if input == 'q': run = False
code=''
if input == 'code': code = raw_input('enter code>')
if 'if ' in code: list1.append(code)
if 'if ' in input: list1.append(input)
if 'while  ' in input: code = input
if ' = ' in input: code = input

if input == 'quit': run = False; print 2
if input == 'undo': list1.pop(); print list1
if input == 'undo prepend': list1.pop(0);#input = '';
if 'prepend ' in input: p = input.lstrip('prepend '); list1.insert(0, p); input = '';
if input == 'list': print list1


	if tts: print 2
if input == 'hi': print 'hello'

if 'find' in input: target = ' '.join(words[words.index('find '):]); list1[words.index(target); print target
if 'replace with' in input: replacement = ' '.join(words[words.index('replace with '):]); list1[words.index(replacement); print replacement