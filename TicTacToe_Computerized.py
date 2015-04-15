# written using Python 3

import random

# initialize my blank tic tac toe board
myMatrix = [[1,2,3], [4,5,6], [7,8,9]]
snapshots = [[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]]
snapMap = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (7,5,3))

#function to print the tic tac toe board 
def printBoard():
	for x in range(0,len(myMatrix)):
		print (myMatrix[x])

#function to find and place current player's marker on the board
def placeMarker(selection):
	for x in range(0,len(myMatrix)):
		for y in range(0,len(myMatrix[x])):
			if myMatrix[x][y] == selection:
				myMatrix[x][y] = marker
				return False
	return True

# function to check to see if a winner is found
def foundWinner(marker):
	#check each horizontal row for completeness, if three in a row found, return true
	for x in range(0,len(myMatrix)):
		counter = 0
		for y in range(0,len(myMatrix[x])):
			if myMatrix[x][y] == marker:
				counter +=1
				if counter == 3:
					return True

	#check each vertical column for completeness, if three in a row found, return true
	for y in range(0,len(myMatrix[0])):
		counter = 0
		for x in range(0,len(myMatrix)):
			if myMatrix[x][y] == marker:
				counter +=1
				if counter == 3:
					return True

	#check diagonally if three in row. 
	if myMatrix[0][0] == marker and myMatrix[1][1] == marker and myMatrix[2][2] == marker:
		return True

	if myMatrix[2][0] == marker and myMatrix[1][1] == marker and myMatrix[0][2] == marker:
		return True	
	
	return False #if no winner found return false

def createSnapShot():
#run through all 8 combinations and populate a 8x3 grid for the computer to assess situation
	snapShotRow = 0
	for x in range(0,len(myMatrix)):
		for y in range(0,len(myMatrix[x])):
			if type(myMatrix[x][y]) is str:
				snapshots[snapShotRow][y] = myMatrix[x][y]
		snapShotRow += 1

	for y in range(0,len(myMatrix[0])):
		for x in range(0,len(myMatrix)):
			if type(myMatrix[x][y]) is str:
				snapshots[snapShotRow][x] = myMatrix[x][y]
		snapShotRow +=1

	if type(myMatrix[0][0]) is str:
		snapshots[snapShotRow][0] = myMatrix[0][0]
	if type(myMatrix[1][1]) is str:
		snapshots[snapShotRow][1] = myMatrix[1][1]
	if type(myMatrix[2][2]) is str:	
		snapshots[snapShotRow][2] = myMatrix[2][2] 
	snapShotRow +=1

	if type(myMatrix[2][0]) is str:
		snapshots[snapShotRow][0] = myMatrix[2][0]
	if type(myMatrix[1][1]) is str:
		snapshots[snapShotRow][1] = myMatrix[1][1]
	if type(myMatrix[0][2]) is str:
		snapshots[snapShotRow][2] = myMatrix[0][2] 

def calculateNextMove():
	#get the latest lay of the land before making a decision
	createSnapShot()
	# go for the win
	for x in range(0,len(snapshots)):
		if snapshots[x].count('O') == 2:
			if snapshots[x].count(1)== 1:
				#return the location of the 1 where you win
				return snapMap[x][snapshots[x].index(1)] 

	# go for the block
	for x in range(0, len(snapshots)):
		if snapshots[x].count('X') == 2:
			if snapshots[x].count(1)==1:
				#return the location of the 1 where you block opponent from winning
				return snapMap[x][snapshots[x].index(1)]

	#go for a spot where you already have a marker started
	for x in range(0, len(snapshots)):
		if snapshots[x].count('O') == 1:
			if snapshots[x].count(1)==2:
				#return the location of first empty cell from where you've started 
				return snapMap[x][snapshots[x].index(1)]

	#if you have no where tactical to go, then pick a random number from 1-9, until you find an empty cell
	return random.randint(1,9)


#check to see if the user would like to have a computerized player
compSelection = int(input("Are you going to play with a computer (enter 1 for Yes, 2 for No: "))
if compSelection == 1:
	computer = True
	print("Player 2 is now the computer")
else:
	computer = False


# while there is no winner, keep asking for inputs
counter = 0 #keep track of how many valid turns have been taken
while counter <9:
	counter +=1
	if counter%2 == 0: # even player = player 2
		player = 2
		marker = "O"
	else:
		player = 1 # odd player = player 1
		marker = "X"
	markerNotPlaced = True
	while markerNotPlaced: #keep asking for valid input until the marker has been placed
		if player == 2 and computer:
			#print ("Computer says your next move should be " + str(calculateNextMove()))
			markerNotPlaced = placeMarker(calculateNextMove())
		else:
			printBoard ()
			selection = input("Player " + str(player) + " please enter which spot to place your [ " + marker + " ]: ")
			markerNotPlaced = placeMarker(int(selection))

		if markerNotPlaced and not (player == 2 and computer):
			#if you come back empty handed from the placement process, throw error msg and go back to begining for another input
			print ("You did not pick a valid spot on the board for your marker")		
		else:
			if foundWinner(marker): #check after each marker placement to see if a three in a row is formed, horizontally, vertically, diagonally
				printBoard ()
				print ("Congrats player " + str(player) + " you WIN!")
				counter = 20
			else:
				if counter == 9:
					printBoard ()
					print ("There seems to be no winner, try again.")



