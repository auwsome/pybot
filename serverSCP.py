#!/usr/bin/env python

# This code is written by Stephen C Phillips.
# It is in the public domain, so you can do what you like with it
# but a link to http://scphillips.com would be nice.

import socket
import re
#import pybot

def makeSock():
	# Standard socket stuff:
	host = 'localhost' # do we need socket.gethostname() ?
	port = 8000
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(5) # don't queue up any requests

def listen():
	makeSock()	
	# Loop forever, listening for requests:
	while True:
		try:
			csock, caddr = sock.accept()
			print "Connection from: " + `caddr`
			req = csock.recv(1024) # get the request, 1kB max
			print req
			# Look in the first line of the request for a move command
			# A move command should be e.g. 'http://server/move?a=90' http://localhost:8000/?q=
			#match = re.match('GET /move\?a=(\d+)\sHTTP/1', req)
			#match = re.match('GET /\?q=Search%20([0-9a-zA-Z]*)\.&form', req)
			match = re.match('GET /\?q=Search%20([0-9a-zA-Z]*)\.&input', req)
			if match:
				angle = match.group(1)
				print "ANGLE: " + angle + "\n"
				return angle
				csock.sendall("""HTTP/1.0 200 OK
		Content-Type: text/html

		<html>
		<head>
		<title>Success</title>
		</head>
		<body>
		Boo!
		</body>
		</html>
		""")
			else:
				# If there was no recognised command then return a 404 (page not found)
				print "Returning 404"
				return "Returning 404"
				csock.sendall("HTTP/1.0 404 Not Found\r\n")
			csock.close()
			
		except Exception,e: 
			print str(e)
			return str(e)
			


listen()	
print listen()

