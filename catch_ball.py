import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball 🎮")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (0, 0, 255)
BLACK = (0, 0, 0)

# Basket setup
basket = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 30, 100, 20)

# Ball setup
ball = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)

# Score & font
score = 0
font = pygame.font.SysFont(None, 36)

# Clock for FPS
clock = pygame.time.Clock()

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.x -= 7
    if keys[pygame.K_RIGHT] and basket.right < WIDTH:
        basket.x += 7

    # Move ball
    ball.y += 5
    if ball.y > HEIGHT:
        ball.x = random.randint(0, WIDTH - 20)
        ball.y = 0

    # Check collision
    if basket.colliderect(ball):
        score += 1
        ball.x = random.randint(0, WIDTH - 20)
        ball.y = 0

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, basket)
    pygame.draw.ellipse(screen, RED, ball)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)
