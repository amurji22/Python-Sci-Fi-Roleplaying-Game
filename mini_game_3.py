import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Maze")

# Set up game variables
player_pos = [0, 0]
maze_size = 20
maze = [[random.randint(0, 1) for i in range(maze_size)] for j in range(maze_size)]
obstacles = []
powerups = []
lives = 3

# Set up game functions
def draw_maze():
    for i in range(maze_size):
        for j in range(maze_size):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (j*20, i*20, 20, 20))

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.circle(screen, (255, 0, 0), obstacle, 10)

def draw_powerups():
    for powerup in powerups:
        pygame.draw.circle(screen, (0, 255, 0), powerup, 10)

def move_player(dx, dy):
    player_pos[0] += dx
    player_pos[1] += dy

def check_collision():
    for obstacle in obstacles:
        distance = ((player_pos[0]-obstacle[0])**2 + (player_pos[1]-obstacle[1])**2)**0.5
        if distance < 20:
            return True
    return False

# render function
def render():
    screen.fill((0, 0, 0))
    draw_maze()
    draw_obstacles()
    draw_powerups()

render()


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_player(0, -20)
            elif event.key == pygame.K_DOWN:
                move_player(0, 20)
            elif event.key == pygame.K_LEFT:
                move_player(-20, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(20, 0)
    
    # Draw the game
    render()
    pygame.display.flip()

pygame.quit()
