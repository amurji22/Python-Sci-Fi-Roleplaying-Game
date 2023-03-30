import pygame, time
import gameElements
        
pygame.init()

bg_img = pygame.image.load('images/background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()
pygame.display.set_caption("Minigame 3 and Scrapyard Choice")

startButton = gameElements.Button('images/Start.png',(600, 384),130,75,20,4, screen)
exitButton = gameElements.Button('images/Exit.png',(1000,700),90,50,12,2, screen)
screen.blit(bg_img, bg_rect)

running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if startButton.command == True:
        exec(open('minigame3_scrapyard.py').read())
        startButton.command = False
    elif exitButton.command == True:
        exec(open('explore_town.py').read())
        exitButton.command = False

    screen.blit(bg_img, bg_rect)
    startButton.check_hover()
    exitButton.check_hover()
    pygame.display.flip()
    time.sleep(0.05)
pygame.quit()