# -*- coding: utf-8 -*-


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
		for row in range(self.GRID_SZE):
			for col in range(self.GRID_SIZE):
				if (self.board[row][col] == 0):
					# there is a 0 therefore the game is not terminal/done
					return False
		# otherwise, lets check the wiining player by checking the score
		player_score, p2_score = self.get_scores()
		# we now check for draw or p1 or p2 wnning
		if (player_score > p2_score):
			return 'Player 1 wins!'
		elif (player_score < p2_score):
			return 'Player 2 wins!'
		else:
			return 'Draw'
		

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
		check_point = 3 if terminal else 2
		# we will have to check the rows, columns, and diagonals

		# lets check rows first
		for rows in range(rows):
			# check rows
			# we have to have the -2 to make sure we dont go ou of bounds
			for col in range(cols-check_point +1):
				# the if statement below says if 0,0 0,1 or 0,3 are NOT 0 and then seeing 
				# if they are either a row of 1 or 2 (0 or X) then it is a point
				if (all(self.board_state[row,col+i] == self.board_state[row][col])):
					# if that is true lets check if it is a X or a 0 (remember 0 is 1 and 2 is X)
					if (self.board_state[row][col] == 2):
						# if there is a row of X, player 2 or AI wins
						score -= 1
					else:
						# if there is a row of 0, player 1 wins
						score += 1
		
		# now let's check the columns
		for col in range(cols):
			for row in range(rows-check_point):
				if (all(self.board_state[row + i,col] == self.board_state[row][col] !=0 for i in range(check_point))):
				# if that is true lets check if it is a X or a 0 (remember 0 is 1 and 2 is X)
					if (self.board_state[row][col] == 2):
						# if there is a row of X, player 2 or AI wins
						score -= 1
					else:
						# if there is a row of 1, player 1 wins
						score += 1
		'''
		These might definitely be wrong, i didnt know how to use checkpoint here??
		'''
		# now we check diagonal of 11 22 33 or 00 11 22 aka the \ and next we check the / diagonal
		if (self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] !=0):
			# we see what values they have
			if self.board_state[0][0] == 1:
				score += 1
			else:
				score -=1
		
		# now we check the other diagonal
		if (self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] !=0):
			# we see what values they have
			if self.board_state[0][2] == 1:
				score += 1
			else:
				score -=1
		# finally, we return final score
		return score

		
	    

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
	    

	def get_moves(self):
		moves = []
		"""
        YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
        MINIMAX OR NEGAMAX FUNCTIONS
        """
		# we will ahve to iterate through rows and columns to count number of empty cells
		# we need to check if there are still 0's on the board aka new moves to be found
		if (self.game_state == 0):
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
		x, y = move[0], move[1]
		new_board_state[x,y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
'''
Resources below:

https://www.youtube.com/watch?v=LbTu0rwikwg

'''