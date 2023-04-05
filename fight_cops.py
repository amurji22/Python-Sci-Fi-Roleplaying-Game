import pygame, time
import random
import gameElements

pygame.init()

# create screen
screen = pygame.display.set_mode((1200, 768))

# load the background and create its rect
bg_img = pygame.image.load("images/escape_background.jpg")
bg_rect = bg_img.get_rect()

# load the spaceship
ship_img = pygame.image.load("images/spaceship.png")
ship_rect = ship_img.get_rect()
# move ship to the bottom middle of screen
ship_rect.x = screen.get_width() / 2 - 100
ship_rect.y = screen.get_height() - 120

# load the cops
cop1_img = pygame.image.load("images/cop_ship.png")
cop2_img = pygame.image.load("images/cop_ship.png")
cop3_img = pygame.image.load("images/cop_ship.png")
cop1_rect = cop1_img.get_rect()
cop2_rect = cop2_img.get_rect()
cop3_rect = cop3_img.get_rect()
# set the starting positions of the cops
cop1_rect.x = 100
cop2_rect.x = 1000
cop3_rect.x = 550

RED = (0, 0, 0)
RED_2 = (0, 0, 0)

laser_move_y = 2
x = (ship_rect.centerx)
y = (ship_rect.centery)
pew_pew = pygame.Rect(1200,y,15,20)
pew_pew_2 = pygame.Rect(1200,y,15,20)

def render():
    screen.blit(bg_img, bg_rect)
    
    pygame.draw.rect(screen, RED, pew_pew)
    pygame.draw.rect(screen,RED_2, pew_pew_2)

    screen.blit(ship_img, ship_rect)

    screen.blit(cop1_img, cop1_rect)
    screen.blit(cop2_img, cop2_rect)
    screen.blit(cop3_img, cop3_rect)
    
    if(gameElements.healer_power_up):
        if hearts_lost == 0:
            screen.blit(heart_1, heart_1_rect)
            screen.blit(heart_2, heart_2_rect)
        elif hearts_lost == 1:
            screen.blit(heart_1, heart_1_rect)
    else:
        if hearts_lost == 1:
            screen.blit(heart_1, heart_1_rect)

    pygame.display.flip()

def moveit_it():
    global RED
    RED = (255, 0, 0)
    pew_pew.y -= laser_move_y
def moveit_it_2():
    global RED_2
    RED_2 = (255, 0, 0)
    pew_pew_2.y -= laser_move_y

if(gameElements.healer_power_up):
    hearts_lost = 0
else:
    hearts_lost = 1

heart_1 = pygame.image.load("images/heart.png")
heart_2 = pygame.image.load("images/heart.png")
heart_1_rect = heart_1.get_rect()
heart_2_rect = heart_2.get_rect()
heart_1_rect.topleft = (20,20)
heart_2_rect.topleft = (70,20)

cops_passed_counter = 50
cop_speed = (0, 1)
cop_x = 2

move_speed_ship_R = (0,0)
move_speed_ship_L = (0,0)

if (gameElements.speed_power_up):
    move_speed_ship_L = (2.5,0)
    move_speed_ship_R = (-2.5,0)
else:
    move_speed_ship_L = (1.8,0)
    move_speed_ship_R = (-1.8,0)

move = False
move_2 = False
running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()
    # make sure the user does not move the bank off the screen
    if keys[pygame.K_LEFT] and ship_rect.x > 0:
        ship_rect = ship_rect.move(move_speed_ship_R)
    if keys[pygame.K_RIGHT] and ship_rect.x < 1020:
        ship_rect = ship_rect.move(move_speed_ship_L)
    if keys[pygame.K_SPACE]:
        if pew_pew.y < 0:
            pew_pew.y = ship_rect.centery
            pew_pew.x = ship_rect.centerx
        if pew_pew.x == 1200:
            pew_pew.x = ship_rect.centerx
        if pew_pew.y == -20:
            move = False
            pew_pew.x = 1200
        move = True
        
    if move:
        moveit_it()
        if pew_pew.y < 500:
            if keys[pygame.K_SPACE]:
                if pew_pew_2.y < 0:
                    pew_pew_2.y = ship_rect.centery
                    pew_pew_2.x = ship_rect.centerx
                if pew_pew_2.x == 1200:
                    pew_pew_2.x = ship_rect.centerx
                if pew_pew_2.y == -20:
                    move_2 = False
                    pew_pew.x = 1200
                move_2 = True

    if move_2:
        moveit_it_2()

        
    

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
        cop_speed = (0, 2)
    # activate third level, increase speed of cops
    if (cops_passed_counter == 30):
        cop_speed = (0, 3)
    # activate fourth level, increase speed of cops
    if (cops_passed_counter == 20):
        cop_speed = (0, 4)
    # if all cops are escaped
    if (cops_passed_counter == 0):
        # open end file
        exec(open("successful_escape.py").read())
    # detect collision between ship and cops
    if ship_rect.colliderect(cop1_rect) or  ship_rect.colliderect(cop2_rect) or ship_rect.colliderect(cop3_rect):
        cop1_rect.center = (random.randint(50,300), 0)
        cop2_rect.center = (random.randint(350,900), 0)
        cop3_rect.center = (random.randint(950,1100), 0)
        hearts_lost += 1 
    if(hearts_lost == 2):
        # open the scene to explore town when the ship is exploded
        exec(open("exploded_ship.py").read())
    if pew_pew.colliderect(cop1_rect) or pew_pew_2.colliderect(cop1_rect):
        cop1_rect.center = (random.randint(50,300), 0)
        cops_passed_counter -= 1
        print("HIT")
    if pew_pew.colliderect(cop2_rect) or pew_pew_2.colliderect(cop2_rect):
        cop2_rect.center = (random.randint(350,900), 0)
        cops_passed_counter -= 1
        print("HIT")
    if pew_pew.colliderect(cop3_rect) or pew_pew_2.colliderect(cop3_rect):
        cop3_rect.center = (random.randint(950,1100), 0)
        cops_passed_counter -= 1
        print("HIT")

    render()

pygame.quit()
