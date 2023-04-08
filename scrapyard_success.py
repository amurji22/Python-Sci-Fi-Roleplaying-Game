import pygame

pygame.init()

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()
pygame.display.set_caption("Build Ship")

# load the background and create its rect
bg_img = pygame.image.load('images/scrapyard_success_background.png')
bg_rect = bg_img.get_rect()

# load spaceship img and create rect
sp_img = pygame.image.load('images/spaceship.png')
sp_rect = sp_img.get_rect()
sp_rect.center = (1200/2, 768/2)

# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(sp_img, sp_rect)
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
                exec(open('escape_cops_startscreen.py').read())

    render()

pygame.quit()