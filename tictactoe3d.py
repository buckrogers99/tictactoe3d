import itertools

def win(current_game):
	
	def all_same(l) :
		if l.count(l[0]) ==len(l) and l[0] != 0:
			return True
		else:
			return False

	#row win
	for layer in game:
		for row in layer:
			if all_same(row):
				print(f"Player {row[0]} is the winner in the x axis!")
				return True

	#column win
	for layer in game:
		for col in range(len(layer)):
			check = []

			for row in layer:
				check.append(row[col])

			if all_same(check):
					print(f"Player {check[0]} is the winner in the y axis")
					return True

	#diagonal win in the same layer
	for layer in game:
		diags = []
		for col, row in enumerate(reversed(range(len(game)))):
			diags.append(layer[row][col])
		if all_same(diags):
				print(f"Player {diags[0]} is the winner diagonally in the x-y axis")
				return True

	#diagonal win in the same layer
	for layer in game:
		diags = []
		for ix in range(len(game)):
			diags.append(layer[ix][ix])
		if all_same(diags):
				print(f"Player {diags[0]} is the winner diagonally in the x-y axis")
				return True

	#vertical win
	for rows in range(len(game)):
		for col in range(len(game)):
			vert = []
			for ix in range(len(game)):
				vert.append(game[ix][rows][col])
			if all_same(vert):
				print(f"Player {vert[0]} is the winner in the z axis!")
				return True

	#diagonal win in the z-x plane
	for row in range(len(game)):
		diags = []
		for ix in range(len(game)):
			diags.append(game[ix][row][ix])
		if all_same(diags):
			print(f"Player {diags[0]} is the winner diagonally in the z-x plane!")
			return True

	#diagonal win in the z-x plane
	for row in range(len(game)):
		diags = []
		for col, layer in enumerate(reversed(range(len(game)))):
			diags.append(game[layer][row][col])
		if all_same(diags):
			print(f"Player {diags[0]} is the winner diagonally in the z-x plane!")
			return True

	#diagonal win in the z-y plane
	for col in range(len(game)):
		diags = []
		for ix in range(len(game)):
			diags.append(game[ix][ix][col])
		if all_same(diags):
			print(f"Player {diags[0]} is the winner diagonally in the z-y plane!")
			return True

	#diagonal win in the z-y plane
	for col in range(len(game)):
		diags = []
		for row, layer in enumerate(reversed(range(len(game)))):
			diags.append(game[layer][row][col])
		if all_same(diags):
			print(f"Player {diags[0]} is the winner diagonally in the z-x plane!")
			return True

	diags = []
	for x in range(len(game)):
		diags.append(game[x][x][x])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner corner to corner")

	diags = []
	for x, y in enumerate(reversed(range(len(game)))):
		diags.append(game[y][x][x])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner corner to corner")

	diags = []
	for x, y in enumerate(reversed(range(len(game)))):
		diags.append(game[x][y][x])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner corner to corner")

	diags = []
	for x, y in enumerate(reversed(range(len(game)))):
		diags.append(game[x][x][y])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner corner to corner")

	return False

def game_board(game_map, player=0, layer=0, row=0, column=0, just_display=False):
	try:
		if game_map[layer][row][column] != 0:
			print("This position is taken! Choose another!")
			return layers, False
		print("   0  1  2")
		if not just_display:
			game_map[layer][row][column] = player
		for count, row in enumerate(game_map[0]):
			print(count, row)
		print()
		for count, row in enumerate(game_map[1]):
			print(count, row)
		print()
		for count, row in enumerate(game_map[2]):
			print(count, row)
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
			for z in range(len(current_game)):
				if current_game[x][y][z]==0:
					zeros = zeros + 1
	if zeros == 0:
		return True
	else:
		return False

play = True

while play:
	game = [[[0, 0, 0],
			 [0, 0, 0],
			 [0, 0, 0],],
			[[0, 0, 0],
			 [0, 0, 0],
			 [0, 0, 0],],
			[[0, 0, 0],
			 [0, 0, 0],
			 [0, 0, 0],],]
	game_won = False
	game, _ = game_board(game,just_display=True)
	player_choice = itertools.cycle([1, 2, 3])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player: {current_player}")
		played = False

		while not played:
			layer_choice = int(input("Layer: "))
			column_choice = int(input("Column: "))
			row_choice = int(input("Row: "))
			print()
			game, played = game_board(game, current_player, layer_choice, row_choice, column_choice)

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
				print("Bye bye shithead")
			else:
				print("Not a valid answer, goodbye")
				play = False
