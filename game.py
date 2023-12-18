import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
FONT = pygame.font.Font(None, 36)

# Game variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 10
opponent_speed = 7
player_score = 0
opponent_score = 0
MAX_SCORE = 10  # Define the maximum score for game over

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define game objects
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)

# Define ball movement
ball_dx = ball_speed_x
ball_dy = ball_speed_y

def ball_restart():
    global ball_dx, ball_dy
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx *= -1
    ball_dy *= -1

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    if ball.left <= 0:
        player_score += 1
        ball_restart()
    if ball.right >= WIDTH:
        opponent_score += 1
        ball_restart()

    # Player collision with ball
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_dx *= -1

    # AI opponent movement
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    # Clear the screen
    screen.fill(BLACK)

    # Draw game objects
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    player_text = FONT.render(f"Player: {player_score}", True, WHITE)
    opponent_text = FONT.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (WIDTH - 150, 20))
    screen.blit(opponent_text, (20, 20))

    # Check for game over
    if player_score >= MAX_SCORE:
        winner_text = FONT.render("Player wins!", True, WHITE)
        screen.blit(winner_text, (WIDTH // 2 - 100, HEIGHT // 2))
        running = False
    elif opponent_score >= MAX_SCORE:
        winner_text = FONT.render("Opponent wins!", True, WHITE)
        screen.blit(winner_text, (WIDTH // 2 - 110, HEIGHT // 2))
        running = False

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

