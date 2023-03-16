import pygame
import time

class Button:
    def __init__(self, image, pos, height, radius, elevation,lowest_elevation):
        
        #attributes
        self.command = False
        self.pressed = False
        self.radius = radius
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.lowest_elevation = lowest_elevation
        self.original_y_pos = pos[1]

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
        pygame.draw.rect(screen,self.bottom_colour, self.bottom_rect, border_radius=self.radius)
        screen.blit(self.image,self.top_rect)
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
    def __init__(self, topImage, bottomImage, pos, elevation,lowest_elevation):
        
        #attributes
        self.command = False
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.lowest_elevation = lowest_elevation
        self.original_y_pos = pos[1]

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
        screen.blit(self.bottomImage,self.bottom_rect)
        screen.blit(self.topImage,self.top_rect)
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

pygame.init()

mainMenuButton = Button('Exit.png',(1000,700),90,50,12,2)
characterOne = characterButton('Character_One.png','Character_One_Underlay.png',(300,430),12,2)
characterTwo = characterButton('Character_Two.png','Character_Two_Underlay.png',(600,430),12,2)
characterThree = characterButton('Character_Three.png','Character_Three_Underlay.png',(900,430),12,2)

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

# create the background and its rect object
bg_img = pygame.image.load("character_background.jpg")
bg_rect = bg_img.get_rect()


# create the text image and its rect
text_img = pygame.image.load("choose.png")
text_rect = text_img.get_rect()



# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(text_img, (320, 0))


render()

# variable to store the character selected
character_selected = 0

# game loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if mainMenuButton.command == True:
        exec(open('main.py').read())
        mainMenuButton.command = False
    elif characterOne.command == True:
        character_selected = 1
        print(character_selected)
        characterOne.command = False
        # pygame.quit()
    elif characterTwo.command == True:
        character_selected = 2
        print(character_selected)
        characterTwo.command = False
        # pygame.quit()
    elif characterThree.command == True:
        character_selected = 3
        print(character_selected)
        characterThree.command = False
        # pygame.quit()

 
    render()
    characterOne.draw()
    characterTwo.draw()
    characterThree.draw()
    mainMenuButton.draw()
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
