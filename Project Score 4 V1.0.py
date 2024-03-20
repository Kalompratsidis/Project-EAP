#Συνάρτηση για δημιοργία ταμπλό
def table_creation():

    #αμυντικός προγραμματισμός
    while True:
        try:
            N = int(input("Εισάγετε αριθμό Ν (από 10 έως 20) για τη δημιουργία του ταμπλό: "))
            if 3 <= N <= 3:
                collumn = [None] * N
                table=[collumn for i in range(N)]
                return table
            else:
                print("Ο αριθμός πρέπει να είναι από 10 έως 20. Παρακαλώ δοκιμάστε ξανά.")
        except ValueError:10
        print("Παρακαλώ εισάγετε έναν ακέραιο αριθμό.")

#Συνάρτηση για τοποθέτηση πιονιών στο πίνακα
#Δεν έχουν ληφθεί υπόψιν οι προυποθέσεις για την τοποθέτηση το πιονιών 
#Υπάρχει λάθος στην λογική τοποθέτησης των πιονιών
def player_pieces():
    print("Τα πιόνια του παίκτη 1 θα συμβολίζονται στο ταμπλό του παιχνιδιού με Ο κεφαλαίο και του παίκτη 2 με Χ κεφαλαίο")

    # Εισαγωγή θέσεων για τον παίκτη 1
    player_1_row = int(input("Εισαγωγή γραμμής πίνακα για τον παίκτη 1: "))
    player_1_column = int(input("Εισαγωγή στήλης  πίνακα για τον παίκτη 1: "))
    
    # Εισαγωγή θέσεων για τον παίκτη 2
    player_2_row = int(input("Εισαγωγή γραμμής πίνακα για τον παίκτη 2: "))
    player_2_column = int(input("Εισαγωγή στήλης πίνακα για τον παίκτη 2: "))
    
    # Τοποθέτηση των πιονιών στον πίνακα
    table[player_1_row][player_1_column] = 'Ο'
    table[player_2_row][player_2_column] = 'Χ'

    return table

#Συνάρτηση για ανάδειξη νικητή
def player_winning():
    pass





table=table_creation()
player_pieces()
print(table)
#print(table) εκτυπώνει αυτο το αποτέλεσμα 
#ουσιαστικά δημιουργεί το ταμπλό για να αποθηκεύουμε τις τιμές
#[[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None], 
#[None, None, None, None, None, None, None, None, None, None]]


