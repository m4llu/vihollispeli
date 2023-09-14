import pygame
import random

canvas = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Vihollispeli")

def drawImage(file, x, y):
    image = pygame.image.load(file).convert()
    canvas.blit(image, (x, y))

def drawing(canvas, characters):
    for character in characters:
        file, x, y, isDrawn = character
        if isDrawn:
            drawImage(file, x, y)

def control(characters, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            for character in characters:
                character[3] = True

def main():
    characters = [["catSmall.png", 100, 100, True], ["catSmallGreen.png", 300, 300, False]]
    print(characters)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        canvas.fill((0, 0, 0))
        
        drawing(canvas, characters)
        control(characters, event)
        
        pygame.display.flip()

main()