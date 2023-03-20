import pygame, time, random
from characterSelectionMenu import character_selected

pygame.init()

# create screen
screen = pygame.display.set_mode((1200, 740))

# load the background and create its rect
bg_img = pygame.image.load("space_background.jpg")
bg_rect = bg_img.get_rect()

# load the three aliens
speed_alien_img = pygame.image.load("speed_alien.png")
healer_alien_img = pygame.image.load("health_alien.png")
ammo_alien_img = pygame.image.load("ammo_alien.png")
speed_alien_rect = speed_alien_img.get_rect()
healer_alien_rect = healer_alien_img.get_rect()
ammo_alien_rect = ammo_alien_img.get_rect()

# load the aliens into a random space on the screen
speed_alien_rect.x = random.randrange(0, 400 - speed_alien_rect.width)
speed_alien_rect.y = random.randrange(0, screen.get_rect().height - speed_alien_rect.height)
healer_alien_rect.x = random.randrange(400, 800 - healer_alien_rect.width)
healer_alien_rect.y = random.randrange(0, screen.get_rect().height - healer_alien_rect.height)
ammo_alien_rect.x = random.randrange(800, 1200 - ammo_alien_rect.width)
ammo_alien_rect.y = random.randrange(0, screen.get_rect().height - ammo_alien_rect.height)


# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(speed_alien_img, speed_alien_rect)
    screen.blit(healer_alien_img, healer_alien_rect)
    screen.blit(ammo_alien_img, ammo_alien_rect)

    pygame.display.flip()

# set speeds of the aliens
speed_s = [2, 2]
speed_h = [2, 2]
speed_a = [2, 2]

# boolean to detect when an alien is picked
alien_picked = False
# string to be set to the type of alien picked
alien_type = "none"


# game loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                
                # if the healer alien is clicked
                if healer_alien_rect.collidepoint(event.pos):
                    alien_type = "healer"
                    exec(open('before_space_town.py').read())

                # if the speed alien is clicked
                if speed_alien_rect.collidepoint(event.pos):
                    alien_type = "speed"
                    exec(open('before_space_town.py').read())

                # if the ammo alien is clicked
                if ammo_alien_rect.collidepoint(event.pos):
                    alien_type = "ammo"
                    exec(open('before_space_town.py').read())
                   

    print(character_selected)
    # move the aliens on the screen with their speeds
    speed_alien_rect = speed_alien_rect.move(speed_s)
    healer_alien_rect = healer_alien_rect.move(speed_h)
    ammo_alien_rect = ammo_alien_rect.move(speed_a)

    # if the aliens try to go outside of the screen, reverse their speed
    if speed_alien_rect.x < 0 or speed_alien_rect.x > screen.get_rect().width - speed_alien_rect.width:
        speed_s[0] = -speed_s[0]
    if speed_alien_rect.y < 0 or speed_alien_rect.y > screen.get_rect().height - speed_alien_rect.height:
        speed_s[1] = -speed_s[1]

    if healer_alien_rect.x < 0 or healer_alien_rect.x > screen.get_rect().width - healer_alien_rect.width:
        speed_h[0] = -speed_h[0]
    if healer_alien_rect.y < 0 or healer_alien_rect.y > screen.get_rect().height - healer_alien_rect.height:
        speed_h[1] = -speed_h[1]

    if ammo_alien_rect.x < 0 or ammo_alien_rect.x > screen.get_rect().width - ammo_alien_rect.width:
        speed_a[0] = -speed_a[0]
    if ammo_alien_rect.y < 0 or ammo_alien_rect.y > screen.get_rect().height - ammo_alien_rect.height:
        speed_a[1] = -speed_a[1]

    # if the aliens collide with eachother, reverse their speed
    if healer_alien_rect.colliderect(ammo_alien_rect):
        speed_h[0] = -speed_h[0]
        speed_h[1] = -speed_h[1]
        speed_a[0] = -speed_a[0]
        speed_a[1] = -speed_a[1]
    if healer_alien_rect.colliderect(speed_alien_rect):
        speed_h[0] = -speed_h[0]
        speed_h[1] = -speed_h[1]
        speed_s[0] = -speed_s[0]
        speed_s[1] = -speed_s[1]
    if speed_alien_rect.colliderect(ammo_alien_rect):
        speed_s[0] = -speed_s[0]
        speed_s[1] = -speed_s[1]
        speed_a[0] = -speed_a[0]
        speed_a[1] = -speed_a[1]

    render()


    time.sleep(0.01)


pygame.quit()
