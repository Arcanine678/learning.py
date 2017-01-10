import time
#Things to do:
#Size generator
#Work when unfindabl
#ToDo Color

round = 0
xSize = 20
ySize = 20


def Draw():
	for x in range(0, xSize):
		for y in range(0, ySize):
			if(len(table[x][y]) == 1):
				print ("[ " + table[x][y] + "]", end='')
			else:
				print ("[" + table[x][y] + "]", end='')
	print("")

def Start():
	startx = input("Please select the start point x coordinate between 1 and " + str(xSize - 2) + ":")
	starty = input("Please select the start point y coordinate between 1 and " + str(ySize - 2) + ":")
	table[int(startx)][int(starty)] = "0"
	Draw()
	endx = input("Please select a end point x coordinate between 1 and " + str(xSize - 2) + ":")
	endy = input("Please select a end point y coordiante between 1 and " + str(ySize - 2) + ":")
	table[int(endx)][int(endy)] =  "G"
	Draw()
	numOfObstacles = int(input("How many obstacles would you like to place?"))
	while (numOfObstacles > 0):
		obstaclex = input("Please select the x coordinate of the obstacle")
		obstacley = input("Please select the y coordinate of the obstacle")
		table[int(obstaclex)][int(obstacley)] = " X"
		numOfObstacles = numOfObstacles - 1
		Draw()
	return int(startx),int(starty),int(endx),int(endy)

def Step():
	bFinished = False
	iSteps = 0
	for x in range(0, xSize):
		for y in range(0, ySize):
			if(table[x][y] == str(round)):
				if(table[x-1][y] == "G"):
					bFinished = True
					iSteps = iSteps + 1
					table[x-1][y] = str(round+1)
					iSteps = iSteps + 1
				elif(table[x-1][y] == "  "):
					table[x-1][y] = str(round+1)
					iSteps = iSteps + 1
				if(table[x+1][y] == "G"):
					bFinished = True
					table[x+1][y] = str(round+1)
					iSteps = iSteps + 1
				elif(table[x+1][y] == "  "):
					table[x+1][y] = str(round+1)
					iSteps = iSteps + 1
				if(table[x][y-1] == "G"):
					bFinished = True
					table[x][y-1] = str(round+1)
					iSteps = iSteps + 1
				elif(table[x][y-1] == "  "):
					table[x][y-1] = str(round+1)
					iSteps = iSteps + 1
				if(table[x][y+1] == "G"):
					bFinished = True
					table[x][y+1] = str(round+1)
					iSteps = iSteps + 1
				elif(table[x][y+1] == "  "):
					table[x][y+1] = str(round+1)
					iSteps = iSteps + 1
	if(iSteps == 0):
		bFinished = True
		print("A path could not be found")
	return bFinished
				
def Update():
	print("Dijkstra's step: " + str(round))

def FindPath(startx,starty,endx, endy, round, maxx, maxy):
	iCurrentx = endx
	iCurrenty = endy
	bFirst = True
	while(iCurrentx != startx or iCurrenty != starty):
		if(table[iCurrentx-1][iCurrenty] == str(int(round) -1)):
				if(bFirst == True):
					table[iCurrentx][iCurrenty] = "G"
					bFirst = False
				else:	
					table[iCurrentx][iCurrenty] = "P"
				iCurrentx = iCurrentx - 1
				round = round - 1 
				Draw()
				PathUpdate()
		elif(table[iCurrentx+1][iCurrenty] == str(int(round) -1)):
			if(bFirst == True):
				table[iCurrentx][iCurrenty] = "G"
				bFirst = False
			else:	
				table[iCurrentx][iCurrenty] = "P"
			iCurrentx = iCurrentx + 1
			round = round - 1 
			Draw()
			PathUpdate()
		elif(table[iCurrentx][iCurrenty-1] == str(int(round) -1)):
			if(bFirst == True):
				table[iCurrentx][iCurrenty] = "G"
				bFirst = False
			else:	
				table[iCurrentx][iCurrenty] = "P"
			iCurrenty = iCurrenty - 1
			round = round - 1 
			Draw()
			PathUpdate()
		elif(table[iCurrentx][iCurrenty+1] == str(int(round) -1)):
			if(bFirst == True):
				table[iCurrentx][iCurrenty] = "G"
				bFirst = False
			else:	
				table[iCurrentx][iCurrenty] = "P"
			iCurrenty = iCurrenty + 1
			round = round - 1 
			Draw()
			PathUpdate()
	
		Wait()
	
def PathUpdate():
	print("Calculating path...")

def CleanPath():
	for x in range(0, xSize):
		for y in range(0, ySize):
			if(table[x][y] == "P"):
				pass
			elif(table[x][y] == "G"):
				pass
			elif(table[x][y] == ' X'):
				pass
			elif(table[x][y] == "0"):
				table[x][y] = "S"
			else:
				table[x][y] = " " 

def Wait():
	time.sleep(0.5)

def ChooseMaze():
	selection = input("Select the type of map you want (maze, empty, spiral, rows) : ")
	if (selection == "maze"):
		map = [
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ',' X', ' X','  ','  ','  ','  ','  ','  ',' X','  ', ' X'],
[' X','  ',' X',' X','  ',' X',' X',' X','  ',' X', ' X','  ',' X','  ',' X','  ','  ',' X','  ', ' X'],
[' X','  ',' X','  ','  ',' X','  ','  ','  ',' X', ' X','  ',' X','  ',' X','  ','  ',' X','  ', ' X'],
[' X','  ',' X','  ',' X',' X','  ',' X',' X',' X', ' X','  ',' X','  ',' X',' X',' X',' X','  ', ' X'],
[' X','  ',' X','  ',' X',' X','  ','  ','  ',' X', ' X','  ',' X','  ',' X','  ','  ','  ','  ', ' X'],
[' X','  ',' X','  ','  ',' X',' X',' X','  ',' X', ' X','  ',' X','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ',' X',' X','  ',' X',' X','  ','  ',' X', ' X','  ',' X','  ',' X','  ',' X',' X',' X', ' X'],
[' X','  ','  ',' X','  ',' X',' X','  ',' X',' X', ' X','  ',' X','  ',' X','  ','  ','  ','  ', ' X'],
[' X',' X','  ',' X','  ','  ','  ','  ',' X',' X', ' X','  ',' X','  ',' X',' X','  ',' X','  ', ' X'],
[' X',' X','  ',' X',' X',' X',' X','  ',' X',' X', ' X','  ',' X','  ','  ','  ','  ',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ',' X','  ',' X',' X', ' X','  ',' X',' X',' X',' X','  ',' X','  ', ' X'],
[' X','  ',' X','  ',' X','  ','  ','  ',' X',' X', ' X','  ',' X','  ','  ','  ','  ',' X','  ', ' X'],
[' X','  ',' X','  ',' X','  ','  ','  ',' X',' X', ' X','  ',' X','  ',' X',' X',' X',' X','  ', ' X'],
[' X','  ',' X','  ',' X',' X',' X',' X',' X',' X', ' X','  ',' X','  ','  ','  ',' X',' X','  ', ' X'],
[' X','  ',' X','  ','  ','  ','  ','  ','  ',' X', ' X','  ',' X',' X',' X','  ',' X',' X','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X','  ',' X', ' X','  ',' X','  ','  ','  ',' X','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ',' X', ' X','  ',' X','  ',' X',' X',' X',' X',' X', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ',' X','  ','  ','  ','  ','  ','  ', ' X'],
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X']]
		return map
	elif (selection == "empty"):
		map = [
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X']]
		return map
	
	elif (selection == "spiral"):
		map = [
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ',' X','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ',' X','  ','  ', '  ','  ','  ','  ','  ','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ',' X','  ',' X', ' X',' X',' X',' X',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ',' X','  ',' X', '  ','  ','  ','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ',' X','  ','  ', '  ',' X',' X','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ',' X',' X','  ', '  ','  ',' X','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X','  ','  ','  ','  ', ' X','  ',' X','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ',' X',' X',' X',' X',' X', ' X','  ',' X','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X','  ','  ','  ','  ','  ','  ', '  ','  ',' X','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ',' X','  ',' X','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X','  ',' X','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ',' X','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X']]
		return map
	
	elif (selection == "rows"):
		map = [
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X','  ','  ','  ','  ','  ','  ','  ','  ','  ', '  ','  ','  ','  ','  ','  ','  ','  ','  ', ' X'],
[' X',' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X',' X',' X',' X',' X',' X',' X',' X',' X', ' X']]
		return map
	
print ("Hello and welcome to Eddie's attempt at a Dijkstra style shortest path algorithm")
table = ChooseMaze()


Draw()
startx,starty,endx,endy = Start()
Draw()
Update()

bGoalFound = False
while(bGoalFound == False):
	Draw()
	bGoalFound = Step()
	round = round + 1
	Update()
	Wait()

FindPath(startx,starty,endx,endy,round, xSize, ySize)
CleanPath()
Draw()
done = input("The shortest path has been found")
