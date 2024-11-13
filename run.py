# simulation/run.py

import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent Simulation")

# Create environment and agent
environment = Environment(WIDTH, HEIGHT)
agent = Agent(environment, x=WIDTH // 2, y=HEIGHT // 2)

# Font for displaying position
font = pygame.font.Font(None, 36)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))  # Fill screen with black background
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move("up")
    if keys[pygame.K_DOWN]:
        agent.move("down")
    if keys[pygame.K_LEFT]:
        agent.move("left")
    if keys[pygame.K_RIGHT]:
        agent.move("right")
    
    # Draw agent (as a simple circle)
    pygame.draw.circle(screen, (0, 255, 0), (agent.x, agent.y), 10)
    
    # Display agent's position
    position_text = font.render(f"Position: ({agent.x}, {agent.y})", True, (255, 255, 255))
    screen.blit(position_text, (10, 10))
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(30)

pygame.quit()
