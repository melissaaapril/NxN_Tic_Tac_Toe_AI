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
		return moves

	# 
	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x,y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
'''
Resources below:

https://www.youtube.com/watch?v=LbTu0rwikwg

'''