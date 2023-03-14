import pygame
import time

pygame.init()

bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

main_menu_button_img = pygame.image.load('Exit.png')
main_menu_button_rect = main_menu_button_img.get_rect()

def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(main_menu_button_img,(875,555))
    pygame.display.flip()


render()
running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            main_menu_button_rect = main_menu_button_img.get_rect().move(875,555)
            if main_menu_button_rect.collidepoint(event.pos):
                exec(open('main.py').read())
    
    render()
    time.sleep(0.05)


pygame.quit()
