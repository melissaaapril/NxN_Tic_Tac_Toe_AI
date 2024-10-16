'''
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
 
'''
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random
from pygame_widgets.button import Button


mode = "player_vs_ai" # default mode for playing the game (player vs AI)


class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 3
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1]/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
        # initislize boatrd with numpy array
        self.board = np.zeros((self.GRID_SIZE, self.GRID_SIZE))

        '''
        lets draw the GUI into here including buttons'''
        # we will default to algorithm minimax for now
        self.alg = "minimax"

        # initialize buttons/dropdowns
        self.create_button = None
        self.x_nought = None

        self.game_reset()
        '''
        to draw now we have to define a board, using 2d array/matrix
        where 0 is blank, 1 is a circle, and 2 is an x
        this list will back the grid including the rest of the rows 

        example:

        2 1 0       X O _
        1 0 2  ->   O _ X
        1 2 0       0 X _

        '''
    # This will draw the grids
    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)

        # calling the make lines to draw the game
        self.make_lines(self.WHITE)

        pygame.display.update()

        
    '''
    This function will make lines for the grid and accept a color using the grid lines and such
    - MC
    '''
    def make_lines(self, color):
        # using the number of rows to make the lines
        for i in range(1, self.GRID_SIZE):
            pygame.draw.line(
                self.screen, 
                color, 
                # yhis is start psoition
                (self.WIDTH *i, 0), 
                # end position
                (self.WIDTH * i, self.height),
                width = 4)
            # now draw the horizontal onmes
        for i in range(1, self.GRID_SIZE):
            pygame.draw.line(
                self.screen,
                color,
                # yhis is start psoition
                (0, self.HEIGHT *i),
                # end position
                (self.size[0], self.HEIGHT * i),  
                width = 4)
    '''
    this function will create the drop down for the character or x or 0 select

    def x_nought_select(self):
        self.x_nought_select = Dropdown(
            self.screen, 120, 10, 100, 50, name='Select Your Mark',
            choices=['X', 'O'],
            borderRadius=3, colour=pygame.Color('green'), values=['X', 'O'], direction='down', textHAlign='left'
        )
    '''


    def change_turn(self):
        '''
        we have to base our board
        off 0, 1, 2 or a numpy array to keep track of points and turns
        '''
        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        # if it is 1 we draw a O
        if self.board[x][y] == 1:
            # now we have to draw and divide by 2 to ensure we draw in teh circle
            pygame.draw.circle(self.screen, 
            self.CIRCLE_COLOR, 
            #below is the x center
            (int(self.WIDTH * x + self.WIDTH // 2)), 
            # below is the y center
            (int(self.HEIGHT * y + self.HEIGHT // 2)),
            # let's choose a radius
            10,
            5)
        

    def draw_cross(self, x, y):
        # this is the player and 2 = X
        if self.board[x][y] == 2:
            # now we have to draw and divide by 2 to ensure we draw in teh circle
            pygame.draw.line(screen, 
            color, 
            (columns * self.GRID_SIZE + self.GRID_SIZE // 4), 
            (rows * self.GRID_SIZE + self.GRID_SIZE //4),
            )       
        

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
        # not sure if this code is right because there must me more to it no?
        # *************************************** check this later!!! **************************
        return self.is_terminal()
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)

    '''
    this code will select an algorithm or use the user sleected algorithm and initiate game play
    draws the AI's moves once the AI is chosen
    '''
    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        # we will default to minimax, but this may changed based on GUI
        alg = "minimax"

        # lets let the player choose the character
        if x_nought == 'X':
            x_nought = 2
        else:
            x_nought = 1

        if (alg =="minimax"):
            # minimax params: game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')
            # maximizing is True since AI will amke a move now
            _, best_move = minimax(self.board, True)
        
        # now lets actually make the best move we got
        # error handling bc it cant be none
        if (best_move != None):
            # best move will be a grid placement so we need xy
            x,y = best_move
            # we mark the choice on the board
            selfboard[x][y] = x_nought if self.game_state.turn_O else 2
            # we draw the move
            if self.game_state.turn_O:
                self.draw_circle(x, y)
            else:
                self.draw_cross(x, y)

        # now we have to change the turn
        self.change_turn()
        pygame.display.update()

        if self.is_game_over():
            # if game over, display the score and update UI
            terminal = self.game_state.is_terminal()

        
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """



    def game_reset(self):
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        
        pygame.display.update()
        

    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()


        while not done:
            for event in pygame.event.get():  # User did something
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                
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
                if event.type == pygame.QUIT:
                    done = True
                # if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    
                    # Change the x/y screen coordinates to grid coordinates
                    
                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
                if self
            pygame.display.update()

        pygame.quit()


tictactoegame = RandomBoardTicTacToe()


"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""
