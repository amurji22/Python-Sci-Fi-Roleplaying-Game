import pygame
import time

pygame.init()

bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

def render():
    screen.blit(bg_img, bg_rect)
    pygame.display.flip()


render()
running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    render()
    time.sleep(0.05)


pygame.quit()
