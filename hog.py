"""
Game: Hog
	In Hog, two players alternate turns trying to be the first to end
	a turn with at least 100 total points. On each turn, the current
	player chooses some number of dice to roll, up to 10. That player's
	score for the turn is the sum of the dice outcomes. There are a couple
	of rules to make it more interesting than just rolling dice however...


	Pig Out: If any of the dice outcomes is a 1, the current player's score
	for the turn is 1.

		Example 1: The current player rolls 7 dice, 5 of which are 1's. They
			score 1 point for the turn.
		Example 2: The current player rolls 4 dice, all of which are 3's. Since
			Pig Out did not occur, they score 12 points for the turn.


	Free Bacon: A player who chooses to roll zero dice scores one more than the
	largest digit in the opponent's total score.

		Example 1: If the opponent has 42 points, the current player gains
			1 + max(4, 2) = 5 points by rolling zero dice.
		Example 2: If the opponent has 48 points, the current player gains
			1 + max(4, 8) = 9 points by rolling zero dice.
		Example 3: If the opponent has 7 points, the current player gains
			1 + max(0, 7) = 8 points by rolling zero dice.


	Hogtimus Prime: If a player's score for the turn is a prime number, then the
	turn score is increased to the next larger prime number. For example, if the
	dice outcomes sum to 11, given that none of the dice outcomes are 1, the
	current player scores 13 points for the turn. This boost only applies to the
	current player. Note: 1 is not a prime number!


	Perfect Piggy: If a player's score for the turn is not a 1, but is a perfect
	square or a perfect cube, the player scores the turn score but swaps the
	normal six-sided dice with four-sided dice for all subsequent turns. The next
	time either player activates Perfect Piggy, the six-sided dice will be swapped
	back. Subsequent activations of Perfect Piggy will continue swapping the dice.


	Swine Swap: After the turn score is added, if one of the scores is double the
	other, then the two scores are swapped.

		Example 1: The current player has a total score of 37 and the opponent
			has 92. The current player rolls two dice that total 9. The current
			player's new total score (46) is half of the opponent's score. These
			scores are swapped! The current player now has 92 points and the
			opponent has 46. The turn ends.
		Example 2: The current player has 91 and the opponent has 55. The current
		player rolls five dice that total 17, a prime that is boosted to 19 points
		for the turn (Hogtimus Prime). The current player has 110, so the scores are
		swapped. The opponent ends the turn with 110 and wins the game.
"""
import random

def main():
	while input("Play hog? (yes/no) ") == "yes":
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
	player_scores = [None, 0, 0]

	current_player = 1
	game_state = "In Progress"

	while game_state == "In Progress":
		take_turn(current_player, player_types[current_player], player_scores)

		print("Score: " + str(player_scores[1]) + " - " + str(player_scores[2]))
		print()

		current_player = switch_player(current_player)
		game_state = check_game_state(player_scores)

	print(game_state)
	print('\n')

def take_turn(current_player, player_type, player_scores):
	"""
	Function for player taking a turn. Consists of requesting
	the player to give how many dice to roll, calculating their
	raw total from the rolled dice and then implementing the rules
	listed in the description in order to figure out both players'
	current scores at the end of the turn.

	current_player: either a 1 or 2
	player_scores: a two element list containing the scores before
		this current turn of the two players. We will change the
		scores in this list at the end of the turn to represent the
		players' new scores.
	"""

	# Amount of dice player wants to roll; set to 0 initially and
	# then we request how many dice they want to roll, change the
	# value num_dice accordingly.
	num_dice, turn_score = 0, 0

	if player_type == "user":
		gave_number = False
		while not gave_number:
			try:
				num_dice = int(input("Player " + str(current_player) + ", how many die would you like to roll? (0 - 10) "))
				if num_dice < 0 or num_dice > 10:
					raise AssertionError
				else:
					gave_number = True
			except:
				print("Please enter a number from 0 to 10.")
	else:
		num_dice = cpu_get_num_dice()
		print("Player " + str(current_player) + " will use " + str(num_dice) + " dice.")

	raw_scores = roll_dice(num_dice)
	if num_dice == 1:
		print("Player " + str(current_player) + " rolled a " + str(raw_scores[0]) + ".")
	elif num_dice == 2:
		print("Player " + str(current_player) + " rolled " + str(raw_scores[0]) + " and " + str(raw_scores[1]) + ".")
	elif num_dice > 2:
		roll_string = "Player " + str(current_player) + " rolled "
		for roll in raw_scores[:len(raw_scores) - 1]:
			roll_string += (str(roll) + ", ")
		roll_string += ("and " + str(raw_scores[len(raw_scores) - 1]) + ".")
		print(roll_string)


	turn_score = sum(raw_scores)

	# Write code below to implement the rules of Hog!

	# Pig Out

	# Free Bacon

	# Hogtimus Prime

	# Perfect Piggy

	# Add turn score to current player's score
	player_scores[current_player] += turn_score

	# Swine Swap

def roll_dice(num_dice):
	"""
	This method simulates rolling a specified number
	of dice and returns all the roll values in a list.

	num_dice: the number of dice to roll
	"""
	# Create a list and fill it with random numbers from 1 to the
	# ammount of sides the current dice has. I.e. a normal dice would be 1 - 6,
	# but sometimes it will be a 4 sided dice, so only random numbers from 1 through 4.
	# HINT: Use random.random() for a random number from 0 to 1.

def check_game_state(player_scores):
	"""
	Returns "In Progress" if no player has reached 100 yet.
	Returns "Player 1 won!" if Player 1's score is >= 100.
	Returns "Player 2 won!" if Player 2's score is >= 100.
	"""

def cpu_get_num_dice():
	return int(random.random() * 11)

def switch_player(current_player):
	if current_player == 1:
		return ________
	else:
		return ________

def swap(lst):
	"""
	Assumes lst is a 3-element list and that
	we want to swap lst[1] and lst[2].
	"""

def prime(num):
	return num in primes

def next_prime(num):
	return primes[primes.index(num) + 1]

# -------- Leave everything below as is -------- #

def get_num_sides():
	return num_sides[0]

def set_num_sides(num):
	num_sides[0] = num

# Number of sides on our rolling dice
num_sides = [6]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
squares_and_cubes = [4, 8, 9, 16, 25, 27, 36, 49, 64, 81, 100]

if __name__ == '__main__':
	main()

