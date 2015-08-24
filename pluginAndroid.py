
#print 'q'
import android
import sys
import getopt
import re
import string
import time
from testfile import dctn, launchable, test, array1, array2

try:
	from testfile import intents, prefs
except ImportError:
	print 'cant import'
	available = False

avcomm=""
var=""
droid=android.Android()
params = droid.getIntent().result[u'extras']
for key in params.keys():
  if key.startswith('%'):
	exec key.lstrip('%') + '="' + params[key] + '"'
print( avcomm )  	
avcommC = avcomm.title()
avarr = avcomm.split(" ")
print 'avarr=',avarr	
if avcomm == "":
	avcomm = "spotify" #"test"


	
## Last Command
f1=open('./scripts/testfile.py', 'a')
if avcomm != "redo":
  print "last=",dctn["last"]
  f1.write("\ndctn = {'last':'"+avcomm+"'}")
if avcomm == "redo":
  print "do last=",dctn["last"]
  avcomm = dctn["last"]
  
'''
#print droid.prefGetAll()
  droid.prefGetValue("last")
  #result = droid.vibrate()
  ###droid.prefPutValue("last", avcomm) #vcmds.txt #String key, Object value, String filename[optional]: Desired preferences file. If not defined, uses the default Shared Preferences.)
'''
if avcomm == "out launch":
  f1.write("\n"+str(droid.getLaunchableApplications()))

print prefs
## Mute voice feedback
if avcomm == 'mute':
	if prefs['mute'] == 'true':
		f1.write("\nprefs = {'mute':'false'}")
	if prefs['mute'] == 'false':
		f1.write("\nprefs = {'mute':'true'}")
'''
if prefs['mute'] == 'true':
	droid.ttsSpeak(avcomm)	'''

found = ['']	
result = ''
	
## apps
apps = droid.getLaunchableApplications().result
#appsL = map(string.lower, apps)
appsL = dict((k.lower(), v) for k, v in apps.iteritems())
if avcomm in appsL:
  found.append('app')	
  print appsL[avcomm]
  droid.launch(appsL[avcomm])
  #result = droid.launch(appsL[avcomm]).result
print 'apps'

## parameters, var 
if "at" in avarr:
  found.append('at')	
  avcomm = " ".join(avarr[0:avarr.index("at")])
  print avcomm,avarr.index("at"),len(avarr)-1
  avvar = avarr[(avarr.index("at")+1):(len(avarr))]
  var = " ".join(avvar)
  print "var=",var, 'avarr2',avvar
  
## Tasker
if "task" in avarr:
	found.append('task')	
	avcomm = " ".join(avarr[0:avarr.index("task")])
	print avcomm,avarr.index("task"),len(avarr)-1
	var = avarr[(avarr.index("task")+2):(len(avarr))]
	#var = " ".join(avvar)
	print "var=",var
	extras = {'version_number': '1.0', 'task_name': var, 'task_priority': 9 }
	result = droid.makeIntent("net.dinglisch.android.tasker.ACTION_TASK", None, None, extras).result
	droid.sendBroadcastIntent(result)
try:
	extras = {'version_number': '1.0', 'task_name': avcommC, 'task_priority': 9 }
	taskIntent = droid.makeIntent("net.dinglisch.android.tasker.ACTION_TASK", None, None, extras).result
	droid.sendBroadcastIntent(taskIntent)
except:
	print "task error"

## SL4A API Commands
if avcomm in array2: 
  var=""
  found.append('api')	
  cmd = array1[array2.index(avcomm)]
  cmd = cmd.replace(" ", "")
  print "droid."+cmd+"()"
  if var == "":
	result = eval("droid."+cmd+"()")
  elif var != "":
	found.append('var')	
	print eval("droid."+cmd+"('"+var+"')")
	result = eval("droid."+cmd+"('"+var+"')")
print 'api'

##Launchables
print avcommC
if avcommC in launchable:
	found.append('launch')	
	print launchable[avcommC]
	droid.launch("'"+launchable[avcommC]+"'")
	taskIntent = droid.makeIntent("'"+launchable[avcommC]+"'").result
	#droid.sendBroadcastIntent(taskIntent)
	result = droid.sendBroadcastIntent(taskIntent).result
	print result

## Intents
if avcomm in intents:
	found.append('intent')	
	print intents[avcomm]
	#droid.launch("'"+intents[avcommC]+"'")
	taskIntent = droid.makeIntent(intents[avcomm]).result
	print taskIntent
	#droid.sendBroadcastIntent(taskIntent)
	result = droid.sendBroadcastIntent(taskIntent).result
	print result

## Custom
if avcomm == "next":
  taskIntent = droid.makeIntent("com.bambuna.podcastaddict.service.player.nexttrack").result
  droid.sendBroadcastIntent(taskIntent)
if avcomm == "test":
  result = droid.vibrate()
  print result
if (avcomm == "pause") or (avcomm == "paws"):
  result = droid.mediaPlayPause()
  #result = eval("droid."+avcomm+"()")
  print result
if (avcomm == "play"):
  result = droid.mediaPlayStart()
if avcomm == "hey":
	extras = {'version_number': '1.0', 'task_name': 'Butter', 'task_priority': 9 }
	taskIntent = droid.makeIntent("net.dinglisch.android.tasker.ACTION_TASK", None, None, extras).result
	print taskIntent
	result = droid.sendBroadcastIntent(taskIntent)  
	print result
	
	
if avcomm == "spotify":
	extras = {'query' :'artist:beatles'}
	taskIntent = droid.makeIntent("android.media.action.MEDIA_PLAY_FROM_SEARCH", None, None, extras).result
	droid.sendBroadcastIntent(taskIntent)  
	print taskIntent,droid.sendBroadcastIntent(taskIntent).result
print 'custom'
  
if avcomm == "find":
  extras = {"type":"String","description":"Stuff to look for","key":"query","name":var}
  taskIntent = droid.makeIntent("com.google.android.googlequicksearchbox.GOOGLE_SEARCH", None, None, extras).result
  droid.sendBroadcastIntent(taskIntent)
  print taskIntent, droid.sendBroadcastIntent(taskIntent).result
  

if found == '': 
	droid.vibrate()
if prefs['mute'] != 'true':
	foundJ = " ".join(found)
	output = [foundJ, avcomm]
	outputJ = " ".join(output)
	print outputJ
	droid.ttsSpeak(outputJ) 
	#if result[result] == None:
		#print 'none'
	#print str(result[result])
	#resultS = str(result[result])
	#droid.ttsSpeak(resultS)	
	#droid.makeToast(avcomm)
f1.close
print 'done'

'''	
{"target":"Activity","action":"com.google.android.googlequicksearchbox.GOOGLE_SEARCH","categories":[{"category":"android.intent.category.DEFAULT"}],"extras":[{"type":"String","description":"Stuff to look for","key":"query","name":"Search terms"}],"name":"Search","appname":"Google Now","id":"GoogleNowSearch"}	

	
if avcommC == "test":
  taskIntent = droid.makeIntent("com.pannous.voice.ACTION = 'test'").result
  droid.sendBroadcastIntent(taskIntent)	
	

if avcomm == "next":
  taskIntent = droid.makeIntent("com.bambuna.podcastaddict.service.player.nexttrack").result
  droid.sendBroadcastIntent(taskIntent)
  	
{"target":"Activity","action":"com.google.android.googlequicksearchbox.GOOGLE_SEARCH","categories":[{"category":"android.intent.category.DEFAULT"}],"extras":[{"type":"String","description":"Stuff to look for","key":"query","name":"Search terms"}],"name":"Search","appname":"Google Now","id":"GoogleNowSearch"}	


#droid.launch("com.android.browser.BrowserActivity")

class Task():
    SET_VARIABLE = "pause"
    def new_task(self):
        self.action_cnt = 0
        self.extras = {'version_number': '1.0', 'task_name': 'task' + str(time.time()), 'task_priority': 9 }
    def set_var(self, varname, value):
        self.action_cnt += 1
        self.extras['action' + str(self.action_cnt)] = {'action': self.SET_VARIABLE, 'arg:1': varname, 'arg:2': value, 'arg:3': False, 'arg:4': False, 'arg:5': False}
    def run_task(self):
        taskIntent = droid.makeIntent('net.dinglisch.android.tasker.ACTION_TASK', None, None, self.extras).result
        droid.sendBroadcastIntent(taskIntent)
    def set_var_now(self, varname, value):
        self.new_task()
        self.set_var(varname, value)
        self.run_task()

parameter = "par"
t = Task()
t.set_var_now("%RIM_TEST", parameter)
'''

'''
regex
(?<!^)(?=[A-Z])
\1 \2\3
\n\s
\s\s\s\s
results = map(int, results)
","
'''
  


	
	



