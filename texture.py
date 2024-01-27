import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_square():
    glBegin(GL_TRIANGLES)
    # Define vertices and texture coordinates for two triangles forming a square
    # Triangle 1
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    
    # Triangle 2
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)
    glEnd()

def add_texture():
    image = pygame.image.load('box.jpg')
    data = pygame.image.tostring(image, 'RGBA', 1)
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

def draw_cube():
    glPushMatrix()
    draw_square()
    glPopMatrix()

    # Apply rotations for the other sides of the cube based on the table
    rotations = [
        (90, 0, 1, 0),
        (-90, 1, 0, 0),
        (180, 0, 1, 0),
        (-90, 0, 1, 0),
        (90, 1, 0, 0)
    ]

    for angle, x, y, z in rotations:
        glPushMatrix()
        glRotatef(angle, x, y, z)
        draw_square()
        glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    add_texture()

    glEnable(GL_DEPTH_TEST)  # Enable depth testing
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)  # Move the cube back along the z-axis
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glRotatef(1, 1, 1, 1)  # Rotate the cube
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
