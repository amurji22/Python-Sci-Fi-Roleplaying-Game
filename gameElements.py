import pygame

class Button:
    def __init__(self, image, pos, height, radius, elevation,lowest_elevation, screen):
        
        #attributes
        self.command = False
        self.pressed = False
        self.radius = radius
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.lowest_elevation = lowest_elevation
        self.original_y_pos = pos[1]
        self.screen = screen

        # top rectangle
        self.image = pygame.image.load(image)
        self.top_rect = self.image.get_rect()
        self.top_rect.center = (pos)

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(self.top_rect.width,height))
        self.bottom_rect.center = (pos)
        self.bottom_colour = "#495d6e"

    def draw(self):
        self.top_rect.centery = self.original_y_pos - self.dynamic_elevation
        pygame.draw.rect(self.screen,self.bottom_colour, self.bottom_rect, border_radius=self.radius)
        self.screen.blit(self.image,self.top_rect)
        self.check_click()


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = self.lowest_elevation
                self.pressed  = True
            else: 
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print('click')
                    self.pressed = False
                    self.command = True
        else:
            self.dynamic_elevation = self.elevation

class characterButton:
    def __init__(self, topImage, bottomImage, pos, elevation,lowest_elevation, screen):
        
        #attributes
        self.command = False
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.lowest_elevation = lowest_elevation
        self.original_y_pos = pos[1]
        self.screen = screen

        # top rectangle
        self.topImage = pygame.image.load(topImage)
        self.top_rect = self.topImage.get_rect()
        self.top_rect.center = (pos)

        # bottom rectangle
        self.bottomImage = pygame.image.load(bottomImage)
        self.bottom_rect = self.bottomImage.get_rect()
        self.bottom_rect.center = (pos)


    def draw(self):
        self.top_rect.centery = self.original_y_pos - self.dynamic_elevation
        self.screen.blit(self.bottomImage,self.bottom_rect)
        self.screen.blit(self.topImage,self.top_rect)
        self.check_click()


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = self.lowest_elevation
                self.pressed  = True
            else: 
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print('click')
                    self.pressed = False
                    self.command = True
        else:
            self.dynamic_elevation = self.elevation
