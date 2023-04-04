import pygame, time
import gameElements

        
pygame.init()

bg_img = pygame.image.load('images/scrapyard_success_background.png')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()
pygame.display.set_caption("Upgrade Choice")

shieldButton = gameElements.Button('images/Start.png',(300, 484),130,75,20,4, screen)
speedButton = gameElements.Button('images/Big_Exit.png',(900,484),130,75,20,4, screen)
screen.blit(bg_img, bg_rect)

Black = (0,0,0)
White = (255,255,255)

running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if shieldButton.command == True:
        gameElements.shield_power = True
        exec(open('escape_cops_hard.py').read())
        shieldButton.command = False
    elif speedButton.command == True:
        gameElements.speed_power = True
        exec(open('escape_cops_hard.py').read())
        speedButton.command = False

    screen.blit(bg_img, bg_rect)
    shieldButton.check_hover()
    speedButton.check_hover()
    pygame.display.flip()
    time.sleep(0.05)
pygame.quit()