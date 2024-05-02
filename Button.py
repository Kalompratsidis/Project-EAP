import pygame


class Button:
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    hover_col = (75, 225, 255)
    

    def __init__(self, window, x, y, width, height, text):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = self.RED
        self.button_color = self.YELLOW
        self.center = (self.x + self.width // 2, self.y + self.height // 2)
        self.clicked = False    #πάτημα κλικ

    def draw(self):

        pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Εάν το ποντίκι είναι πάνω από το κουμπί
        if button_rect.collidepoint(pos):
            pygame.draw.rect(self.window, self.hover_col, button_rect)  # Σχεδίαση κουμπιού με το ποντίκι πάνω του
        else:
            pygame.draw.rect(self.window, self.button_color, button_rect)  # Σχεδίαση κουμπιού χωρίς το ποντίκι από πάνω

        # Εμφάνιση του κειμένου μέσα στο κουμπί
        font_path = "game_font.ttf"
        font = pygame.font.Font(font_path, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.center)
        self.window.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mouse_pos)
