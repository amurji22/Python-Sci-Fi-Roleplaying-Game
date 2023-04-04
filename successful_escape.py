import pygame
# from escape_cops import alien_type

pygame.init()

# create screen
screen = pygame.display.set_mode((1200, 740))

# load the background and create its rect
bg_img = pygame.image.load("images/success_background.jpg")
bg_rect = bg_img.get_rect()

# render
def render():
    screen.blit(bg_img, bg_rect)
    pygame.display.flip()

running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    render()

pygame.quit()