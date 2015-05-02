# Tic Tac Toe
# Tic Tac Toe console text user interface game for a human playing against the computer. 
# The random class generates random  numbers which are used for the moves of the computer in the game. 
# Class time is used to set time elapse to make the game more real.
# Class os is uset to clear the console. 
import random
import time
import os
os.system("mode con: line = 60")  

def ClearCmd():
	os.system("cls" if os.name=="nt" else "clear")

def PlayFirstOrSecond():
	print("WELCOM TO TIC TAC TOE!")
	print()
	print("You are playing against the computer!")
	print("Choose if you want to play first or second.")
	print("To play first press 1 and to play second press 2.")
	
	while True:
		firstOrSec = input("Enter number: ")
		if(firstOrSec == "1"):
			break;
		elif(firstOrSec == "2"):
			break;
		else:
			print("Invalid input!")
	firstOrSec = int(firstOrSec)
	return firstOrSec
	
def IntroToGame():
	print("WELCOME TO TIC TAC TOE!");
	print();
	print("Please choose a position \"box number\" to place your \"X\" or \"O\".");
	print("The first player by default uses \"X\", the second player uses\"O\".");
	print();
	print("Enjoy!");
	print();
	
def FrameAndContent(numsTo9):
	for i in range(0, length + 2,3):  #//////////////Start code for: Printing frame and content of frame
		adds = 0
		for l in range( 0,length):
			print("-", end="")
		print()
		if (i == 9):
			break;
		for j in range(0,length):
			if (j % 2 == 0):
				print('|', end="")
			else:
				if (numsTo9[i + adds] == 'X'):
					print(numsTo9[i + adds], end="")    # 1 2 3
				elif (numsTo9[i + adds] == 'O'):        # 4 5 6 
					print(numsTo9[i + adds], end="")    # 7 8 9 
				else:
					print(numsTo9[i + adds], end="")
				adds = adds + 1	
		print()       #/////////////////////////End code for: Printing Frame and content of the frame 
def ManipulateNumsTo9Arr(inputForGame, counter):  # Player input will be a number from 1 to 9 
	xO = [ 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O' ]
	inputForGame = int(inputForGame)
	numsTo9[inputForGame - 1] = xO[counter]
	return numsTo9	

def ValidPlayerInput():
	while True:
		playerInput = input("** "+xO[counter]+" ** Enter position --> ")
		try:
			playerInput = int(playerInput)
			playerInput = str(playerInput)
			for i in range(0,9):
				if(numsTo9[i] == playerInput):
					return playerInput
					break;
				elif(i == 8):
					error = int(err) # I'm causing error on purpose to go to except statement;
			break;
		except: 
			print("Invalid input!")
			
def ComputerInput():
	temp = 5
	while(temp > 0): # gives us true unless temp value is changed!
		inputFromComp = random.randrange(1, 9)
		inputFromComp = str(inputFromComp)
		for i in range(0, len(numsTo9)):
			if(numsTo9[i] == inputFromComp): # inputFromComp is a string on this line 
				temp = -1 # temp less than 0 so we can exit the while loop!
				time.sleep(1.5)                                                                     # time.sleep
				return inputFromComp
				break;
	
def CheckForWinner(numsTo9):
	winner = False;
	if(numsTo9[0] == numsTo9[1] and numsTo9[1] == numsTo9[2]):
		winner = True;
	elif(numsTo9[3] == numsTo9[4] and numsTo9[4] == numsTo9[5]):
		winner = True;
	elif(numsTo9[6] == numsTo9[7] and numsTo9[7] == numsTo9[8]):
		winner = True;
	elif(numsTo9[0] == numsTo9[3] and numsTo9[3] == numsTo9[6]):
		winner = True;
	elif(numsTo9[1] == numsTo9[4] and numsTo9[4] == numsTo9[7]):
		winner = True;
	elif(numsTo9[2] == numsTo9[5] and numsTo9[5] == numsTo9[8]):
		winner = True;
	elif(numsTo9[0] == numsTo9[4] and numsTo9[4] == numsTo9[8]):
		winner = True;
	elif(numsTo9[2] == numsTo9[4] and numsTo9[4] == numsTo9[6]):
		winner = True;
	return winner 

def ContinueOrQuit():
	quit = True 
	time.sleep(2)
	print()
	while True:
		yesOrNo = input("Do you want to continue yes/no ").lower()
		if(yesOrNo == "no"):
			quit = False
			break;
		elif(yesOrNo == "yes"):
			break;
	return quit
				
		
# we can ask if you want to play first or second regarding enter 1 0r 2 ;
quit = True
while(quit == True):
	xO = [ 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O' ]
	length = 7
	temp = 0
	frameEl = 0
	frameStr = ""
	triger = 0
	counter = 0
	f = 0
	numsTo9 = ['1', '2','3','4','5','6','7','8','9']
	oneOrTwo = 1
	ClearCmd()
	firstOrSec = PlayFirstOrSecond()
	ClearCmd()
	print("mama, mia...........")
	IntroToGame()
	FrameAndContent(numsTo9)
	for i in range(0,9):
		print()
		#playerInput = input("** "+xO[counter]+" ** Enter position --> ") # -------> INPUT 
		if(firstOrSec == 1):
			firstOrSec = firstOrSec + 1
			oneOrTwo = oneOrTwo -1
		if((i+1) % firstOrSec == oneOrTwo):
			inputForGame = ComputerInput()
		else:
			inputForGame = ValidPlayerInput()  # input from player
			
		ManipulateNumsTo9Arr(inputForGame, counter)# no printing, input and arrNumsto9 manipulation
		ClearCmd()
		IntroToGame()
		numsTo9 = ManipulateNumsTo9Arr(inputForGame, counter)
		counter = counter + 1
		FrameAndContent(numsTo9)
		endOfGame = CheckForWinner(numsTo9)
		if(endOfGame == True):
			print()
			print("WE HAVE A WINNER!!!")
			print("The player with \""+xO[counter-1]+ "\" wins the game.")
			break
	if(endOfGame == False):
		print()
		print("No Winner try again.")
	quit = ContinueOrQuit()