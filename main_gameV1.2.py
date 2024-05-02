import numpy as np
import pygame
import time
from Button import Button
# Σταθερές
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2.5)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
BLUE = (0, 0, 255)
LIGHT_BLUE=(0, 0, 128)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Αρχικοποίηση του Pygame
pygame.init()

# Δημιουργία οθόνης
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4 Game")


font_path="game_font.ttf"
font = pygame.font.Font(font_path, 100)

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
    # Έλεγχος για νίκη στις γραμμές
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Έλεγχος για νίκη στις στήλες
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Έλεγχος για νίκη στις διαγωνίους (/)
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Έλεγχος για νίκη στις διαγωνίους (\)
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
            # Σχεδίαση των τετραγώνων του πίνακα
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # Σχεδίαση των κύκλων για τα κομμάτια στο εσωτερικό των τετραγώνων
            pygame.draw.circle(screen, (0, 0, 0), (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE / 2) + SQUARESIZE), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # Σχεδίαση των κόκκινων και κίτρινων κύκλων για τα κομμάτια των παικτών
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)



def wait_for_click():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def show_winner(winner):
    # Εμφάνιση του νικητή
    font_path="game_font.ttf"
    font = pygame.font.Font(font_path, 100)
    text_surface = font.render(f"Player {winner} wins!", True, BLUE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT / 15))
      
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    wait_for_click()



# Κύριος κώδικας του παιχνιδιού
def play_game():
    
    board = create_board()

    #δείχνει αν τρέχει το παιχνίδι
    game_over = False
    turn = 0
    draw_board(board)
    pygame.display.update()
    
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, RED if turn == 0 else YELLOW, (int(posx), int(SQUARESIZE / 2)), RADIUS)
                col = int(posx // SQUARESIZE)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                col = int(posx // SQUARESIZE)

                if is_valid_location(board, col) :
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1 if turn == 0 else 2)
                    

                    if winning_move(board, 1 if turn == 0 else 2):
                        winner = 1 if turn == 0 else 2
                        print(f"Player {winner} wins!")
                        draw_board(board)#Εμφανίζει και το 4ο πιόνι
                        show_winner(winner)#εμφανίζει το νικητή
                        
                        
                        #Αφού βρεθεί νικητής εμφανίζεται το menu για να ξανα παίξει ο παίχτης
                        starting_menu()
                    #βάζοντας μέσα στην if is_valid_location την αλλαγή του παίκτη 
                    #εξασφαλίζουμε ότι δεν αλλάζει η σειρά του παίκτη εάν
                    #δεν τοποθετήσει πιόνι σε σωστή θέση
                    turn += 1
                    turn %= 2
                

                draw_board(board)#σχεδιάζει το πίνακα με τα πιόνια
                
                pygame.display.update()

                

            #Πατώντας το esc εμφανίζεται το κύριο menu 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                result=display_menu()
                #Αν πατηθεί το continue επιστρέφει 1
                #Αν το result εχει τιμή 1 τότε εμφανίζεται ο πίνακας όπως τον είχαμε αφήσει
                if result==1:
                    draw_board(board)
                    print(result)   #Εμφανίζει στην κονσόλα την τιμή του result για debugging
                    pygame.display.update() #Ανανεώνει την εικόνα στην οθόνη  

            
        
        
        #Αν λήξει ισοπαλία δίνεται στο παίκτη η δυνατότητα να ξεκινήσει νέο παιχνίδι ή να κάνει exit
        if is_board_full(board) and not winning_move(board, 1) and not winning_move(board, 2):
            wait_for_click()
            starting_menu()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()

                        if WIDTH // 4 + 5 < pos[0] < WIDTH // 4 + WIDTH // 2 - 10 + 5:
                            if HEIGHT // 3 + 5 < pos[1] < HEIGHT // 3 + 40 + 5:
                                return
                            elif HEIGHT // 3 + 90 < pos[1] < HEIGHT // 3 + 125:
                                score = [0, 0]
                            elif HEIGHT // 3 + 140 < pos[1] < HEIGHT // 3 + 175:
                                return "quit"

                        board = create_board()
                        draw_board(board)
                        
                        pygame.display.update()


def display_menu():
    # Δημιουργία της οθόνης μενού
    menu_running = True     #το μενού είναι ανοικτό

    #Δημιουργεί τα παρακάτω κουμπιά
    continue_button = Button(screen, WIDTH // 4, HEIGHT // 5, WIDTH // 2, HEIGHT // 6, "Continue")
    new_game_button = Button(screen, WIDTH // 4, HEIGHT // 5 * 2, WIDTH // 2, HEIGHT // 6, "New Game")
    exit_button = Button(screen, WIDTH // 4, HEIGHT // 5 * 3, WIDTH // 2, HEIGHT // 6, "Exit")

    #όσο το μενού είναι ανοικτό 
    while menu_running:
        #σχεδιάζει τα κουμπιά
        screen.fill((0, 0, 128))
        continue_button.draw()
        new_game_button.draw()
        exit_button.draw()

        pygame.display.update()
        for event in pygame.event.get():
            #τερματίζει το πρόγραμμα
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #Αν πατηθεί το continue κλείνει το παράθυρο του menu και συνεχίζει το παιχνίδι 
                #Αν πατηθεί το continue επιστρέφει 1
                if continue_button.is_clicked(mouse_pos):
                    menu_running = False
                    return 1
                    
                    
                #Αν πατηθεί το new_game κλείνει το παράθυρο του menu και αρχίζει νέο παιχνίδι
                elif new_game_button.is_clicked(mouse_pos):
                    play_game()
                    menu_running = False
                

                elif exit_button.is_clicked(mouse_pos):
                    pygame.quit()
                    exit()

#Εμφανίζει το αρχικό menu
def starting_menu():
# Κύριος κώδικας του παιχνιδιού
    start_button = Button(screen, WIDTH // 4, HEIGHT // 5, WIDTH // 2, HEIGHT // 6, "Start Game")
    exit_button = Button(screen, WIDTH // 4, HEIGHT // 5* 2, WIDTH // 2, HEIGHT // 6, "Exit")

    while True:
        for event in pygame.event.get():
            #Αν πατήσεις X κλείνει το πρόγραμμα
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Έλεγχος αν κάποιο από τα κουμπιά του μενού πατήθηκε
                #Ξεκινά το παιχνίδι
                if start_button.is_clicked(mouse_pos):
                    play_game()

                #Τερματίζει το παιχνίδι
                elif exit_button.is_clicked(mouse_pos):
                    pygame.quit()
                    exit()

        screen.fill(LIGHT_BLUE)
        start_button.draw()
        exit_button.draw()
        
        
        pygame.display.update()

def main():
    # Κύριος κώδικας του παιχνιδιού
    starting_menu()


if __name__ == '__main__':
    pygame.display.update()
    main()