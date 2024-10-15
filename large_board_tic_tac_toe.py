# large_board_tic_tac_toe.py

import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys
import colorsys  # hsv to rgb conversion
import sounds    # import sounds from sounds.py

class RandomBoardTicTacToe:
    def __init__(self, size=(600, 600)):
        self.size = self.width, self.height = size

        # dynamic size section
        self.grid_size = 3  
        self.depth = 3      
        self.algorithm = "minimax"  

        # defining colors for test purposes
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.GRAY = (200, 200, 200)
        self.DARK_GRAY = (50, 50, 50)
        self.BLUE = (0, 0, 255)

        # Initialize OFFSET
        self.OFFSET = 5

        # RGB background
        self.hue = 0  # Start hue at 0
        self.color_speed = 5  # Fixed color speed at 5

        # Initialize pygame/sounds
        pygame.init()
        sounds.init_sounds()

    def draw_game(self):
        # Grid Size/offset
        self.GRID_SIZE = self.grid_size

        # colors for the players
        self.CIRCLE_COLOR = (255, 255, 255) 
        self.CROSS_COLOR = (255, 255, 255)   

        # Sets width and height for grid location
        self.WIDTH = self.size[0] / self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1] / self.GRID_SIZE - self.OFFSET

        # sets margin
        self.MARGIN = 5

        # array to hold board state
        self.board_state = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe")

    #testing border caption
    def change_turn(self):
        if self.game_state.player_turn == 1:
            pygame.display.set_caption("Tic Tac Toe - It is your turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - AI's turn")

    # drawing the circle function
    def draw_circle(self, x, y):
        # Calculate the center of the cell
        pos_x = y * (self.WIDTH + self.MARGIN) + self.WIDTH / 2 + self.MARGIN
        pos_y = x * (self.HEIGHT + self.MARGIN) + self.HEIGHT / 2 + self.MARGIN
        radius = min(self.WIDTH, self.HEIGHT) / 2 - self.MARGIN
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (int(pos_x), int(pos_y)), int(radius), 2)

    # Drawing the cross function
    def draw_cross(self, x, y):
        # calculate the corners of cell
        start_x = y * (self.WIDTH + self.MARGIN) + self.MARGIN
        start_y = x * (self.HEIGHT + self.MARGIN) + self.MARGIN
        end_x = start_x + self.WIDTH
        end_y = start_y + self.HEIGHT
        # Draw two diagonal lines
        pygame.draw.line(self.screen, self.CROSS_COLOR, (start_x, start_y), (end_x, end_y), 2)
        pygame.draw.line(self.screen, self.CROSS_COLOR, (start_x, end_y), (end_x, start_y), 2)

    def is_game_over(self):
        return self.game_state.is_terminal()

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)
        self.board_state = self.game_state.board_state  # Update board_state

    def play_ai(self):
        # AI's turn
        ai_symbol = self.game_state.player_turn  # Should be -1
        if self.algorithm == "minimax":
            value, move = minimax(self.game_state, self.depth, maximizingPlayer=False)
        else:  # Negamax
            value, move = negamax(self.game_state, self.depth, ai_symbol)
        if move is not None:
            self.move(move)
            x, y = move[0], move[1]
            if ai_symbol == 1:
                self.draw_cross(x, y)
                sounds.play_x_sound()  # Play X sound if AI uses X
            else:
                self.draw_circle(x, y)
                sounds.play_circle_sound()  # Play circle sound
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        if terminal:
            score = self.game_state.get_scores(True)
            self.display_winner(score)

    def game_reset(self):
        self.draw_game()
        # Reset the game state
        self.board_state = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)
        self.game_state = GameStatus(self.board_state, player_turn=1)  # Human player starts
        self.change_turn()
        pygame.display.update()

    def display_winner(self, score):
        # stop music here
        sounds.stop_background_music()

        font = pygame.font.Font(None, 72)
        if score > 0:
            sounds.play_win_sound()
            text = font.render("You Win!", True, self.BLACK)
        elif score < 0:
            sounds.play_lose_sound()
            text = font.render("AI Wins!", True, self.BLACK)
        else:
            sounds.play_draw_sound()
            text = font.render("Draw!", True, self.WHITE)
        text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        self.show_settings_menu()  # return back to game settings

    def update_background_color(self):
        # update hue
        self.hue = (self.hue + self.color_speed) % 360
        # convert hsv to rgb
        rgb = colorsys.hsv_to_rgb(self.hue / 360.0, 1, 1)
        # Convert scale to 0-255
        color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
        # Fill the screen with the new color
        self.screen.fill(color)
        # Redraw grid lines
        for row in range(self.GRID_SIZE):
            for column in range(self.GRID_SIZE):
                pygame.draw.rect(self.screen,
                                 self.WHITE,
                                 [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                  (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                  self.WIDTH,
                                  self.HEIGHT],
                                 1)  # Draw as lines

    def show_settings_menu(self):


        # Define settings menu screen
        settings_screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Settings")

        font = pygame.font.Font(None, 36)
        clock = pygame.time.Clock()

        # Sliders position
        grid_size_slider_rect = pygame.Rect(200, 100, 300, 10)
        depth_slider_rect = pygame.Rect(200, 170, 300, 10)

        # Handles
        grid_size_handle_rect = pygame.Rect(0, 95, 20, 20)
        depth_handle_rect = pygame.Rect(0, 165, 20, 20)

        # Initialize values for slide
        grid_size_value = self.grid_size
        depth_value = self.depth

        # Handle positions based on values
        grid_size_handle_rect.x = 200 + ((grid_size_value - 3) / 7) * 300 - 10
        depth_handle_rect.x = 200 + ((depth_value - 3) / 7) * 300 - 10

        # GUI for algorithm
        algorithm_dropdown_rect = pygame.Rect(200, 240, 200, 40)
        algorithm_options = ["minimax", "negamax"]
        algorithm_active = False
        selected_algorithm = self.algorithm

        grid_size_dragging = False
        depth_dragging = False

        run_settings = True
        while run_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Checking for mousebuttondown (click)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    # check grid handle
                    if grid_size_handle_rect.collidepoint(mouse_pos):
                        grid_size_dragging = True

                    # Check depth handle
                    if depth_handle_rect.collidepoint(mouse_pos):
                        depth_dragging = True

                    # Check if algorithm 
                    if algorithm_dropdown_rect.collidepoint(mouse_pos):
                        algorithm_active = not algorithm_active
                    else:
                        # Check if any option is selected
                        if algorithm_active:
                            for i, option in enumerate(algorithm_options):
                                option_rect = pygame.Rect(200, 240 + (i + 1) * 40, 200, 40)
                                if option_rect.collidepoint(mouse_pos):
                                    selected_algorithm = option
                                    algorithm_active = False
                                    break
                            else:
                                algorithm_active = False



                    # Start button
                    start_button = pygame.Rect(250, 350, 100, 50) 
                    if start_button.collidepoint(mouse_pos):
                        self.grid_size = int(grid_size_value)
                        self.depth = int(depth_value)
                        self.algorithm = selected_algorithm

                        # Recalculation based on grid size here
                        self.WIDTH = self.size[0] / self.grid_size - self.OFFSET
                        self.HEIGHT = self.size[1] / self.grid_size - self.OFFSET
                        self.hue = 0  # Reset rgb
                        self.game_reset()
                        sounds.play_background_music()  # I AM THE CANDYMAN
                        run_settings = False

                elif event.type == pygame.MOUSEBUTTONUP:
                    grid_size_dragging = False
                    depth_dragging = False

                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    if grid_size_dragging:
                    
                        grid_size_handle_rect.x = max(200 - 10, min(mouse_pos[0] - 10, 500 - 10))
                    

                        relative_x = grid_size_handle_rect.x + 10 - 200
                        grid_size_value = round(3 + (relative_x / 300) * 7)


                    if depth_dragging:
                        depth_handle_rect.x = max(200 - 10, min(mouse_pos[0] - 10, 500 - 10))
                        relative_x = depth_handle_rect.x + 10 - 200
                        depth_value = round(3 + (relative_x / 300) * 7)

            settings_screen.fill((30, 30, 30))

            # render text for grid size
            grid_size_txt = font.render(f'Grid Size: {grid_size_value}', True, self.WHITE)
            settings_screen.blit(grid_size_txt, (50, 90))
            # Draw slider for grid size
            pygame.draw.rect(settings_screen, self.GRAY, grid_size_slider_rect)
            pygame.draw.rect(settings_screen, self.BLUE, grid_size_handle_rect)

            # Render text for depth
            depth_txt = font.render(f'Depth: {depth_value}', True, self.WHITE)
            settings_screen.blit(depth_txt, (50, 160))

            # Depth Slider
            pygame.draw.rect(settings_screen, self.GRAY, depth_slider_rect)
            pygame.draw.rect(settings_screen, self.BLUE, depth_handle_rect)

            # Algorithm selection text
            algorithm_txt = font.render('Algorithm:', True, self.WHITE)
            settings_screen.blit(algorithm_txt, (50, 250))
            # Drop down menu
            pygame.draw.rect(settings_screen, self.GRAY, algorithm_dropdown_rect)
            selected_alg_txt = font.render(selected_algorithm.capitalize(), True, self.WHITE)
            settings_screen.blit(selected_alg_txt, (algorithm_dropdown_rect.x + 5, algorithm_dropdown_rect.y + 5))
            pygame.draw.polygon(settings_screen, self.WHITE, [
                (algorithm_dropdown_rect.right - 20, algorithm_dropdown_rect.y + 15),
                (algorithm_dropdown_rect.right - 10, algorithm_dropdown_rect.y + 15),
                (algorithm_dropdown_rect.right - 15, algorithm_dropdown_rect.y + 25)
            ])

            # Draw the drop down
            if algorithm_active:
                for i, option in enumerate(algorithm_options):
                    option_rect = pygame.Rect(200, 240 + (i + 1) * 40, 200, 40)
                    pygame.draw.rect(settings_screen, self.DARK_GRAY, option_rect)
                    option_txt = font.render(option.capitalize(), True, self.WHITE)
                    settings_screen.blit(option_txt, (option_rect.x + 5, option_rect.y + 5))

            # Render start button
            start_button = pygame.Rect(250, 350, 100, 50)  # Moved down
            pygame.draw.rect(settings_screen, self.GREEN, start_button)
            start_txt = font.render('Start', True, self.BLACK)
            settings_screen.blit(start_txt, (start_button.x + 20, start_button.y + 10))

            pygame.display.flip()
            clock.tick(60)

    def play_game(self, mode="player_vs_ai"):
        self.show_settings_menu()  # display settings menu before booting game

        done = False
        clock = pygame.time.Clock()

        while not done:
            self.update_background_color()  # Update background color
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = int(pos[0] // (self.WIDTH + self.MARGIN))
                    row = int(pos[1] // (self.HEIGHT + self.MARGIN))
                    if row < self.grid_size and column < self.grid_size:
                        if self.board_state[row, column] == 0:
                            self.board_state[row, column] = 1  # Human player
                            self.draw_cross(row, column)
                            sounds.play_x_sound()  # Play X sound
                            self.game_state = GameStatus(self.board_state, player_turn=-1)  # AI turn
                            pygame.display.update()
                            if self.is_game_over():
                                self.display_winner(self.game_state.get_scores(True))
                                continue
                            self.play_ai()
                            if self.is_game_over():
                                self.display_winner(self.game_state.get_scores(True))
            # redraw existing x's / o's
            for row in range(self.GRID_SIZE):
                for col in range(self.GRID_SIZE):
                    if self.board_state[row, col] == 1:
                        self.draw_cross(row, col)
                    elif self.board_state[row, col] == -1:
                        self.draw_circle(row, col)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        sounds.stop_background_music() 

if __name__ == "__main__":
    tictactoegame = RandomBoardTicTacToe()
    tictactoegame.play_game()