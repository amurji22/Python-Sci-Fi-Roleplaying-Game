import pygame

class Button():
    def __init__(self, x, y, image, scaleDefault, action=None):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scaleDefault), int(height * scaleDefault)))
        self.rect_img = self.image.get_rect()
        self.rect_img.center = (x, y)
        self.clicked = False
        self.mouse_over = False
        self.action = action

    def draw(self, surface):
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect_img.collidepoint(pos):
            self.mouse_over = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return self.action
            else:
                self.clicked = False

        surface.blit(self.image, self.rect_img)
  
class GameState():
    QUIT = -1
    TITLE = 0
