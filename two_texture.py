import pygame
import sys

pygame.init()

# Set up the window
width, height = 1000, 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Textured Objects Animation')

# Load textures
texture1 = pygame.image.load('peg.png') 
texture2 = pygame.image.load('tex.jpg')  

# Set starting positions
rect1_pos = [50, 50]
rect2_pos = [200, 150]

clock = pygame.time.Clock()

while True:
    window.fill((0, 0, 0))  # Fill the window with black

    # Draw textured objects
    window.blit(texture1, rect1_pos)
    window.blit(texture2, rect2_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update positions (example: moving the objects)
    rect1_pos[0] += 1
    rect2_pos[0] -= 1

    # Rendering
    pygame.display.flip()
    clock.tick(60)  # Control frame rate
