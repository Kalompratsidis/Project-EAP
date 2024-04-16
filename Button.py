# Κλάση για τα κουμπιά
import pygame

class Button:
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, window, x, y, width, height, text):
        self.window = window  # η επιφάνεια στην οποία θα εμφανιστεί το κουμπί
        self.x = x  # θέση στον άξονα x
        self.y = y  # θέση στον άξονα y
        self.width = width  # πλάτος
        self.height = height  # ύψος
        self.text = text  # κείμενο
        self.text_color = self.RED  # χρώμα κειμένου
        self.button_color = self.YELLOW  # χρώμα κουμπιού
        self.center = self.x + self.width // 2, self.y + self.height // 2

    def draw(self):
        # Σχεδίαση του κουμπιού
        pygame.draw.rect(self.window, self.button_color, (self.x, self.y, self.width, self.height))

        # Προσθήκη κειμένου μέσα στο κουμπί
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.center)
        self.window.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        # Έλεγχος αν το ποντίκι κάνει κλικ στο κουμπί
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mouse_pos)
