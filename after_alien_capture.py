import pygame
from capture_alien import alien_type

pygame.init()

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 740))
screen_rect = screen.get_rect()

# load the background and create its rect
bg_img = pygame.image.load("images/after_alien_capture_background.jpg")
bg_rect = bg_img.get_rect()

# load the alien that was picked
alien_img = pygame.image.load(alien_type)
alien_rect = alien_img.get_rect()

# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(alien_img, (540,250))
  
    alien_chosen = ""
    end_text = ""

# create the strings to be used for the text depending on alien that was picked
    if(alien_type == "images/health_alien.png"):
        alien_chosen = "health alien"
        end_text = "This alien will provide you an extra life in the future!"
    elif (alien_type == "images/ammo_alien.png"):
        alien_chosen = "ammo alien"
        end_text = "This alien will provide your spaceship extra ammo later!"
    elif (alien_type == "images/speed_alien.png"):
        alien_chosen = "speed alien"
        end_text = "This alien will increase the speed of your spaceship later!"

  # create the text 
    label = pygame.font.Font('verdana.ttf', 40)
    label_two = pygame.font.Font('verdana.ttf', 40)
    font_image_one = label.render("You have chosen the " + alien_chosen + "!", True, (0,0,0))
    font_image_two = label_two.render(end_text, True, (0,0,0))
    screen.blit(font_image_one, (10,500))
    screen.blit(font_image_two, (10, 550))

    pygame.display.flip()


# game loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # if the space bar is pressed, move to next scene
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # open the before space town scene
                exec(open('before_space_town.py').read())
    print(alien_type)

    render()

pygame.quit()
