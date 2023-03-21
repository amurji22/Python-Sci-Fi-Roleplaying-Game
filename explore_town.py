import pygame, time
import gameElements

pygame.init()

bg_img = pygame.image.load('town_background.png')
bg_rect = bg_img.get_rect()

screen_width = 1200
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

player = gameElements.Character("Character_One.png", screen_width, screen_height, scale=0.5, speed=200)

# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(player.image, player.rect)

render()

#time variables
time_value = time.time()

running = True
while running:
    #getting the time for the fps
    delta_time = time.time() - time_value
    time_value = time.time()
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pressed_keys = pygame.key.get_pressed()

    player.movement(pressed_keys, delta_time)

    render()
    pygame.display.flip()

pygame.quit()