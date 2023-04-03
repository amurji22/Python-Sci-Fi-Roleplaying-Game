import pygame

class Button:
    def __init__(self, image, pos, height, radius, elevation, lowest_elevation, screen):
        
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

        # for hover animation
        self.bigTopImage = pygame.transform.scale(self.image, (self.top_rect.width * 1.1, self.top_rect.height * 1.1))
        self.bigTopImage_rect = self.bigTopImage.get_rect()
        self.bigTopImage_rect.center = (pos)

        self.bigBottom_rect = pygame.Rect(pos,(self.bigTopImage_rect.width,height))
        self.bigBottom_rect.center = (pos)

    def draw_noHover(self):

        self.top_rect.centery = self.original_y_pos - self.dynamic_elevation
        pygame.draw.rect(self.screen,self.bottom_colour, self.bottom_rect, border_radius=self.radius)
        self.screen.blit(self.image,self.top_rect)
        self.check_click()
    
    def draw_hover(self):
        self.dynamic_elevation = self.dynamic_elevation *1.5
        self.bigTopImage_rect.centery = self.original_y_pos - self.dynamic_elevation
        pygame.draw.rect(self.screen,self.bottom_colour, self.bigBottom_rect, border_radius=self.radius)
        self.screen.blit(self.bigTopImage,self.bigTopImage_rect)
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
            
    def check_hover(self):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            self.draw_hover()
        else:
            self.draw_noHover()

class characterButton:
    def __init__(self, topImage, bottomImage, pos, elevation, lowest_elevation, screen):
        
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
        
        # for hover animation
        self.bigTopImage = pygame.transform.scale(self.topImage, (self.top_rect.width * 1.1, self.top_rect.height * 1.1))
        self.bigTopImage_rect = self.bigTopImage.get_rect()
        self.bigTopImage_rect.center = (pos)

        self.bigBottomImage = pygame.transform.scale(self.bottomImage, (self.bottom_rect.width * 1.1, self.bottom_rect.height * 1.1))
        self.bigBottomImage_rect = self.bigBottomImage.get_rect()
        self.bigBottomImage_rect.center = (pos)
          
    def draw_noHover(self):
        self.top_rect.centery = self.original_y_pos - self.dynamic_elevation
        self.screen.blit(self.bottomImage,self.bottom_rect)
        self.screen.blit(self.topImage,self.top_rect)
        self.check_click()
    
    def draw_hover(self):
        self
        self.bigTopImage_rect.centery = self.original_y_pos - self.dynamic_elevation
        self.screen.blit(self.bigBottomImage, self.bigBottomImage_rect)
        self.screen.blit(self.bigTopImage, self.bigTopImage_rect)
        self.check_click()
        
    def check_hover(self):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            self.draw_hover()
        else:
            self.draw_noHover()

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

class Character:
    def __init__(self, image_path, x, y, scale=1, speed=1):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.x = x/2 - self.rect.width/2
        self.rect.y = y - self.rect.height
        self.speed = speed
        self.screen_width = x
        self.screen_height = y
        self.rect_posx = self.rect.x

minigame_2_complete = False

minigame_1_complete = False

minigame_3_complete = False
        
        



            
