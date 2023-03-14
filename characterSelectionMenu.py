import pygame
import time

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
    screen.blit(character_one_img, (100, 100))
    screen.blit(character_two_img, (466, 100))
    screen.blit(character_three_img, (825, 100))
    screen.blit(text_img, (200, 400))
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
        screen.blit(character_one_img_big, (75, 75))
        pygame.display.flip()
        time.sleep(0.7)
    elif character_two_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(character_two_img_big, (441, 75))
        pygame.display.flip()
        time.sleep(0.7)
    elif character_three_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(character_three_img_big, (800, 75))
        pygame.display.flip()
        time.sleep(0.7)
    
    render()
    time.sleep(0.05)

pygame.quit()
