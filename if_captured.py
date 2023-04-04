import pygame, gameElements

pygame.init()

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

# load the background and create its rect
bg_img = pygame.image.load("images/if_captured_background.jpg")
bg_rect = bg_img.get_rect()

# create the button objects
bribeBtn = gameElements.Button('images/bribe_button.png',(225, 500), 125, 100, 20, 10, screen)
fightBtn = gameElements.Button('images/fight_button.png',(975, 500), 125, 100, 20, 10, screen)

# render function
def render():
    screen.blit(bg_img, bg_rect)
    bribeBtn.check_hover()
    fightBtn.check_hover()

    pygame.display.flip()

# game loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if bribeBtn.command == True:
        exec(open('bribe_scene.py').read())
        bribeBtn.command = False
    elif fightBtn.command == True:
        exec(open('fight_cops.py').read())
        fightBtn.command = False

    render()

pygame.quit()