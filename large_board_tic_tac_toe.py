"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""

import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random
from pygame_widgets.button import Button


mode = "player_vs_ai"  # default mode for playing the game (player vs AI)

"""
we have to change the initialization of the cxlass to allow for user input"""


class RandomBoardTicTacToe:
    def __init__(
        self, size=(600, 600), grid_size=3, mode="player_vs_ai", player_symbol="X"
    ):

        # i changed grid size to grid size for user input
        self.GRID_SIZE = grid_size
        # this will choose human vs computer
        self.mode = mode
        # this ewill be the players chocie of symbol X or O
        self.player_symbol = player_symbol

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.OFFSET = 5
        # let's make this the default
        self.algorithm = "minimax"
        self.play_mode = "player_vs_ai"

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0] / self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1] / self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()

        # intiialize board as array
        self.board = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)
        # have to add game status to take teh game state
        self.game_state = GameStatus(self.board, True)

        # if depending on symbol, that person goes first
        self.current_player = 1 if self.player_symbol == "X" else 2

        self.draw_game()

        # self.game_reset()
        """
        to draw now we have to define a board, using 2d array/matrix
        where 0 is blank, 1 is a circle, and 2 is an x
        this list will back the grid including the rest of the rows 

        example:

        2 1 0       X O _
        1 0 2  ->   O _ X
        1 2 0       0 X _

        """

    # This will draw the grids
    def draw_game(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)

        # calling the make lines to draw the game
        self.make_lines(self.WHITE)
        pygame.display.update()

        # we first have to define the size using the self.GRID_SIZE that tells
        # us the size of the board
        # board = np.zeros((self.GRID_SIZE, self.GRID_SIZE))

    """
    This function will make lines for the grid and accept a color using the grid lines and such
    - MC
    """

    def make_lines(self, color):
        # using the number of rows to make the lines
        for i in range(1, self.GRID_SIZE):
            pygame.draw.line(
                self.screen,
                color,
                # yhis is start psoition
                (self.WIDTH * i, 0),
                # end position
                (self.WIDTH * i, self.height),
                width=4,
            )
            # now draw the horizontal onmes
        for i in range(1, self.GRID_SIZE):
            pygame.draw.line(
                self.screen,
                color,
                # yhis is start psoition
                (0, self.HEIGHT * i),
                # end position
                (self.size[0], self.HEIGHT * i),
                width=4,
            )

    """
    we have to adjust this function and its place in the rest of the class/game
    I wasnt using it properly but we'll see how it goes
    """

    def change_turn(self):
        """
        we have to base our board
        off 0, 1, 2 or a numpy array to keep track of points and turns
        """
        self.game_state.turn_O = not self.game_state.turn_O
        if self.game_state.turn_O:
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")

    def draw_circle(self, x, y):
        # if it is 1 we draw a O
        if self.board[x][y] == 0:
            # now we have to draw and divide by 2 to ensure we draw in teh circle
            pygame.draw.circle(
                self.screen,
                self.CIRCLE_COLOR,
                (
                    (int(self.WIDTH * x + self.WIDTH // 2)),
                    # below is the y center
                    (int(self.HEIGHT * y + self.HEIGHT // 2)),
                ),
                # below is the x center
                # let's choose a radius
                60,
                5,
            )
            self.board[x][y] = 1

    def draw_cross(self, x, y):
        # this is the player and 2 = X
        if self.board[x][y] == 0:
            # now we have to draw and divide by 2 to ensure we draw in teh circle
            # ************ changed
            # pygame.draw.line(
            # self.screen,
            # self.CROSS_COLOR,
            # start_pos1,
            # end_pos1, 5)
            pygame.draw.line(
                self.screen,
                self.RED,
                (
                    (int(self.WIDTH * x + self.WIDTH // 2) - 50),
                    # below is the y center
                    (int(self.HEIGHT * y + self.HEIGHT // 2) + 50),
                ),
                # below is the x center
                # let's choose a radius
                (
                    (int(self.WIDTH * x + self.WIDTH // 2) + 50),
                    # below is the y center
                    (int(self.HEIGHT * y + self.HEIGHT // 2) - 50),
                ),
                5,
            )
            pygame.draw.line(
                self.screen,
                self.RED,
                (
                    (int(self.WIDTH * x + self.WIDTH // 2) - 50),
                    # below is the y center
                    (int(self.HEIGHT * y + self.HEIGHT // 2) - 50),
                ),
                # below is the x center
                # let's choose a radius
                (
                    (int(self.WIDTH * x + self.WIDTH // 2) + 50),
                    # below is the y center
                    (int(self.HEIGHT * y + self.HEIGHT // 2) + 50),
                ),
                5,
            )
            self.board[x][y] = 2

            """
            pygame.draw.line(
                screen,
                color,
                (columns * self.GRID_SIZE + self.GRID_SIZE // 4),
                (rows * self.GRID_SIZE + self.GRID_SIZE // 4),
            )
            """

    def is_game_over(self):
        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)

        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
        # not sure if this code is right
        # *************************************** check this later!!! **************************
        if self.game_state.is_terminal():
            # we will get scores if it is terminal
            scores = self.game_state.get_scores()
            if scores["winner"] is not None:
                print(f"Player {scores['winner']} wins!")
            else:
                print("It's a draw!")
            return True
        return False

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)

    """
    this code will select an algorithm or use the user sleected algorithm and initiate game play
    draws the AI's moves once the AI is chosen
    """


    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)

        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        # we will default to minimax, but this may changed based on GUI
        # basically alg = "minimax"
        _, best_move = minimax(self.game_state, depth=3, maximizingPlayer=True)
        # now lets actually make the best move we got
        # error handling bc it cant be none
        if best_move != None:
            # best move will be a grid placement so we need xy
            x, y = best_move
            # we draw the move depedning on player mark
            if self.current_player == 1:
                self.draw_cross(x, y)
            else:
                self.draw_circle(x, y)

            # now we update the game and change turns
            # Check if the game is over
        if self.game_state.is_terminal():
            terminal = True
            scores = self.game_state.get_scores(terminal)
            print(f"Final scores: {scores}")
        else:
            terminal = False

        self.change_turn()
        pygame.display.update()

        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.get_scores(terminal)
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """

    def game_reset(self):
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        self.board = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)
        # reset game and e=current player
        self.game_state = GameStatus(self.board, True)
        self.current_player = 1 if self.player_symbol == "X" else 2
        # redraw game
        self.draw_game()

    """
    now that we did play_ai,
    we want to make it so we switch form the playyer mofe to the AI mode aka switch turns
    - mc"""

    def play_game(self, mode="player_vs_ai"):
        Run = True

        clock = pygame.time.Clock()

        while Run:
            for event in pygame.event.get():  # User did something
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                if event.type == pygame.QUIT:
                    Run = False

                # after the player has moved, we will check thier mouse click (not exit)
                if (event.type == pygame.MOUSEBUTTONDOWN) and (
                    self.current_player == 1
                ):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    gridX = int(mouseX // self.WIDTH)
                    gridY = int(mouseY // self.HEIGHT)
                    # error handling to make sure the grid is empty before they click it:
                    if (
                        (0 <= gridX < self.GRID_SIZE)
                        and (0 <= gridY < self.GRID_SIZE)
                        and (self.board[gridX][gridY] == 0)
                    ):

                        """
                             if self.player_symbol == "X":
                                self.draw_cross(gridX, gridY)
                            else:
                                self.draw_circle(gridX, gridY)
                            # switch depending on the game mode
                            if self.mode == "player_vs_ai":
                                self.current_player = 2
                            else:
                                self.current_player = 1 if self.current_player == 2 else 2

                        if self.current_player == 2 and self.mode == "player_vs_ai":
                            self.play_ai()
                            self.current_player = 1
                        """
                        # again we consider ythe player's charcter/symbol
                        if self.current_player == 1 and self.player_symbol == "X":
                            self.draw_cross(gridX, gridY)
                            self.current_player = 2
                        # elif self.current_player == 1 and self.player_symbol == 'O':
                        #   self.draw_circle(gridX, gridY)
                        #  self.current_player = 2
                        if self.current_player == 2 and self.mode == "player_vs_ai":
                            self.play_ai()
                            self.current_player = 1

                        if self.is_game_over() == True:
                            pygame.quit()

            pygame.display.update()
            clock.tick(30)

        pygame.quit()

        """
        YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
        THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
        """

        """
        YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
        IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
        DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
        PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
        """

        # Change the x/y screen coordinates to grid coordinates

        # Check if the game is human vs human or human vs AI player from the GUI.
        # If it is human vs human then your opponent should have the value of the selected cell set to -1
        # Then draw the symbol for your opponent in the selected cell
        # Within this code portion, continue checking if the game has ended by using is_terminal function


"""
added main menu to incoporate GUI absed off the board file eduardo made


************ please note that the 5x5 is not working too well when it comes to highlighting it
ALSO, note that the game does NOT have a quit button
we should look into that

Further, if the user does NOT select one of the options and tries to click start, the window will crash;
therefore, we need error handling for that in the next sprint
"""


# main menu GUI to select options and start the game
def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    pygame.display.set_caption("Tic Tac Toe Options")
    # sets look going
    running = True
    n = 3
    mode = "player_vs_ai"
    symbol = "X"
    white = (255, 255, 255)
    # will be used to highlight options
    green = (0, 255, 0)

    # text settings function
    def generate_text(text, colors, font_size):
        font = pygame.font.Font(None, font_size)
        return font.render(text, True, colors)

    # making all the buttons for the GUI

    # this covers the start buttons including the opponent/mode
    def start_button(selected_color, unselected_color):
        # Select Opponent
        screen.blit(generate_text("Select Opponent", white, 20), (195, 59))
        pygame.draw.rect(screen, white, (124, 45, 250, 100), width=3)
        pygame.draw.circle(
            screen,
            selected_color if mode == "player_vs_ai" else unselected_color,
            (195, 89),
            8,
            3,
        )
        # AI or human vs human
        screen.blit(generate_text("You vs. Computer", white, 16), (215, 84))
        pygame.draw.circle(
            screen,
            selected_color if mode == "player_vs_player" else unselected_color,
            (195, 119),
            8,
            3,
        )
        screen.blit(generate_text("You vs. Person", white, 16), (215, 115))

        # this part generates where the user will select X or O
        screen.blit(generate_text("Select X or O", white, 20), (205, 183))
        pygame.draw.rect(screen, white, (124, 166, 250, 100), width=3)
        pygame.draw.circle(
            screen,
            selected_color if symbol == "X" else unselected_color,
            (195, 213),
            8,
            3,
        )
        screen.blit(generate_text("Select X", white, 16), (215, 208))
        pygame.draw.circle(
            screen,
            selected_color if symbol == "O" else unselected_color,
            (195, 243),
            8,
            3,
        )
        screen.blit(generate_text("Select O", white, 16), (215, 238))

        # this part is to select grid size
        """
        ************************PLS note that the 5x5 doesnt work as it should and i dont know why, but take a 
        look at lmk if you fudn anything
        by selecting 5x5, it goes to 4x4
        ***********************************************
        """
        screen.blit(generate_text("Select Grid Size", white, 20), (700, 59))
        pygame.draw.rect(screen, white, (625, 45, 250, 100), width=3)
        pygame.draw.circle(
            screen, selected_color if n == 3 else unselected_color, (700, 89), 8, 3
        )
        screen.blit(generate_text("3 x 3", white, 16), (720, 85))
        pygame.draw.circle(
            screen, selected_color if n == 4 else unselected_color, (775, 89), 8, 3
        )
        screen.blit(generate_text("4 x 4", white, 16), (795, 85))
        pygame.draw.circle(
            screen, selected_color if n == 5 else unselected_color, (700, 119), 8, 3
        )
        screen.blit(generate_text("5 x 5", white, 16), (720, 114))

        # START Button
        pygame.draw.rect(screen, white, (625, 166, 250, 100), width=3)
        screen.blit(generate_text("START", white, 24), (725, 205))

    while running:
        # fills with black
        screen.fill((0, 0, 0))
        start_button(green, white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos

                # select Opponent
                if 124 < mouseX < 374 and 45 < mouseY < 145:
                    if 70 < mouseY < 100:
                        mode = "player_vs_ai"
                    elif 115 < mouseY < 145:
                        mode = "player_vs_player"

                # select X or O
                if 124 < mouseX < 374 and 166 < mouseY < 266:
                    if 200 < mouseY < 225:
                        symbol = "X"
                    elif 230 < mouseY < 260:
                        symbol = "O"

                # I got the grid size to work, it allows you to pick 4x4 and 5x5 now - ER
                # select Grid Size
                if 690 < mouseX < 705:  # and 45 < mouseY < 145:
                    if 70 < mouseY < 100:
                        n = 3
                    elif 110 < mouseY < 150:
                        n = 5

                elif 770 < mouseX < 780:
                    if 70 < mouseY < 100:
                        n = 4

                # start Game
                if 625 < mouseX < 875 and 166 < mouseY < 266:
                    running = False

        pygame.display.update()

    pygame.quit()

    # instantiate and play the game with the selected options wooo
    tictactoegame = RandomBoardTicTacToe(
        size=(1000, 900), grid_size=n, mode=mode, player_symbol=symbol
    )
    tictactoegame.play_game(mode)


if __name__ == "__main__":
    main()
