#έβαλα 2-3 πραγματα οπως 
#να δείχνει score
#και θα επρεπε να υπάρχει το κουμπί 
#που έχω καποια θέματα να το ενσωματώσω
#θέλει και άλλη δουλεια.
import numpy as np
import pygame
import time

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2.5)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
SCORE_WIDTH = SQUARESIZE * 2
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4 Game")

class Button:
    RED=(255,0,0)
    YELLOW=(255,255,0)
    
    def __init__(self, window, x, y, width, height, text):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = self.RED
        self.button_color = self.YELLOW
        self.center = self.x + self.width // 2, self.y + self.height // 2

    def draw(self):
        pygame.draw.rect(self.window, self.button_color, (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.center)
        self.window.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mouse_pos)

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

    return False

def is_board_full(board):
    return np.all(board != 0)

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, (0, 0, 0), (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE / 2) + SQUARESIZE), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

def draw_score(score):
    font = pygame.font.SysFont("monospace", 40)
    label = font.render(f"Score - Player 1: {score[0]}, Player 2: {score[1]}", 1, (255, 255, 255))
    screen.blit(label, (WIDTH - SCORE_WIDTH + 10, 10))

def show_winner(winner):
    font = pygame.font.SysFont("monospace", 75)
    label = font.render(f"Player {winner} wins!", 1, (255, 255, 255))
    screen.blit(label, (40, HEIGHT // 2 - 50))
    pygame.display.update()
    time.sleep(2)

def show_restart_menu():
    pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 4, HEIGHT // 3, WIDTH // 2, HEIGHT // 3))
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 4 + 5, HEIGHT // 3 + 5, WIDTH // 2 - 10, HEIGHT // 3 - 10))
    
    font = pygame.font.Font(None, 36)
    text = font.render("Play Again", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 60, HEIGHT // 3 + 40))

    text = font.render("Reset Score", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 60, HEIGHT // 3 + 90))

    text = font.render("Quit to Main Menu", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 3 + 140))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Check if any of the buttons are clicked
                if WIDTH // 4 + 5 < pos[0] < WIDTH // 4 + WIDTH // 2 - 10 + 5:
                    if HEIGHT // 3 + 5 < pos[1] < HEIGHT // 3 + 40 + 5:
                        return "play_again"
                    elif HEIGHT // 3 + 90 < pos[1] < HEIGHT // 3 + 125:
                        return "reset_score"
                    elif HEIGHT // 3 + 140 < pos[1] < HEIGHT // 3 + 175:
                        return "quit"

def play_game():
    board = create_board()
    game_over = False
    turn = 0
    score = [0, 0]

    draw_board(board)
    draw_score(score)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, RED if turn == 0 else YELLOW, (int(posx), int(SQUARESIZE / 2)), RADIUS)
                col = int(posx // SQUARESIZE)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                col = int(posx // SQUARESIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1 if turn == 0 else 2)

                    if winning_move(board, 1 if turn == 0 else 2):
                        winner = 1 if turn == 0 else 2
                        print(f"Player {winner} wins!")
                        score[winner - 1] += 1
                        show_winner(winner)
                        time.sleep(2)

                        choice = show_restart_menu()
                        if choice == "play_again":
                            return
                        elif choice == "reset_score":
                            score = [0, 0]
                        elif choice == "quit":
                            return

                        board = create_board()
                        draw_board(board)
                        draw_score(score)
                        pygame.display.update()
                        continue

                draw_board(board)
                draw_score(score)
                pygame.display.update()

                turn += 1
                turn %= 2

        if is_board_full(board) and not winning_move(board, 1) and not winning_move(board, 2):
            pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 4, HEIGHT // 3, WIDTH // 2, HEIGHT // 3))
            pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 4 + 5, HEIGHT // 3 + 5, WIDTH // 2 - 10, HEIGHT // 3 - 10))
            
            font = pygame.font.Font(None, 36)
            text = font.render("Play Again", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - 60, HEIGHT // 3 + 40))

            text = font.render("Reset Score", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - 60, HEIGHT // 3 + 90))

            text = font.render("Quit to Main Menu", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 3 + 140))

            pygame.display.update()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()

                        # Check if any of the buttons are clicked
                        if WIDTH // 4 + 5 < pos[0] < WIDTH // 4 + WIDTH // 2 - 10 + 5:
                            if HEIGHT // 3 + 5 < pos[1] < HEIGHT // 3 + 40 + 5:
                                return
                            elif HEIGHT // 3 + 90 < pos[1] < HEIGHT // 3 + 125:
                                score = [0, 0]
                            elif HEIGHT // 3 + 140 < pos[1] < HEIGHT // 3 + 175:
                                return "quit"

                        board = create_board()
                        draw_board(board)
                        draw_score(score)
                        pygame.display.update()

def main():
    while True:
        play_game()

if __name__ == '__main__':
    main()