import pygame, random, time

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Mini Game 1 Snake Game ")

x, y = 600, 400
delta_x, delta_y = 50, 0

food_x, food_y = (random.randrange(0, 1200)//50)*50,(random.randrange(0, 800)//50)*50

body_list = [(x, y)]

clock = pygame.time.Clock()

def snake():
    global x, y, food_x, food_y
    x = (delta_x+x)%1200
    y = (delta_y+y)%800

    body_list.append((x, y))
    
    if (food_x == x and food_y == y):
        while((food_x, food_y) in body_list):
            food_x, food_y = (random.randrange(0, 1200)//50)*50,(random.randrange(0, 800)//50)*50
    else:
        del body_list[0]

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), [food_x,food_y, 50, 50])
    for (i,j) in body_list:
        pygame.draw.rect(screen, (255, 255, 255), [i, j, 50, 50])
    pygame.display.update()

running = True
while running:
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