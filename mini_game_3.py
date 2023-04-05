import pygame, time
import gameElements

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Squisher")

# Set up the player
player_width = 50
player_height = 50
player_x = 100
player_y = screen_height - player_height - 50
player_vel = 0
player_acc = 0.5
player_jump_vel = -10
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the object
object_width = 50
object_height = 50
object_x = screen_width
object_y = screen_height - object_height
object_speed = 5
object = pygame.Rect(object_x, object_y, object_width, object_height)

# Set up the score
score = 0
font = pygame.font.Font('PublicPixel-z84yD.ttf', 36)

# Set up the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.bottom == screen_height:
                player_vel = player_jump_vel

    # Apply gravity to the player
    player_vel += player_acc
    player.y += player_vel

    # Keep the player from falling through the bottom of the screen
    if player.bottom > screen_height:
        player.bottom = screen_height
        player_vel = 0

    # Move the object
    object.x -= object_speed

    # Check for collision
    if player.colliderect(object):
        if player.bottom <= object.top + 10:
            score += 1
            print(f"Jump successful! Score: {score}")
            if score % 2 == 0:
                object_speed *= 1.25
                print(f"Speed doubled! New speed: {object_speed}")
            object.x = screen_width
            if score == 10:
                screen.fill((0,0,0))
                msg = font.render("YOU WIN!", True, (255, 255, 255))
                msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(msg, msg_rect)
                pygame.display.update()
                time.sleep(5)
                gameElements.minigame_3_complete = True
                exec(open('win_minigame.py').read())
        else:
            screen.fill((0,0,0))
            msg = font.render("GAME OVER!", True, (255, 255, 255))
            msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            time.sleep(5)
            exec(open('lose_minigame.py').read())

    # Reset the object if it reaches the left side of the screen
    if object.right < 0:
        object.x = screen_width

    # Draw the player and object
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), object)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)
