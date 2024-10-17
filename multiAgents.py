# multiAgents.py
from GameStatus_5120 import GameStatus

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
    # check if game is over or depth limit is reached
    terminal = game_state.is_terminal()
    if depth == 0 or terminal:
        newScores = game_state.get_scores(terminal)
        return newScores, None  # return score if terminal or max depth

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        for move in game_state.get_moves():
            # evaluate child state assuming minimizing play
            child_state = game_state.get_new_state(move)
            eval, _ = minimax(child_state, depth - 1, False, alpha, beta)
            if eval > maxEval:  # update best score and move if higher
                maxEval = eval
                best_move = move
            alpha = max(alpha, eval)  # update alpha
            if beta <= alpha:  # alpha-beta pruning
                break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in game_state.get_moves():
            # evaluate child state assuming maximizing play
            child_state = game_state.get_new_state(move)
            eval, _ = minimax(child_state, depth - 1, True, alpha, beta)
            if eval < minEval:  # update best score and move if lower
                minEval = eval
                best_move = move
            beta = min(beta, eval)  # update beta
            if beta <= alpha:  # alpha-beta pruning
                break
        return minEval, best_move

def negamax(game_state: GameStatus, depth: int, color: int, alpha=float('-inf'), beta=float('inf')):
    # check if game is over or depth limit is reached
    terminal = game_state.is_terminal()
    if depth == 0 or terminal:
        scores = color * game_state.get_negamax_scores(terminal)
        return scores, None  # return score adjusted for current player

    maxEval = float('-inf')
    best_move = None
    for move in game_state.get_moves():
        # evaluate child state from opponent's perspective
        child_state = game_state.get_new_state(move)
        eval, _ = negamax(child_state, depth - 1, -color, -beta, -alpha)
        eval = -eval  # reverse score for current player's perspective
        if eval > maxEval:  # update best score and move if higher
            maxEval = eval
            best_move = move
        alpha = max(alpha, eval)  # update alpha
        if alpha >= beta:  # alpha-beta pruning
            break
    return maxEval, best_move


