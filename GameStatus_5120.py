# GameStatus_5120.py
import numpy as np

class GameStatus:
    def __init__(self, board_state, player_turn):
        self.board_state = board_state  # game board matrix
        self.player_turn = player_turn  # 1 for human, -1 for AI
        self.winner = ""  # track winner

    def is_terminal(self):
        # check if there are any empty cells. if none, game over
        if np.any(self.board_state == 0):
            return False  # game is ongoing
        else:
            # determine winner if no empty cells
            score = self.get_scores(terminal=True)
            if score > 0:
                self.winner = "Human"
            elif score < 0:
                self.winner = "AI"
            else:
                self.winner = "Draw"
            return True  # game is over

    def get_scores(self, terminal):
        rows = self.board_state.shape[0]
        cols = self.board_state.shape[1]
        scores = 0

        # check rows for any triplets of 1s or -1s
        for i in range(rows):
            for j in range(cols - 2):
                triplet = self.board_state[i, j:j+3]
                if np.all(triplet == 1):
                    scores += 1
                elif np.all(triplet == -1):
                    scores -= 1

        # check columns for triplets
        for i in range(rows - 2):
            for j in range(cols):
                triplet = self.board_state[i:i+3, j]
                if np.all(triplet == 1):
                    scores += 1
                elif np.all(triplet == -1):
                    scores -= 1

        # check diagonals for triplets
        for i in range(rows - 2):
            for j in range(cols - 2):
                # main diagonal
                triplet = [self.board_state[i+k, j+k] for k in range(3)]
                if all(x == 1 for x in triplet):
                    scores += 1
                elif all(x == -1 for x in triplet):
                    scores -= 1

                # anti-diagonal
                triplet = [self.board_state[i+2-k, j+k] for k in range(3)]
                if all(x == 1 for x in triplet):
                    scores += 1
                elif all(x == -1 for x in triplet):
                    scores -= 1

        return scores

    def get_negamax_scores(self, terminal):
        # negamax uses same scoring function
        return self.get_scores(terminal)

    def get_moves(self):
        moves = []
        rows, cols = self.board_state.shape
        # check each cell for possible moves
        for i in range(rows):
            for j in range(cols):
                if self.board_state[i, j] == 0:
                    moves.append((i, j))  # add empty cell coordinates
        return moves

    def get_new_state(self, move):
        new_board_state = self.board_state.copy()  # create copy of board
        x, y = move[0], move[1]
        new_board_state[x, y] = self.player_turn  # apply move
        return GameStatus(new_board_state, -self.player_turn)  # switch player turn
