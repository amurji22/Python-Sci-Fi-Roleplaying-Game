import pygame, time
import gameElements
        
pygame.init()

bg_img = pygame.image.load('images/background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()


startButton = gameElements.Button('images/Start.png',(600, 384),130,75,20,4, screen)
exitButton = gameElements.Button('images/Exit.png',(1000,700),90,50,12,2, screen)
screen.blit(bg_img, bg_rect)

# def render():
#     screen.blit(bg_img, bg_rect)
#     screen.blit(start_button_img, (384, 150))
#     screen.blit(exit_button_img,(875,555))
#     pygame.display.flip()

# render()

running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         exit_button_rect = exit_button_img.get_rect().move(875,555)
    #         if exit_button_rect.collidepoint(event.pos):
    #             running = False
    #         start_button_rect = start_button_img.get_rect().move(384, 150)
    #         if start_button_rect.collidepoint(event.pos):
    #             exec(open('characterSelectionMenu.py').read())
    # render()

    if startButton.command == True:
        exec(open('characterSelectionMenu.py').read())
        startButton.command = False
    elif exitButton.command == True:
        running = False
        exitButton.command = False

    screen.blit(bg_img, bg_rect)
    startButton.check_hover()
    exitButton.check_hover()
    pygame.display.flip()
    time.sleep(0.05)
pygame.quit()