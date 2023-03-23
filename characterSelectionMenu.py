import pygame, time
import gameElements

pygame.init()

# create the screen and its rect object
screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

mainMenuButton = gameElements.Button('images/Exit.png',(1000,700),90,50,12,2, screen)
characterOne = gameElements.characterButton('images/Character_One.png','images/Character_One_Underlay.png',(300,430),12,2, screen)
characterTwo = gameElements.characterButton('images/Character_Two.png','images/Character_Two_Underlay.png',(600,430),12,2, screen)
characterThree = gameElements.characterButton('images/Character_Three.png','images/Character_Three_Underlay.png',(900,430),12,2, screen)

# create the background and its rect object
bg_img = pygame.image.load("images/character_background.jpg")
bg_rect = bg_img.get_rect()


# create the text image and its rect
text_img = pygame.image.load("images/choose.png")
text_rect = text_img.get_rect()

# render function
def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(text_img, (320, 0))

render()

# variable to store the character selected
character_selected = "none"

# game loop
nextScene = False
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if mainMenuButton.command == True:
        exec(open('main.py').read())
        mainMenuButton.command = False
    elif characterOne.command == True:
        character_selected = "images/Character_One.png"
        exec(open('before_capture_alien.py').read())
    elif characterTwo.command == True:
        character_selected = "images/Character_Two.png"
        exec(open('before_capture_alien.py').read())
    elif characterThree.command == True:
        character_selected = "images/Character_Three.png"
        exec(open('before_capture_alien.py').read())
    #if(nextScene):
        #exec(open('before_capture_alien.py').read())
 
    render()
    characterOne.check_hover()
    characterTwo.check_hover()
    characterThree.check_hover()
    mainMenuButton.check_hover()
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
