#!/usr/bin/env python

import sys

f = open(sys.argv[1])

progList = [0]
startList = []
dataPointer = 0

def incPointer():
	global dataPointer
	progList.append(0)
	dataPointer += 1

def decPointer():
	global dataPointer
	dataPointer -= 1

def incData():
	progList[dataPointer] += 1

def decData():
	progList[dataPointer] -= 1

def printData():
	sys.stdout.write(chr(progList[dataPointer]))

def inputData():
	progList[dataPointer] = ord(sys.stdin.read(1))

def startWhile():
	startList.append(f.tell() - 1)

def endWhile():
	if progList[dataPointer] > 0:
		f.seek(startList.pop())
	else:
		startList.pop()

########
## Super Set Functions
########

def inputString():
	global dataPointer
	orig_pos = dataPointer
	
	print dataPointer
	string = sys.stdin.read(progList[dataPointer])
	
	for character in string:
		incPointer()
		progList[dataPointer] = ord(character)

	dataPointer = orig_pos

def resetPos():
	global dataPointer
	dataPointer = 0

########
## End of Super Set Functions
########

cmds = {
	'>' : incPointer,
	'<' : decPointer,
	'+' : incData,
	'-' : decData,
	'.' : printData,
	',' : inputData,
	'[' : startWhile,
	']' : endWhile,

	';' : inputString,
	'*' : resetPos,
}

while True:
	c = f.read(1)
	if not c:
		break
	if c in cmds.keys():
		cmds[c]()