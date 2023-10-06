import pygame
import random

pygame.mixer.init()

enemySpeed = 1
playerSpeed = 3

canvas = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Vihollispeli")

def drawImage(file, x, y):
    image = pygame.image.load(file).convert_alpha()
    canvas.blit(image, (x, y))

def drawing(canvas, characters, enemies, gameOverImage):
    for character in characters:
        file, x, y, isDrawn = character
        if isDrawn:
            drawImage(file, x, y)
    for enemy in enemies:
        file, x, y, isDrawn = enemy
        if isDrawn:
            drawImage(file, x, y)
    if gameOverImage[3]:
        drawImage(gameOverImage[0], gameOverImage[1], gameOverImage[2])

def control(characters, event, enemies, gameOverImage):
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

        # Tarkista osuuko pelaaja viholliseen
        for enemy in enemies:
            if mainCharacter[1] + 50 > enemy[1] and mainCharacter[1] < enemy[1] + 50 and mainCharacter[2] + 50 > enemy[2] and mainCharacter[2] < enemy[2] + 50:
                gameOverImage[3] = True
                pygame.mixer.music.load('Smurf.wav')
                pygame.mixer.music.play(-1)
                del characters[0]
                canvas.fill((0, 0, 0))


def enemyMovement(enemies, speed):
    for enemy in enemies:
        file, x, y, isDrawn = enemy
        if isDrawn:
            if x >= 1000:
                enemy[1] = -200
                enemy[2] = random.randint(0, 1000)
            enemy[1] += 1

def main():
    characters = [["player.png", 100, 100, True]]
    enemies = [["croc.png", 400, 400, False]]
    gameOverImage = ["gameover.png", 250, 200, False]
    print(characters)
    enemy1 = enemies[0]
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break


        canvas.fill((0, 50, 0))
        enemyMovement(enemies, 1)
        drawing(canvas, characters, enemies, gameOverImage)
        control(characters, event, enemies, gameOverImage)
        
        pygame.display.flip()

main()