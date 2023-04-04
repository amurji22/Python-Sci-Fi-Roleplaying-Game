import pygame

pygame.init()

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()
pygame.display.set_caption("Escape Cops Startscreen")

# load the background and create its rect
bg_img = pygame.image.load('images/escape_start_background.png')
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
                exec(open('escape_cops_hard.py').read())

    render()

pygame.quit()