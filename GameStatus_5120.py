	# -*- coding: utf-8 -*-
import numpy as np

class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""

	''' 
	YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. IF THERE IS NO EMPTY
		THEN YOU SHOULD ALSO RETURN THE WINNER OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER
	'''
	def is_terminal(self):
		# use the np array to check if any cell is 0 aka, there game is not yet done and there
		# ia still space left on the board
		"""
		Check if the game has ended. Returns True if the game is over, otherwise False.
		"""
		# Check rows and columns for a win
		for i in range(len(self.board_state)):
			# Check rows
			if np.all(self.board_state[i, :] == 1) or np.all(self.board_state[i, :] == 2):
				self.winner = "Player 1" if np.all(self.board_state[i, :] == 1) else "Player 2"
				return True

			# this will check the columns
			if np.all(self.board_state[:, i] == 1) or np.all(self.board_state[:, i] == 2):
				self.winner = "Player 1" if np.all(self.board_state[:, i] == 1) else "Player 2"
				return True

			# check diagonals for a win
			if np.all(np.diag(self.board_state) == 1) or np.all(np.diag(self.board_state) == 2):
				self.winner = "Player 1" if np.all(np.diag(self.board_state) == 1) else "Player 2"
				return True
			# other diagonal
			if np.all(np.diag(np.fliplr(self.board_state)) == 1) or np.all(np.diag(np.fliplr(self.board_state)) == 2):
				self.winner = "Player 1" if np.all(np.diag(np.fliplr(self.board_state)) == 1) else "Player 2"
				return True

			# check fi the board is full
			if not np.any(self.board_state == 0):
				self.winner = "Draw"
				return True

		# if board not full, game is not over
		return False
		

	def get_scores(self, terminal):
		'''
		******************************************Check this one*****************************
		did we use the cols/range right??? what do i do with the check_point variable???
		'''
		"""
		YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
		EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)

		YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
		NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
		"""        
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		# we will have to check the rows, columns, and diagonals
		'''
		this code will be based hevaily hevaily on abdul's code for the get scores function
		thank you abdul
		'''
		# lets check rows first
		for i in range(rows):
			# check rows
			# we have to have the -2 to make sure we dont go ou of bounds
			for j in range(cols-2):
				# the if statement below says if 0,0 0,1 or 0,3 are NOT 0 and then seeing 
				# if they are either a row of 1 or 2 (0 or X) then it is a point
				triplet = self.board_state[i, j:j+3]
				# if that is true lets check if it is a X or a 0 (remember 0 is 1 and 2 is X)
				if np.all(triplet == 1):
					# if there is a row of O, player 2 or AI wins
					scores += 1
				elif np.all(triplet == 2):
					# if there is a row of 2, player 1 wins
					scores -= 1
		
		# now let's check the columns
		for i in range(rows - 2):
			for j in range(cols):
				triplet = self.board_state[i:i+3, j]
				if np.all(triplet == 1):  # Player 1 (or O)
					scores += 1
				elif np.all(triplet == 2):  # Player 2 (or X)
					scores -= 1

		# now we check diagonal of 11 22 33 or 00 11 22 aka the \ and next we check the / diagonal
		for i in range(rows - 2):
			for j in range(cols - 2):
				# first diagonal
				triplet = [self.board_state[i+k, j+k] for k in range(3)]
				if all(x == 1 for x in triplet):  # Player 1 (or O)
					scores += 1
				elif all(x == 2 for x in triplet):  # Player 2 (or X)
					scores -= 1

				# the other diagonal
				triplet = [self.board_state[i+2-k, j+k] for k in range(3)]
				if all(x == 1 for x in triplet):  # Player 1 (or O)
					scores += 1
				elif all(x == 2 for x in triplet):  # Player 2 (or X)
					scores -= 1
		# finally, we return final score
		return scores

		
	    
	'''
	this is on the back burner for now
	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
	'''

	def get_moves(self):
		moves = []
		"""
        YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
        MINIMAX OR NEGAMAX FUNCTIONS
        """
		# we will ahve to iterate through rows and columns to count number of empty cells
		# we use the same logic as in egt scores to check if there are 0s on board
		rows = len(self.board_state)
		cols = len(self.board_state[0])

		# now check the rows and columns for mvoes
		for row in range(rows):
			for col in range(cols):
				# of this specific board place is a 0, save the board space
				if (self.board_state[row][col] == 0):
					moves.append((row,col))
		#return list of moves
		return moves

	# gets new state for board
	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move
		new_board_state[x,y] = 1 if self.turn_O else 2
		return GameStatus(new_board_state, not self.turn_O)
'''
Resources below:

https://www.youtube.com/watch?v=LbTu0rwikwg

'''