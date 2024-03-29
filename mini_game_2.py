import pygame, random, time
import gameElements


pygame.init()

FPS = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption('Pong')

#colours
Black = (0,0,0)
White = (255,255,255)
Gray = (169,169,169)
Red = (255,0,0)
boxColour = Black

green = (0, 255, 0)
blue = (0, 0, 128)

#game element speeds
Speed = 5
asteroid_x = 5
asteroid_y = 5
fast_asteroid_speed = 10

#import images
asteroid_img = pygame.image.load("images/asteroid.png")
og_fast_asteroid_img = pygame.image.load("images/flaming_asteroid.png")
heart_1 = pygame.image.load("images/heart.png")
heart_2 = pygame.image.load("images/heart.png")
heart_3 = pygame.image.load("images/heart.png")
bg_img = pygame.image.load("images/mini_game_2_background.jpg")

#rectangles
Player = pygame.Rect(375,750, 150, 18)
missedPointBox = pygame.Rect(0,750,800,50)

#rect objects from images
bg_rect = bg_img.get_rect()
asteroid_rect = asteroid_img.get_rect()
og_fast_ateroid_rect = og_fast_asteroid_img.get_rect()
heart_1_rect = heart_1.get_rect()
heart_2_rect = heart_2.get_rect()
heart_3_rect = heart_3.get_rect()

#position rect objects
heart_1_rect.topleft = (20,20)
heart_2_rect.topleft = (70,20)
heart_3_rect.topleft = (120,20)

#create new resized rect objects
resized_asteroid_img = pygame.transform.scale(asteroid_img, (asteroid_rect.width * 0.15, asteroid_rect.height * 0.15))
resized_asteroid_rect = resized_asteroid_img.get_rect()

fast_asteroid = pygame.transform.scale(og_fast_asteroid_img, (og_fast_ateroid_rect.width * 0.25, og_fast_ateroid_rect.height * 0.25))
#fast_asteroid = pygame.transform.scale(asteroid_img, (asteroid_rect.width * 0.15, asteroid_rect.height * 0.15))
fast_asteroid_rect = fast_asteroid.get_rect()

flipped_fast_asteroid = pygame.transform.flip(fast_asteroid,True,False)
flipped_fast_asteroid_rect = flipped_fast_asteroid.get_rect()

resized_asteroid_rect.center = (385,285)

#create text
final_points_earned = 0
font = pygame.font.Font('PublicPixel-z84yD.ttf', 32)
text = font.render(str(final_points_earned), True, green, blue)
textRect = text.get_rect()
textRect.center = (650,35)


def draw():
    FPS.tick(60)
    screen.blit(bg_img, bg_rect)
    pygame.draw.rect(screen, boxColour, missedPointBox)
    pygame.draw.rect(screen, White, Player)

    screen.blit(resized_asteroid_img, resized_asteroid_rect)

    screen.blit(text, textRect)


    if hearts_lost == 0:
        screen.blit(heart_1, heart_1_rect)
        screen.blit(heart_2, heart_2_rect)
        screen.blit(heart_3, heart_3_rect)
    elif hearts_lost == 1:
        screen.blit(heart_1, heart_1_rect)
        screen.blit(heart_2, heart_2_rect)
    elif hearts_lost == 2:
        screen.blit(heart_1, heart_1_rect)

def move():
    if keys[pygame.K_RIGHT]:
        Player.x += Speed

    if keys[pygame.K_LEFT]:
        Player.x -= Speed


def Player_Border():
    if Player.x >= 645:
        Speed = 0
        Player.x = 644
    if Player.x <= 5:
        Speed = 0
        Player.x = 6

def makeFastAsteroid():
    fast_asteroid_rect.center = (random.randint(10,790),0)
    fast_asteroid_speed = 10


def moveFastAsteroid():
    fast_asteroid_rect.y += fast_asteroid_speed
    screen.blit(fast_asteroid, fast_asteroid_rect)

    # if flip_asteroid == False:
    #     fast_asteroid_rect.y += fast_asteroid_speed
    #     screen.blit(fast_asteroid, fast_asteroid_rect)
    # else:
    #     flipped_fast_asteroid_rect.center = fast_asteroid_rect.center
    #     flipped_fast_asteroid_rect.y += fast_asteroid_speed
    #     screen.blit(flipped_fast_asteroid, flipped_fast_asteroid_rect)

hearts_lost = 0
points_earned = 0

make_asteroid_move = False
out_of_bounds = False

points_till_fast_asteroid = random.randint(1,3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if hearts_lost == 3:
        screen.fill((0,0,0))
        msg = font.render("GAME OVER!", True, (255, 255, 255))
        screen.blit(msg, [800//3, 800//3])
        pygame.display.update()
        time.sleep(5)
        exec(open("lose_minigame.py").read())

    resized_asteroid_rect.x += asteroid_x
    resized_asteroid_rect.y += asteroid_y

    if final_points_earned == 20:
        screen.fill((0,0,0))
        msg = font.render("YOU WIN!", True, (255, 255, 255))
        screen.blit(msg, [800//3, 800//3])
        pygame.display.update()
        time.sleep(5)
        gameElements.minigame_2_complete = True
        exec(open("win_minigame.py").read())

    if points_earned == points_till_fast_asteroid:
        fast_asteroid_speed = 10
        makeFastAsteroid()
        points_earned = 0
        points_till_fast_asteroid = random.randint(1,3)
        out_of_bounds = False
        make_asteroid_move = True

    if fast_asteroid_rect.colliderect(Player) and out_of_bounds == False:
        fast_asteroid_speed *= -1
        Speed += 0.8
        final_points_earned += 1 
    elif fast_asteroid_rect.colliderect(missedPointBox):
        boxColour = Red
        hearts_lost += 1 
        fast_asteroid_rect.bottomright=(0,0)
        fast_asteroid_speed = 0
        out_of_bounds = True


    if resized_asteroid_rect.colliderect(Player):
        asteroid_y *= -1
        Speed += 0.8
        points_earned += 1
        final_points_earned += 1 
    elif resized_asteroid_rect.colliderect(missedPointBox):
        asteroid_y *= -1
        boxColour = Red
        hearts_lost += 1
    
    if resized_asteroid_rect.top <= 0:
        asteroid_y *= -1
        boxColour = Black

    if resized_asteroid_rect.left <0 or resized_asteroid_rect.right >= 800:
        asteroid_x *= -1
        boxColour = Black



     
        

    keys = pygame.key.get_pressed()

    text = font.render("Score:" +  str(final_points_earned), True, White, Black)
    textRect = text.get_rect()
    textRect.center = (665,40)

    draw()

    if make_asteroid_move == True:
        moveFastAsteroid()

    move()

    Player_Border()

    pygame.display.update()
