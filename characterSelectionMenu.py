import pygame
import time

class Button:
    def __init__(self, image, pos, height, radius, elevation):
        
        #attributes
        self.command = False
        self.pressed = False
        self.radius = radius
        self.elevation = elevation
        self.dynamic_elevation = elevation
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
                self.dynamic_elevation = 4
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

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

# create the background and its rect object
bg_img = pygame.image.load("character_background.jpg")
bg_rect = bg_img.get_rect()

main_menu_button_img = pygame.image.load('Exit.png')
main_menu_button_rect = main_menu_button_img.get_rect()

# create the character images and their rect objects
character_one_img = pygame.image.load("Character_One.png")
character_two_img = pygame.image.load("Character_Two.png")
character_three_img = pygame.image.load("Character_Three.png")
character_one_rect = character_one_img.get_rect()
character_two_rect = character_two_img.get_rect()
character_three_rect = character_three_img.get_rect()


# create the text image and its rect
text_img = pygame.image.load("choose.png")
text_rect = text_img.get_rect()

# create larger images of the characters for hover animation
character_one_img_big = pygame.transform.scale(character_one_img, (character_one_rect.width * 1.15, character_one_rect.height * 1.15))
character_two_img_big = pygame.transform.scale(character_two_img, (character_two_rect.width * 1.15, character_two_rect.height * 1.15))
character_three_img_big = pygame.transform.scale(character_three_img, (character_three_rect.width * 1.15, character_three_rect.height * 1.15))


# render function
def render():

    screen.blit(bg_img, bg_rect)
    screen.blit(character_one_img, (220, 250))
    screen.blit(character_two_img, (520, 250))
    screen.blit(character_three_img, (820, 250))
    screen.blit(text_img, (320, 0))
    screen.blit(main_menu_button_img,(875,555))
    character_one_rect.update((100, 100), (250, 400))
    character_two_rect.update((466, 100), (250, 400))
    character_three_rect.update((825, 100), (250,400))

    pygame.display.flip()

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

        # detect mouse collisions with the character sprite
        # set character_selected to the character the user clicks on
        if event.type == pygame.MOUSEBUTTONDOWN:
            main_menu_button_rect = main_menu_button_img.get_rect().move(875,555)
            if character_one_rect.collidepoint(pygame.mouse.get_pos()):
                character_selected = 1
                pygame.quit()
            elif character_two_rect.collidepoint(pygame.mouse.get_pos()):
                character_selected = 2
                pygame.quit()
            elif character_three_rect.collidepoint(pygame.mouse.get_pos()):
                character_selected = 3
                pygame.quit()
            elif main_menu_button_rect.collidepoint(event.pos):
                exec(open('main.py').read())
    # animations for characters if the mouse hovers over the images
    if character_one_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(character_one_img_big, (190, 75))
        pygame.display.flip()
        time.sleep(0.7)
    elif character_two_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(character_two_img_big, (490, 75))
        pygame.display.flip()
        time.sleep(0.7)
    elif character_three_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(character_three_img_big, (790, 75))
        pygame.display.flip()
        time.sleep(0.7)
    
    render()
    time.sleep(0.05)

pygame.quit()
