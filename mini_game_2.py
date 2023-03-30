import pygame

pygame.init()

FPS = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption('Pong')

Black = (0,0,0)
White = (255,255,255)
Gray = (169,169,169)
Red = (255,0,0)
boxColour = Black
Speed = 5

asteroid_x = 5
asteroid_y = 5

asteroid_img = pygame.image.load("images/asteroid.png")
heart_1 = pygame.image.load("images/heart.png")
heart_2 = pygame.image.load("images/heart.png")
heart_3 = pygame.image.load("images/heart.png")

# create the background and its rect object
bg_img = pygame.image.load("images/mini_game_2_background.jpg")
bg_rect = bg_img.get_rect()

Player = pygame.Rect(375,750, 150, 18)
missedPointBox = pygame.Rect(0,750,800,50)
asteroid_rect = asteroid_img.get_rect()

heart_1_rect = heart_1.get_rect()
heart_1_rect.topleft = (20,20)

heart_2_rect = heart_2.get_rect()
heart_2_rect.topleft = (70,20)

heart_3_rect = heart_3.get_rect()
heart_3_rect.topleft = (120,20)

resized_asteroid_img = pygame.transform.scale(asteroid_img, (asteroid_rect.width * 0.15, asteroid_rect.height * 0.15))
resized_asteroid_rect = resized_asteroid_img.get_rect()

resized_asteroid_rect.center = (385,285)


def draw():
    FPS.tick(60)
    screen.blit(bg_img, bg_rect)
    pygame.draw.rect(screen, boxColour, missedPointBox)
    pygame.draw.rect(screen, White, Player)

    screen.blit(resized_asteroid_img, resized_asteroid_rect)

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


hearts_lost = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    resized_asteroid_rect.x += asteroid_x
    resized_asteroid_rect.y += asteroid_y


    
    if resized_asteroid_rect.colliderect(Player):
        asteroid_y *= -1
        Speed += 0.8
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

    draw()



    move()

    Player_Border()

    pygame.display.update()