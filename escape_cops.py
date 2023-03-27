import pygame, time
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

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
#create Explosion class
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"Explosion_Images/exp{num}.png")
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
        exec(open("").read())

   # detect collision between ship and cops
    if ship_rect.colliderect(cop1_rect):
        explosion = Explosion(ship_rect.x, ship_rect.y)
        explosion_group.add(explosion)
        time.sleep(5)
        running = False
        # open the scene to bargain or fight with cop
        #exec(open("").read())
    if ship_rect.colliderect(cop2_rect):
        explosion = Explosion(ship_rect.x, ship_rect.y)
        explosion_group.add(explosion)
        time.sleep(5)
        running = False
        # open the scene to bargain or fight with cop
        #exec(open("").read())
    if ship_rect.colliderect(cop3_rect):
        explosion = Explosion(ship_rect.x, ship_rect.y)
        explosion_group.add(explosion)
        time.sleep(5)
        running = False
        # open the scene to bargain or fight with cop
        #exec(open("").read())


    
    keys = pygame.key.get_pressed()
    # make sure the user does not move the bank off the screen
    if keys[pygame.K_LEFT] and ship_rect.x > 0:
        ship_rect = ship_rect.move(-3.5,0)
    if keys[pygame.K_RIGHT] and ship_rect.x < 1020:
        ship_rect = ship_rect.move(3.5,0)

    
    pygame.display.update()
    time.sleep(0.001)
    render()

pygame.quit()