import pygame, time
import gameElements
from characterSelectionMenu import character_selected

pygame.init()

bg_img = pygame.image.load('images/town_background.jpg')
bg_rect = bg_img.get_rect()

sign_img = pygame.image.load("images/small_sign_one.png")

screen_width = 1200
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))

backBtn = gameElements.Button('images/back_button.png',(180,100),100, 80, 20, 10, screen)

player = gameElements.Character(character_selected, screen_width, screen_height, scale=0.5, speed=300)

# render function
def render():
    screen.blit(bg_img, bg_rect)
    backBtn.check_hover()
    screen.blit(sign_img, (500, 400))
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
        exec(open('minigame2_startscreen.py').read())

    if move_right and player.rect.right < player.screen_width:
        player.rect_posx += player.speed * delta_time
        player.rect.x = round(player.rect_posx)
    elif move_right and player.rect.right >= player.screen_width:
        player.rect.x = player.screen_width - player.rect.width
        exec(open('minigame1_startscreen.py').read())

    if backBtn.command == True:
        exec(open('explore_town.py').read())
        backBtn.command = False

    render()
    pygame.display.flip()

pygame.quit()
