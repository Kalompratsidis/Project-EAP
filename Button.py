import pygame

class Button:
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    hover_col = (75, 225, 255)  # Χρώμα όταν το ποντίκι είναι πάνω από το κουμπί

    def __init__(self, window, x, y, width, height, text):
        self.window = window    
        self.x = x    # Θέση X του κουμπιού στο παράθυρο
        self.y = y    # Θέση Y του κουμπιού στο παράθυρο
        self.width = width    # Πλάτος του κουμπιού
        self.height = height    # Ύψος του κουμπιού
        self.text = text    # Κείμενο του κουμπιού
        self.text_color = self.RED    # Χρώμα του κειμένου 
        self.button_color = self.YELLOW    # Χρώμα background του κουμπιού
        self.center = (self.x + self.width // 2, self.y + self.height // 2)    # Κέντρο του κουμπιού
        self.clicked = False    

    def draw(self):
        pos = pygame.mouse.get_pos()    # Τρέχουσα θέση του ποντικιού
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)    # Δημιουργία παραλληλογράμμου για το κουμπί

        # Εάν το ποντίκι είναι πάνω από το κουμπί, αλλάξτε το χρώμα του κουμπιού
        if button_rect.collidepoint(pos):
            pygame.draw.rect(self.window, self.hover_col, button_rect)  # Σχεδίαση κουμπιού με το ποντίκι πάνω του
        else:
            pygame.draw.rect(self.window, self.button_color, button_rect)  # Σχεδίαση κουμπιού χωρίς το ποντίκι από πάνω

        # Εμφάνιση του κειμένου μέσα στο κουμπί
        font_path = "game_font.ttf"   
        font = pygame.font.Font(font_path, 36)     # Ορισμός γραμματοσειράς
        text_surface = font.render(self.text, True, self.text_color)    # Δημιουργία επιφάνειας κειμένου
        text_rect = text_surface.get_rect(center=self.center)    # Τοποθέτηση κειμένου στο κέντρο του κουμπιού
        self.window.blit(text_surface, text_rect)    # Εμφάνιση κουμπιου

    def is_clicked(self, mouse_pos):
        # αν το κουμπί πατήθηκε επιστρέφει True 
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mouse_pos)
