import pygame, time
import random

pygame.init()

# create screen
screen = pygame.display.set_mode((1200, 768))

# load the background and create its rect
bg_img = pygame.image.load("escape_background.jpg")
bg_rect = bg_img.get_rect()

# load the spaceship
ship_img = pygame.image.load("spaceship.png")
ship_rect = ship_img.get_rect()
# move ship to the bottom middle of screen
ship_rect.x = screen.get_width() / 2 - 100
ship_rect.y = screen.get_height() - 120

# load the cops
cop1_img = pygame.image.load("cop_ship.png")
cop2_img = pygame.image.load("cop_ship.png")
cop3_img = pygame.image.load("cop_ship.png")
cop1_rect = cop1_img.get_rect()
cop2_rect = cop2_img.get_rect()
cop3_rect = cop3_img.get_rect()
# set the starting positions of the cops
cop1_rect.x = 100
cop2_rect.x = 1000
cop3_rect.x = 550

# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(ship_img, ship_rect)

    screen.blit(cop1_img, cop1_rect)
    screen.blit(cop2_img, cop2_rect)
    screen.blit(cop3_img, cop3_rect)

    pygame.display.flip()



cops_passed_counter = 50
cop_speed = (0, 2)
cop_x = 2


running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # cops move downward
    cop1_rect = cop1_rect.move(cop_speed)
    cop2_rect = cop2_rect.move(cop_speed)
    cop3_rect = cop3_rect.move(cop_speed)
    # cops respawns at top of screen if it goes out at bottom
    if cop1_rect.y > screen.get_rect().height:
        cop1_rect.center = (random.randint(50,300), 0)
    if cop2_rect.y > screen.get_rect().height:
        cops_passed_counter -= 1
        cop2_rect.center = (random.randint(350,900), 0)
    if cop3_rect.y > screen.get_rect().height:
        cop3_rect.center = (random.randint(950,1100), 0)

    # activate second level,  increase speed of cops
    if (cops_passed_counter == 40):
        cop_speed = (0, 3)
    # activate third level, increase speed of cops
    if (cops_passed_counter == 30):
        cop_speed = (0, 4)
    # activate fourth level, increase speed of cops
    if (cops_passed_counter == 20):
        cop_speed = (0, 5)
    # if all cops are escaped
    if (cops_passed_counter == 0):
        # open end file
        exec(open("successful_escape.py").read())

   # detect collision between ship and cops
    if ship_rect.colliderect(cop1_rect):
        # open the scene to bargain or fight with cop
        exec(open("").read())
    if ship_rect.colliderect(cop2_rect):
        # open the scene to bargain or fight with cop
        exec(open("").read())
    if ship_rect.colliderect(cop3_rect):
        # open the scene to bargain or fight with cop
        exec(open("").read())


    
    keys = pygame.key.get_pressed()
    # make sure the user does not move the bank off the screen
    if keys[pygame.K_LEFT] and ship_rect.x > 0:
        ship_rect = ship_rect.move(-3.5,0)
    if keys[pygame.K_RIGHT] and ship_rect.x < 1020:
        ship_rect = ship_rect.move(3.5,0)

    
      
    time.sleep(0.001)
    render()

pygame.quit()
