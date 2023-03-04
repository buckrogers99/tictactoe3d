import itertools
import os

os.system('clear')

def win(current_game):
	
	def all_same(l) :
		if l.count(l[0]) ==len(l) and l[0] != 0:
			return True
		else:
			return False

	for row in game:
		if all_same(row):
			print(f"Player {row[0]} is the winner in the x axis!")
			return True

	#column win
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])
   
		if all_same(check):
			print(f"Player {check[0]} is the winner in the y axis")
			return True

	#diagonal win in the top right to bottom left
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally")
		return True

	#diagonal win in the top left to bottom right
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally")
		return True

	return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("This position is taken! Choose another!")
			return False
		print("   0  1  2")
		if not just_display:
			game_map[row][column] = player
		for count, _row in enumerate(game_map):
			print(count, _row)
		print()

		return game_map, True
	except IndexError as e:
		print("Error did you input row column as 0 1 or 2", e)
		return game_map, False

	except Exception as e:
		print("Something went wrong!", e)
		return game_map, False

def board_full(current_game):
	zeros = 0
	for x in range(len(current_game)):
		for y in range(len(current_game)):
			if current_game[x][y]==0:
				zeros = zeros + 1
	if zeros == 0:
		return True
	else:
		return False

play = True

while play:
	game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],]
	game_won = False
	game, _ = game_board(game,just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player: {current_player}")
		played = False

		while not played:
			column_choice = int(input("Column: "))
			row_choice = int(input("Row: "))
            
			os.system('clear')
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again? (y/n) ")
			if again.lower() == "y":
				print("restarting")
			elif again.lower() == "n":
				print("Bye bye shithead")
			else:
				print("Not a valid answer, goodbye")
				play = False

		if board_full(game):
			game_won = True
			print("Board full, game over")
			again = input("The game is over, would you like to play again? (y/n) ")
			if again.lower() == "y":
				print("restarting")
			elif again.lower() == "n":
				print("Thank you for playing, goodbye!")
			else:
				print("Not a valid answer, goodbye")
				play = False