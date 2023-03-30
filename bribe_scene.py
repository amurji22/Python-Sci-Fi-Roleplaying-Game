import pygame
import gameElements

# from escape_cops import alien_type

pygame.init()

# create screen
screen = pygame.display.set_mode((1200, 740))

# load the background and create its rect
bg_img = pygame.image.load("bribe_scene_background.png")
bg_rect = bg_img.get_rect()

exitButton = gameElements.Button('images/Exit.png',(173,75),90,50,12,2, screen)

og_copImage = pygame.image.load("space_cop.png")
og_copImage_rect = og_copImage.get_rect()
og_copImage_rect.center = (300,370)



# render
def render():
    screen.blit(bg_img, bg_rect)
    exitButton.check_hover()
    screen.blit(copImage, copImage_rect)
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