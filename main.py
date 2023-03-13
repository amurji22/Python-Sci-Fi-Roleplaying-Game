import pygame
import time
import gameElements

pygame.init()

bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

start_button_img = pygame.image.load('Start.png')
start_button_rect = start_button_img.get_rect()

start_button = gameElements.Button(screen_rect.centerx, screen_rect.centery, start_button_img, 0.8, 0.9)


def render():
    screen.blit(bg_img, bg_rect)
    start_button.draw(screen)
    pygame.display.flip()

game_state = gameElements.GameState.TITLE

render()
running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.draw(screen):
                print('START')
    render()
    time.sleep(0.05)
pygame.quit()
