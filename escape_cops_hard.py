import pygame, time
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

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
ship_rect.y = screen.get_height() / 2 

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

# load the Roated cops coming from the bottom 
cop4_img = pygame.image.load("images/cop_ship_rotatated.png")
cop5_img = pygame.image.load("images/cop_ship_rotatated.png")
cop6_img = pygame.image.load("images/cop_ship_rotatated.png")
cop4_rect = cop4_img.get_rect()
cop5_rect = cop5_img.get_rect()
cop6_rect = cop6_img.get_rect()
# set the starting positions of the cops
cop4_rect.x = 100
cop5_rect.x = 1000
cop6_rect.x = 550
#Start from the bottom
cop4_rect.y = 700
cop5_rect.y = 700
cop6_rect.y = 700



# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(ship_img, ship_rect)

    screen.blit(cop1_img, cop1_rect)
    screen.blit(cop2_img, cop2_rect)
    screen.blit(cop3_img, cop3_rect)

    screen.blit(cop4_img, cop4_rect)
    screen.blit(cop5_img, cop5_rect)
    screen.blit(cop6_img, cop6_rect)

    pygame.display.flip()



cops_passed_counter = 50
cop_speed = (0, 2)
cop_speed_up = (0,-2)
cop_x = 2
#create Explosion class
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"images/Explosion_Images/exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()

explosion_group = pygame.sprite.Group()

running = True
# game loop
while running:

    clock.tick(fps)
    

    explosion_group.draw(screen)
    explosion_group.update()
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            explosion = Explosion(pos[0], pos[1])
            explosion_group.add(explosion)
            x, y = pos
            if cop1_rect.collidepoint(x, y):
                cop1_rect.center = (random.randint(50,300), 0)
            if cop2_rect.collidepoint(x, y):
                cop2_rect.center = (random.randint(350,900), 0)
            if cop3_rect.collidepoint(x, y):
                cop3_rect.center = (random.randint(950,1100), 0)
            if cop4_rect.collidepoint(x, y):
                cop4_rect.center = (random.randint(50,300), 700)
            if cop5_rect.collidepoint(x, y):
                cop5_rect.center = (random.randint(350,900), 700)
            if cop6_rect.collidepoint(x, y):
                cop6_rect.center = (random.randint(950,1100), 700)
            

    # cops move downward
    cop1_rect = cop1_rect.move(cop_speed)
    cop2_rect = cop2_rect.move(cop_speed)
    cop3_rect = cop3_rect.move(cop_speed)
    # cops move up
    cop4_rect = cop4_rect.move(cop_speed_up)
    cop5_rect = cop5_rect.move(cop_speed_up)
    cop6_rect = cop6_rect.move(cop_speed_up)
    # cops respawns at top of screen if it goes out at bottom
    if cop1_rect.y > screen.get_rect().height:
        cop1_rect.center = (random.randint(50,300), 0)
    if cop2_rect.y > screen.get_rect().height:
        cops_passed_counter -= 1
        cop2_rect.center = (random.randint(350,900), 0)
    if cop3_rect.y > screen.get_rect().height:
        cop3_rect.center = (random.randint(950,1100), 0)
    # cops respawns at bottom of the screen if it goes out at the top
    if cop4_rect.y < 0:
        cop4_rect.center = (random.randint(50,300), 700)
    if cop5_rect.y < 0:
        cops_passed_counter -= 1
        cop5_rect.center = (random.randint(350,900), 700)
    if cop6_rect.y < 0:
        cop6_rect.center = (random.randint(950,1100), 700)

    # activate second level,  increase speed of cops
    if (cops_passed_counter == 40):
        cop_speed = (0, 3)
        cop_speed_up = (0, -3)
    # activate third level, increase speed of cops
    if (cops_passed_counter == 30):
        cop_speed = (0, 4)
        cop_speed_up = (0, -4)
    # activate fourth level, increase speed of cops
    if (cops_passed_counter == 20):
        cop_speed = (0, 5)
        cop_speed_up = (0, -5)
    # if all cops are escaped
    if (cops_passed_counter == 0):
        # open end file
        exec(open("successful_escape.py").read())

   # detect collision between ship and cops
    if ship_rect.colliderect(cop1_rect) or  ship_rect.colliderect(cop2_rect) or ship_rect.colliderect(cop3_rect) or ship_rect.colliderect(cop4_rect) or ship_rect.colliderect(cop5_rect) or ship_rect.colliderect(cop6_rect):
        # open the scene to bargain or fight with cop
        exec(open("if_captured.py").read())


    
    keys = pygame.key.get_pressed()
    # make sure the user does not move the bank off the screen
    if keys[pygame.K_LEFT] and ship_rect.x > 0:
            ship_rect = ship_rect.move(-3.5,0)
    if keys[pygame.K_RIGHT] and ship_rect.x < 1020:
            ship_rect = ship_rect.move(3.5,0)
    if keys[pygame.K_UP] and ship_rect.y > 0:
            ship_rect = ship_rect.move(0,-3.5)
    if keys[pygame.K_DOWN] and ship_rect.y < 660:
            ship_rect = ship_rect.move(0,3.5)    

    
    pygame.display.update()
    time.sleep(0.001)
    render()

pygame.quit()