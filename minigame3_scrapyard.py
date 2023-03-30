# import pygame, time
# import gameElements
# from characterSelectionMenu import character_selected

# pygame.init()

# bg_img = pygame.image.load('images/space_background.jpg')
# bg_rect = bg_img.get_rect()

# screen_width = 1200
# screen_height = 740
# screen = pygame.display.set_mode((screen_width, screen_height))

# player = gameElements.Character(character_selected, screen_width, screen_height, scale=0.5, speed=200)

# # render function
# def render():
#     screen.blit(bg_img, bg_rect)
#     screen.blit(player.image, player.rect)

# render()

# #arrow key move variables
# move_left = False
# move_right = False

# #time variables
# time_value = time.time()

# running = True
# while running:
#     #getting the time for the fps
#     delta_time = time.time() - time_value
#     time_value = time.time()
    
#     #event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 move_left = True
#             elif event.key == pygame.K_RIGHT:
#                 move_right = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 move_left = False
#             elif event.key == pygame.K_RIGHT:
#                 move_right = False

#     render()
#     pygame.display.flip()

# pygame.quit()

import pygame, time
import gameElements
from characterSelectionMenu import character_selected

pygame.init()

bg_img = pygame.image.load('images/character_background_backup.jpg')
bg_rect = bg_img.get_rect()

screen_width = 1200
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))

player = gameElements.Character(character_selected, screen_width, screen_height, scale=0.5, speed=200)

# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(player.image, player.rect)

render()

#arrow key move variables
move_left = False
move_right = False

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
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False

    if move_left and player.rect.left > 0:
        player.rect_posx -= player.speed * delta_time
        player.rect.x = round(player.rect_posx)
    elif move_left and player.rect.left <= 0:
        player.rect.x = 0
        #minigame 3 needed
        print("UH OH! No file yet")
        #exec(open('mini_game_1.py').read())

    if move_right and player.rect.right < player.screen_width:
        player.rect_posx += player.speed * delta_time
        player.rect.x = round(player.rect_posx)
    elif move_right and player.rect.right >= player.screen_width:
        player.rect.x = player.screen_width - player.rect.width
        #scapyard needed
        print("UH OH! No file yet")
        #exec(open('mini_game_2.py').read())

    render()
    pygame.display.flip()

pygame.quit()