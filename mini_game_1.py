import pygame, random, time

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Mini Game 1 Snake Game ")

star_image = pygame.image.load("images/star.png")
# -- get its rect object
star_rect = star_image.get_rect()

x, y = 600, 400
delta_x, delta_y = 50, 0

food_x, food_y = (random.randrange(0, 1200)//50)*50,(random.randrange(0, 800)//50)*50

body_list = [(x, y)]

clock = pygame.time.Clock()

game_over = False

font = pygame.font.SysFont("bahnschrift", 100)

def snake():
    global x, y, food_x, food_y, game_over, star_rect
    x = (delta_x+x)%1200
    y = (delta_y+y)%800

    if((x,y) in body_list):
        game_over = True
        return

    body_list.append((x, y))
    
    if (food_x == x and food_y == y):
        while((food_x, food_y) in body_list):
            food_x, food_y = (random.randrange(0, 1050)//50)*50,(random.randrange(0, 700)//50)*50
    else:
        del body_list[0]

    screen.fill((0, 0, 0))
    score = font.render("Score: "+ str(len(body_list)), True, (255, 255, 0))
    screen.blit(score, [0, 0])
    #pygame.draw.rect(screen, (255, 0, 0), [food_x,food_y, 50, 50])
    screen.blit(star_image, (food_x,food_y, 50, 50))
    for (i,j) in body_list:
        pygame.draw.rect(screen, (255, 255, 255), [i, j, 50, 50])
    pygame.display.update()

running = True
while running:
    if(game_over):
        screen.fill((0,0,0))
        msg = font.render("GAME OVER!", True, (255, 255, 255))
        screen.blit(msg, [1200//3, 800//3])
        pygame.display.update()
        time.sleep(10)
        pygame.quit()
   #Handle the close or x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(delta_x != 50):
                    delta_x = -50
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                if(delta_x != -50):
                    delta_x = 50
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                if(delta_y != 50):
                    delta_y = -50
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                if(delta_x != -50):
                    delta_y = 50
            snake()   
    else:
       snake()
    clock.tick(10)
pygame.quit()