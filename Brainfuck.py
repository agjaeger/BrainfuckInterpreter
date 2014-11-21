
import sys

progList = [0] * 100
dataPointer = 0

def incrementPointer():
	global dataPointer
	dataPointer += 1

def decrementPointer():
	global dataPointer
	dataPointer -= 1

def incrementData():
	global progList
	progList[dataPointer] += 1

def decrementData():
	global progList
	progList[dataPointer] -= 1

def printData():
	sys.stdout.write(chr(progList[dataPointer]))

def inputData():
	progList[dataPointer] = ord(sys.stdin.read(1))

cmds = {
	'>' : incrementPointer,
	'<' : decrementPointer,
	'+' : incrementData,
	'-' : decrementData,
	'.' : printData,
	',' : inputData,
}

with open("test.bf") as f:
  while True:
    c = f.read(1)
    
    if not c:
    	break
    
    if c in cmds.keys():
    	cmds[c]()

