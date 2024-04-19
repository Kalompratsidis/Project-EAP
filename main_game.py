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
SCORE_WIDTH = SQUARESIZE * 2
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Αρχικοποίηση του Pygame
pygame.init()

# Δημιουργία οθόνης
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4 Game")




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
    #λύνει το πρόβλημα με το χρώμα στην πάνω γραμμη. Τώρα το χρώμα είναι από την αρχή μπλε και δδεν αλλάζει όταν κινούμε τον κέρσορα
    screen.fill((0, 0, 255))

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





def show_winner(winner):
    # Εμφάνιση του νικητή
    font = pygame.font.SysFont("monospace", 75)
    label = font.render(f"Player {winner} wins!", 1, (255, 255, 255))
    screen.blit(label, (40, HEIGHT // 2 - 50))
    pygame.display.update()
    time.sleep(2)


def play_game():
    # Κύριος κώδικας του παιχνιδιού
    board = create_board()

    #δείχνει αν τρέχει το παιχνίδι
    game_over = False
    turn = 0
    score = [0, 0]
    draw_board(board)
    
    pygame.display.update()
    game_paused = False
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

                        

                        board = create_board()
                        draw_board(board)
                        
                        pygame.display.update()
                        continue

                draw_board(board)
                
                pygame.display.update()

                turn += 1
                turn %= 2
            #Πατώντας το esc εμφανίζεται το κύριο menu 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                result=display_menu()
                #Αν πατηθεί το continue επιστρέφει 1
                #Αν το result εχει τιμή 1 τότε εμφανίζεται ο πίνακας όπως τον είχαμε αφήσει
                if result==1:
                    draw_board(board)
                    print(result)   #Εμφανίζει στην κονσόλα την τιμή του result για debugging
                    pygame.display.update() #Ανανεώνει την εικόνα στην οθόνη  

            
        
        
        
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
      
def main():
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
                
                

        screen.fill((0, 0, 128))
        start_button.draw()
        exit_button.draw()
        
        pygame.display.update()


if __name__ == '__main__':
    main()
