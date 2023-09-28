import pygame
import random

enemySpeed = 1
playerSpeed = 3

canvas = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Vihollispeli")

def drawImage(file, x, y):
    image = pygame.image.load(file).convert_alpha()
    canvas.blit(image, (x, y))

def drawing(canvas, characters, enemies):
    for character in characters:
        file, x, y, isDrawn = character
        if isDrawn:
            drawImage(file, x, y)
    for enemy in enemies:
        file, x, y, isDrawn = enemy
        if isDrawn:
            drawImage(file, x, y)

def control(characters, event, enemies):
    if len(characters) > 0:
        mainCharacter = characters[0]
        for enemy in enemies:
            del characters[0]
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for enemy in enemies:
                    enemy[3] = True 
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_RIGHT]:
            if mainCharacter[1] < 880:
                mainCharacter[1] += playerSpeed
    
        if keys[pygame.K_LEFT]:
            if mainCharacter[1] > -10:
                mainCharacter[1] -= playerSpeed
    
        if keys[pygame.K_UP]:
            if mainCharacter[2] > 0:
                mainCharacter[2] -= playerSpeed
    
        if keys[pygame.K_DOWN]:
            if mainCharacter[2] < 800:
                mainCharacter[2] += playerSpeed
        
        characters.append(mainCharacter)

def enemyMovement(enemies, enemySpeed):
    speed = 1
    enemy1 = enemies[0]
    if enemy1[3] == True:
        if enemy1[1] > 870:
            speed = 1
        if enemy1[1] < 10:
            speed = -1
        enemy1[1] += speed

        

def main():
    characters = [["player.png", 100, 100, True]]
    enemies = [["croc.png", 400, 400, False]]
    print(characters)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        canvas.fill((0, 50, 0))
        
        drawing(canvas, characters, enemies)
        control(characters, event, enemies)
        enemyMovement(enemies, enemySpeed)
        
        pygame.display.flip()

main()