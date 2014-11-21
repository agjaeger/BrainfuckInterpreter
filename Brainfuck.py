
import sys

progList = [0] * 100
dataPointer = 0

def incrementPointer():
	dataPointer += 1

def decrementPointer():
	dataPointer -= 1

def incrementData():
	progList[dataPointer] += 1

def decrementData():
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

