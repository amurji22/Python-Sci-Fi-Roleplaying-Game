import pygame
import time

pygame.init()

bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

start_button_img = pygame.image.load('Start.png')
start_button_rect = start_button_img.get_rect()

exit_button_img = pygame.image.load('Exit.png')
exit_button_rect = exit_button_img.get_rect()


def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(start_button_img, (384, 150))
    screen.blit(exit_button_img,(875,555))
    pygame.display.flip()


render()
running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    render()
    time.sleep(0.05)
pygame.quit()
