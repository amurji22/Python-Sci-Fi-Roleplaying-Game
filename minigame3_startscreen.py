import pygame, time
import gameElements
        
pygame.init()

bg_img = pygame.image.load('images/minigame3_start_background.png')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()
pygame.display.set_caption("Play Space Squishers")

startButton = gameElements.Button('images/Start.png',(300, 484),130,75,20,4, screen)
exitButton = gameElements.Button('images/Big_Exit.png',(900,484),130,75,20,4, screen)
screen.blit(bg_img, bg_rect)

Black = (0,0,0)
White = (255,255,255)

#create text
game_status = ''
if gameElements.minigame_3_complete == False:
    game_status ='INCOMPLETE'
elif gameElements.minigame_3_complete == True:
    game_status = 'COMPLETE'

font = pygame.font.Font('PublicPixel-z84yD.ttf', 32)
text = font.render(game_status, True, White, Black)
textRect = text.get_rect()
textRect.center = (600,700)

running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if startButton.command == True:
        if gameElements.minigame_3_complete == False: 
            exec(open('mini_game_3.py').read())
            startButton.command = False
        elif gameElements.minigame_3_complete == True:
            startButton.command = False
    elif exitButton.command == True:
        exec(open('minigame3_scrapyard.py').read())
        exitButton.command = False

    screen.blit(bg_img, bg_rect)
    screen.blit(text,textRect)
    startButton.check_hover()
    exitButton.check_hover()
    pygame.display.flip()
    time.sleep(0.05)
pygame.quit()