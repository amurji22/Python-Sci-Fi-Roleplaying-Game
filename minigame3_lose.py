import pygame, time
import gameElements
        
pygame.init()

bg_img = pygame.image.load('images/minigame3_lose_background.png')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()
pygame.display.set_caption("You Lose!")

exitButton = gameElements.Button('images/Big_Exit.png',(600, 484),130,75,20,4, screen)
screen.blit(bg_img, bg_rect)

running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if exitButton.command == True:
        exec(open('explore_town.py').read())
        exitButton.command = False

    screen.blit(bg_img, bg_rect)
    exitButton.check_hover()
    pygame.display.flip()
    time.sleep(0.05)
pygame.quit()