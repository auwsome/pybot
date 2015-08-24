# from https://gist.github.com/auwsome/7815c3b220de0faf5694
# This code is modified from code by Stephen C Phillips at http://scphillips.com would be nice.


html1 = """HTTP/1.0 200 OK
		Content-Type: text/html

		<html>
		<head>
		<title>Success</title>
		</head>
		<body>
		Boo!
		</body>
		</html>
		"""

def makeSock():
	import socket
	# Standard socket stuff:
	host = 'localhost' # do we need socket.gethostname() ?
	port = 8000
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(5) # don't queue up any requests

def listen():
	import re
	makeSock()	
	# Loop forever, listening for requests:
	#while True:
	if True:
		try:
			csock, caddr = sock.accept()
			#print "Connection from: " + `caddr`
			req = csock.recv(1024) # get the request, 1kB max
			#print req
			match=[]
			# Look in the first line of the request for a move command
			# A move command should be e.g. 'http://server/move?a=90' http://localhost:8000/?q=
			#match = re.match('GET /move\?a=(\d+)\sHTTP/1', req)
			match[0] = re.match('GET /\?q=([0-9a-zA-Z]*)\.&input', req)
			match[1] = re.match('GET /\?q=Search%20([0-9a-zA-Z]*)\.&input', req)
			match[2] = re.match('GET /\?q=([0-9a-zA-Z]*)&form', req)
			for i in enumerate(match):
				print match
				angle = match.group(1)
				print "ANGLE: " + angle + "\n"
				csock.sendall(html1)
				csock.close()
				sock.close()
				return str(angle)
			else:
				# If there was no recognised command then return a 404 (page not found)
				print "Returning 404"
				csock.sendall("HTTP/1.0 404 Not Found\r\n")
				csock.close()
				sock.close()
				return "Returning 404"
			
		except Exception,e: 
			print str(e)
			return str(e)

listen()	
#print listen()
