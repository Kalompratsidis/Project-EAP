#Κλάση για δημιουργία κουμιού που επιστρέφει True ή False αν το κουμπί έχει πατηθεί ή όχι αντίστοιχα. 

import pygame

class Button:
    RED=(255,0,0)
    YELLOW=(255,255,0)
    def __init__(self, window, x, y, width, height, text):
        self.window = window    #δηλωνει σε ποια επιφάνεια θα εκτελεστεί(τυπωθεί)
        self.x = x              #η θέση στο άξονα x
        self.y = y              #η θέση στο άξονα y
        self.width = width      #το πλάτος
        self.height = height       #το ύψος
        self.text = text           #κείμενο
        self.text_color = self.RED  #το κείμενο θα έχει χρώμα κόκκινο
        self.button_color =self.YELLOW  #το κουμπί θα έχει χρώμα κίτρινο
        self.center=self.x + self.width // 2, self.y + self.height // 2
        
    
    def draw(self):
        #σχεδιάζει το κουμπί με ορθογώνιο σχήμα και ορισμένο χρώμα ξεκινόντας από τις συντεταγμένες x,y με το αντίστοιχο ύψος και πλάτος
        pygame.draw.rect(self.window, self.button_color, (self.x, self.y, self.width, self.height)) #pygame.draw.rect(surface,color,rect,width) σύμφωνα με τα docs

    # Προσθήκη του κειμένου μέσα στο κουμπί
        #ορίζουμε γραμματοσειρά σε None και μέγεθος του κειμένου σε 36 χωρίς ακόμη να τα εφαρμόζουμε στο κείμενο
        font = pygame.font.Font(None, 36)   #pygame.font.Font(file_path=None, size=12) σύμφωνα με τα docs

        #δημιουργήσει επιφάνεια που που περιέχει το κείμενο που θα εμφανιστεί στο κουμπί
        text_surface = font.render(self.text, True, self.text_color)    #render(text, antialias, color, background=None) σύμφωνα με τα docs το antialias πρέπει παντα να είναι true

        #δημιουργούμε το ορθογώνιο background του κομπιού και 
        text_rect = text_surface.get_rect(self.center)

        #εμφανίζει το κουμπί στην οθόνη
        self.surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        # Ελέγχουμε εάν το σημείο του ποντικιού είναι εντός του πλαισίου του κουμπιού και επιστρέφει True ή False αντίστοιχα
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(mouse_pos) 
    
    

