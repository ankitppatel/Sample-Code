import random

#create a list of words to choose from
List = ['Hello', 'Banana', 'Basketball', 'Computer', 'Phone', 'Car', 'Glasses'] 

#randomly select a word and define a number of variables
word = random.choice(List).upper() 
wordLength = len(word)
tempList = '-'*wordLength
L = list(tempList)
missedletters = []
failedAttempts = 0
correctAttempts = 0
response = ''	

# define a graphical output function based on number of incorrect letters
def printHangMan (fails):
	if fails == 0:
		print ()
	elif fails == 1:
		print ('|-0')
		print ('|  ')
		print ('|  ')
	elif fails == 2:
		print ('|-0')
		print ('| | ')
		print ('|   ')
	elif fails == 3:
		print ('|-\\0')
		print ('|  | ')
		print ('|   ')
	elif fails == 4:
		print ('|-\\0/')
		print ('|  | ')
		print ('|    ')
	elif fails == 5:
		print ('|-\\0/')
		print ('|  | ')
		print ('| / ')
	else:
		print ('|-\\0/')
		print ('|  | ')
		print ('| / \\')

	return

#keep guessing letters until you've lost or won 
while (failedAttempts < 6) and (correctAttempts < wordLength):
	while response == '':
		printHangMan (failedAttempts)
		response = input('Guess a letter in the word ' + ''.join(L) + " : " ).upper()
		if response == '':
			print ('You did not enter a letter') #ask again for a letter if a blank is entered
	
# find letter in the chosen word and replace each dash with relevant letter or increment failedAttempts
	if response in word: 
		print ('Correct!')
		a = 0
		for i in word:
			if response == i:
				L[a] = i
				correctAttempts += 1
			a += 1
		response = ''
	else:
		print ('wrong!')
		missedletters.append(response)
		missedletters.sort()
		print ("Incorrect guesses: ")
		print (missedletters)
		failedAttempts += 1
		response = ''
#after you've reached a limit on one of your counters. indicate if you won or lost		
if failedAttempts == 6:
	print ('You lose!')
	printHangMan (failedAttempts)
else:
	print ('You Win! You have figured out the word: ' + ''.join(L))
		

