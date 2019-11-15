# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars


while gameVars.player is False:
	print("========================================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("========================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors: \n")
	 
	# start doing some logic and condition checking
	# print("computer: ", computer, "player: ", player)

	# ~~this is where we will do the compare stuff
	
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]