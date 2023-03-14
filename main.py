import pygame
import time

<<<<<<< Updated upstream
=======
class Button:
    def __init__(self, image, pos, height, radius, elevation):
        
        #attributes
        self.command = False
        self.pressed = False
        self.radius = radius
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.image = pygame.image.load(image)
        self.top_rect = self.image.get_rect()
        self.top_rect.center = (pos)

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(self.top_rect.width,height))
        self.bottom_rect.center = (pos)
        self.bottom_colour = "#495d6e"

    def drawBackground(self):
        screen.blit(bg_img, bg_rect)


    def draw(self):
        self.top_rect.centery = self.original_y_pos - self.dynamic_elevation
  

        # self.bottom_rect.midtop = self.top_rect.midtop
        # self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation


        pygame.draw.rect(screen,self.bottom_colour, self.bottom_rect, border_radius=self.radius)
        screen.blit(self.image,self.top_rect)
        self.check_click()


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 4
                self.pressed  = True
            else: 
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print('click')
                    self.pressed = False
                    self.command = True
        else:
            self.dynamic_elevation = self.elevation
        
             

        
        

>>>>>>> Stashed changes

pygame.init()

bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((1200, 768))
screen_rect = screen.get_rect()

<<<<<<< Updated upstream
start_button_img = pygame.image.load('Start.png')
start_button_rect = start_button_img.get_rect()

exit_button_img = pygame.image.load('Exit.png')
exit_button_rect = exit_button_img.get_rect()


def render():
    screen.blit(bg_img, bg_rect)
    screen.blit(start_button_img, (384, 150))
    screen.blit(exit_button_img,(875,555))
    pygame.display.flip()



render()
=======

startButton = Button('Start.png',(600, 384),130,75,25)
exitButton = Button('Exit.png',(1000,700),90,50,20)
screen.blit(bg_img, bg_rect)

# def render():
#     screen.blit(bg_img, bg_rect)
#     screen.blit(start_button_img, (384, 150))
#     screen.blit(exit_button_img,(875,555))
#     pygame.display.flip()



# render()
>>>>>>> Stashed changes
running = True
# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
<<<<<<< Updated upstream
        elif event.type == pygame.MOUSEBUTTONDOWN:
            exit_button_rect = exit_button_img.get_rect().move(875,555)
            if exit_button_rect.collidepoint(event.pos):
                running = False
            start_button_rect = start_button_img.get_rect().move(384, 150)
            if start_button_rect.collidepoint(event.pos):
                exec(open('characterSelectionMenu.py').read())
        
    render()
=======
    #     elif event.type == pygame.MOUSEBUTTONDOWN:
    #         exit_button_rect = exit_button_img.get_rect().move(875,555)
    #         if exit_button_rect.collidepoint(event.pos):
    #             running = False
    #         start_button_rect = start_button_img.get_rect().move(384, 150)
    #         if start_button_rect.collidepoint(event.pos):
    #             exec(open('characterSelectionMenu.py').read())
        
    # render()

    if startButton.command == True:
        exec(open('characterSelectionMenu.py').read())
        startButton.command = False
    elif exitButton.command == True:
        running = False
        exitButton.command = False


    startButton.drawBackground()
    startButton.draw()
    exitButton.draw()
    pygame.display.flip()
>>>>>>> Stashed changes
    time.sleep(0.05)
pygame.quit()