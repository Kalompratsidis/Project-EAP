# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:03:19 2024

@author: i.daraki
"""

import numpy as np
# Σταθερές για τις διαστάσεις του πίνακα
ROW_COUNT  = 6
COLUMN_COUNT = 7

def create_board():
    # Δημιουργία ενός πίνακα 6x7 γεμάτου με μηδενικά
    board= np.zeros ((ROW_COUNT,COLUMN_COUNT))
    return board
    board=np.zeros ((6,7))
    return boar
    
def drop_piece (board, row, col, piece):
    # Τοποθέτηση ενός κομματιού στην συγκεκριμένη θέση του πίνακα
   board [row] [col] = piece

def is_valid_location(board,col):
    # Έλεγχος αν η κορυφή της στήλης είναι κενή (δηλαδή αν υπάρχει χώρος για νέο κομμάτι)
    return board[5][col]==0
    pass

def get_next_open_row(board,col):
    # Επιστρέφει την πρώτη κενή γραμμή από το κάτω μέρος της συγκεκριμένης στήλης
    for r in range (ROW_COUNT):
        if board [r][col]== 0:
            return r
def print_board(board):
    # Εκτυπώνει τον πίνακα αναποδογυρισμένο (τα κομμάτια πέφτουν στο κάτω μέρος)
    print(np.flip(board,0))
     
def winning_move(board,piece):
    # Έλεγχος για νικητήρια κίνηση οριζόντια
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2]== piece and board[r][c+3] == piece:
                return True
            
     # Έλεγχος για νικητήρια κίνηση κατακόρυφα
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c]== piece and board[r+3][c] == piece:
                return True
            
    # Έλεγχος για νικητήρια κίνηση διαγώνια με θετική κλίση
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2]== piece and board[r+3][c+3] == piece:
                return True
                
    # Έλεγχος για νικητήρια κίνηση διαγώνια με αρνητική κλίση
                for c in range (COLUMN_COUNT-3):
                    for r in range(3,ROW_COUNT):
                        if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2]== piece and board[r-3][c+3] == piece:
                            return True
                
   # Πίνακας για την καταγραφή των σκορ των παικτών                 
player_scores = {1: 0, 2: 0}
round_count = 0

# Βασικός βρόχος παιχνιδιού
while round_count < 3:
    board = create_board()
    game_over = False
    turn = 0
    
    while not game_over:
        player = turn % 2 + 1
        valid_choice = False
        
        while not valid_choice:
            col = int(input(f"Παίχτης {player}, κάντε την επιλογή σας (0-6):"))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, player)
                valid_choice = True
                
                if winning_move(board, player):
                    print(f"Παίχτης {player} κερδίζει!!! Συγχαρητήρια!!!")
                    player_scores[player] += 1
                    game_over = True
            else:
                print("Η στήλη είναι γεμάτη, παρακάλω επιλέξτε άλλη.")
        
        print_board(board)
        turn += 1
    
    round_count += 1
    if round_count < 3:
        print(f"Σκορ: Παίχτης 1: {player_scores[1]}, Παίχτης 2: {player_scores[2]}")
        print("Ξεκινάει νέος γύρος...")
    else:
        print("Ολοκληρώθηκαν 3 γύροι παιχνιδιού.")

# Εκτύπωση του τελικού σκορ και ανακήρυξη του νικητή
winner = max(player_scores, key=player_scores.get)
print(f"Τελικό Σκορ: Παίχτης 1: {player_scores[1]}, Παίχτης 2: {player_scores[2]}")
print(f"Ο νικητής είναι ο Παίχτης {winner}!")