from GameStatus_5120 import GameStatus


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
	terminal = game_state.is_terminal()
	if (depth==0) or (terminal):
		newScores = game_state.get_scores(terminal)
		return newScores, None
    
	if maximizingPlayer == True:
		maxEval = float('-inf')
		best_move = None # track best move
		for move in game_state.get_moves(): #iterate over all possible moves in current game state
			child_state = game_state.get_new_state(move) #generate gamestate from making this move
			eval, _ = minimax(child_state, depth - 1, False, alpha, beta) #recusively call minimax for the minimizing player
			if eval > maxEval: #conditional to update maxeval if evaluation score is better.
				maxEval = eval
				best_move = move
			if beta <= maxEval: #alpha beta pruning. if beta <= alpha, we stop considering other moves, because minimizing player wouldnt allow this outcome
				break
			alpha = max(alpha, maxEval) #update alpha
		return maxEval, best_move # returns best score
    else:
        minEval = float('inf')
        best_move = None

        for move in game_state.get_moves(): #same  logic as above
            child_state = game_state.get_new_state(move) 

            eval, _ = minimax(child_state, depth - 1, True, alpha, beta) 

            if eval < minEval: 
                minEval = eval
                best_move = move 

            if beta >= minEval: 
                break
            beta = min(beta, minEval) 
        return minEval, best_move

        
	"""
    YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """

	# return value, best_move



def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	terminal = game_status.is_terminal()
	if (depth==0) or (terminal):
		scores = game_status.get_negamax_scores(terminal)
		return scores, None

	"""
    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    
    """
    #return value, best_move