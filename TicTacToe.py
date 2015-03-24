# written using Python 3

# initialize my blank tic tac toe board
myMatrix = [[1,2,3], [4,5,6], [7,8,9]]

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
	printBoard ()
	markerNotPlaced = True
	while markerNotPlaced: #keep asking for valid input until the marker has been placed
		selection = input("Player " + str(player) + " please enter which spot to place your [ " + marker + " ]: ")
		markerNotPlaced = placeMarker(int(selection))
		if markerNotPlaced:
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


