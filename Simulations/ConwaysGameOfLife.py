import time

xSize = 10
ySize = 10
currentTable = [
[' ',' ',' ',' ',' ',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ','X',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ','X',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ','X',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ', ' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ']]

nextTable = currentTable

def Draw():
	for x in range(0, xSize):
		for y in range(0, ySize):
			print ("[" + currentTable[x][y] + "]", end='')
		print("")

def Start():
	Draw()
	sInput = input("Please select run if you would like to run the simulation, or add if you wish to add more starting peices: ")
	if (sInput == "add"):
		Add()
	elif(sInput == "run"):
		Run(currentTable)
	else:
		Start()

def Wait():
	time.sleep(100)

def Add():
	sInputx = input("Choose an x coordinate :")
	sInputy = input("Choose a y coordinate :")
	currentTable[int(sInputx)][int(sInputy)] = "X"
	Start()

def Run(currentTable):
	bWorking = True
	while(bWorking == True):
		nextTable = currentTable
		for x in range(1, xSize - 1):
			for y in range(1, ySize - 1):
				iCountAdjacent = 0
				if(currentTable[x-1][y] == 'X'):
					iCountAdjacent = iCountAdjacent + 1
				if(currentTable[x+1][y] == 'X'):
					iCountAdjacent = iCountAdjacent + 1
				if(currentTable[x][y-1] == 'X'):
					iCountAdjacent = iCountAdjacent + 1
				if(currentTable[x][y+1] == 'X'):
					iCountAdjacent = iCountAdjacent + 1
				
				#Check fewer than 2 or more than 3
				if(iCountAdjacent < 2 or iCountAdjacent > 3):
					#If so kill
					nextTable[x][y]	= ' '
					print("kill")
				
				#Check if exactly 3 neighbours
				if(iCountAdjacent == 3):
					#If so live
					nextTable[x][y] = 'X'
					print("Live")

		currentTable = nextTable
		Draw()
		print("Life is living")
		Wait()
	bWorking = False
		
Start()