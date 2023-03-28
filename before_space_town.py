import pygame
from characterSelectionMenu import character_selected

pygame.init()

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 740))
screen_rect = screen.get_rect()

# load the background and create its rect
bg_img = pygame.image.load("images/before_space_town_background.jpg")
bg_rect = bg_img.get_rect()


# render function
def render():
    screen.blit(bg_img, bg_rect)

    pygame.display.flip()


# game loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # if the space bar is pressed, move to next scene
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # fill this with the py file name for the space town when it is completed
                exec(open('explore_town.py').read())


    render()

pygame.quit()
