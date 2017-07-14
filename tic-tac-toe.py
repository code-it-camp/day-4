import random

def main():
	while input("Play Tic-Tac-Toe? (yes/no) ").lower() == "yes":
		game(int(input("How many players? (0/1/2) ")))

def game(num_users):
	"""
	Designates what type each player is, what their initial scores are,
	and starts game loop. Each iteration of the game loop represents a player's turn.
	"""
	player_types = [
		None,
		"user" if num_users != 0 else "cpu",
		"user" if num_users == 2 else "cpu"
	]

	current_player = 1
	game_state = "In Progress"

	while game_state == "In Progress":
		take_turn(player_types[current_player], current_player)

		current_player = switch_player(current_player)
		game_state = check_game_state()

		print("Player " + str(current_player) + "'s Move:")
		print_board()

	print(game_state)
	reset_board()

def take_turn(player_type, current_player):
	target = ""
	while ________:
		# either "user" or "cpu"
		if player_type == ________:
			target = input("Place an " + symbol_dictionary[current_player] + ": ")
		else:
			target = cpu_get_target()

	place_symbol(target, current_player)

def valid(target):
	# Prerequisite 1: Target must consist of one letter and one number with no spaces.
	if len(target) != ________ or len(target) != ________:
		return False

	# Prerequisite 2: Target's letter must be either "a", "b" or "c" and
	# the target's number must be 1, 2, or 3.
	if target[________:________].lower() not in target_dictionary.keys():
		print("Position must be on board.")
		return False
	if int(target[________:________]) not in range(________, ________ + 1):
		print("Position must be on board.")
		return False

	# coord is a two-element tuple of numbers, for example (1, 2), it
	# represents the target's y and x indices
	coord = target_to_coord(target)

	# Prerequisite 3: If the target has a symbol at that position on board,
	# it is not a valid target to place a symbol.
	if board[________][________] != "-":
		print("Can't place piece here.")
		return False

	# If all the above prerequisites are met, then the target is valid!
	return True

def place_symbol(target, current_player):
	# coord is a two-element tuple of numbers, for example (1, 2), it
	# represents the target's y and x indices
	coord = target_to_coord(target)

	# We want to place the current player's symbol on the board at the
	# specified target.
	board[________][________] = symbol_dictionary[________]

def target_to_coord(target):
	return (target_dictionary[target[________:________]] - 1, int(target[________:________]) - 1)

def check_game_state():
	"""
	Checks the board for three different states:
	Game Over, In Progress and Cat's Game.
	"""

	# Condition 1: Game Over; One Player Won
	for symbol in ["X", "O"]:
		# Case 1: Horizontal Win

		# Fill in blank with the correct value for how tall
		# our board is.
		for i in range(________):
			this_row = True
			# Fill in blank with the correct value for how wide our
			# board is.
			for j in range(________):
				if board[i][j] != symbol:
					this_row = False
					break
			if this_row:
				return symbol + " won!"

		# Case 2: Vertical Win

		# Fill in blank with the correct value for how wide our
		# board is.
		for j in range(________):
			this_col = True
			# Fill in blank with the correct value for how tall
			# our board is.
			for i in range(________):
				if board[i][j] != symbol:
					this_col = False
					break
			if this_col:
				return symbol + " won!"

		# Case 3: Diagonal Win
		# Fill in blanks with correct indices on the board to give
		# the positions for a diagonal win.
		if board[0][0] == symbol
			and board[________][________] == symbol
			and board[________][________] == symbol:
			return symbol + " won!"
		elif board[0][2] == symbol
			and board[________][________] == symbol
			and board[________][________] == symbol:
			return symbol + " won!"

	# Condition 2: In Progress
	for row in board:
		# If neither player has won the game yet, but there
		# are still these symbols on the board, then the game
		# is still in progress. Fill in the blank with the correct string.
		if ________ in row:
			return "In Progress"

	# Condition 3: Cat's Game
	return "Cat's Game"

def switch_player(current_player):
	# if current_player is 1, switch to 2 and vice versa.
	if current_player == 1:
		return ________
	else:
		return ________

# -------- Leave below as is -------- #

def reset_board():
	for row in board:
		for i in range(len(row)):
			row[i] = "-"

def print_board():
	print("  " + " ".join([" " + str(i) for i in range(1, 3 + 1)]))

	for letter in target_dictionary.keys():
		i = target_dictionary[letter] - 1
		print(letter + " " + " ".join([" " + board[i][j] for j in range(3)]))
	print()

def cpu_get_target():
	valid_placements = []
	for letter in target_dictionary.keys():
		for i in range(len(board[0])):
			coord = target_to_coord(letter + str(i + 1))
			if board[coord[0]][coord[1]] == "-":
				valid_placements.append(letter + str(i + 1))
	return valid_placements[int(random.random() * len(valid_placements))]

board = [
	["-", "-", "-"],
	["-", "-", "-"],
	["-", "-", "-"]
]
target_dictionary = {"a": 1, "b": 2, "c": 3}
symbol_dictionary = {1: "X", 2: "O"}

if __name__ == '__main__':
	main()
