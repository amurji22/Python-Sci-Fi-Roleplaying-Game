import pygame
import gameElements
#from characterSelectionMenu import character_selected

# from escape_cops import alien_type

pygame.init()

#TEMPORARY CHARACTER ASSIGNMENT!!!!!
character_selected = 'images/Character_One.png'

# create screen
screen = pygame.display.set_mode((1200, 740))

# load the background and create its rect
bg_img = pygame.image.load("bribe_scene_background.png")
bg_rect = bg_img.get_rect()

#create exit button
exitButton = gameElements.Button('images/Exit.png',(173,75),90,50,12,2, screen)

#load the cop image and create its rect
og_copImage = pygame.image.load("space_cop.png")
og_copImage_rect = og_copImage.get_rect()

#load the character image and create its rect
og_character_img = pygame.image.load(character_selected)
og_character_rect = og_character_img.get_rect()

#create new resized images
resized_cop_img = pygame.transform.scale(og_copImage, (og_copImage_rect.width * 1.25, og_copImage_rect.height * 1.25))
character_img = pygame.transform.scale(og_character_img, (og_character_rect.width *0.8, og_character_rect.height * 0.8))

#flip cop image
cop_img = pygame.transform.flip(resized_cop_img, True, False)

# create new rect objects 
character_rect = character_img.get_rect()
cop_rect = cop_img.get_rect()

#position rect objects
cop_rect.center = (400,470)
character_rect.center = (800,470)


# render
def render():
    screen.blit(bg_img, bg_rect)
    exitButton.check_hover()
    screen.blit(cop_img, cop_rect)
    screen.blit(character_img, character_rect)
    pygame.display.flip()

running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if exitButton.command == True:
        exec(open('if_captured.py').read())


    render()

pygame.quit()