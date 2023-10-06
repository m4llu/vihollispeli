import pygame                                                                      # Importing all the libraries needed
import random

pygame.mixer.init()                                                                # Initializing pygame.mixer to be able to play sound

enemySpeed = 1
playerSpeed = 3

canvas = pygame.display.set_mode((1000, 1000))                                     # Initializing canvas and setting the window size to 1000x1000
pygame.display.set_caption("Vihollispeli")                                         # Window title

def drawImage(file, x, y):                                                         # Function that lets you draw an image to the screen easily
    image = pygame.image.load(file).convert_alpha()                                # ".convert_alpha" lets .png images appear transparent
    canvas.blit(image, (x, y))

def drawing(canvas, characters, enemies, gameOverImage):                           # Function that draws all characters and enemies to the screen
    for character in characters:                                                   # For loop goes through all instances of the "characters" list and draws them
        file, x, y, isDrawn = character
        if isDrawn:
            drawImage(file, x, y)
    for enemy in enemies:                                                          # Same thing with the "enemies" list
        file, x, y, isDrawn = enemy
        if isDrawn:
            drawImage(file, x, y)
    if gameOverImage[3]:
        drawImage(gameOverImage[0], gameOverImage[1], gameOverImage[2])



def control(characters, event, enemies, gameOverImage):                            # Control function (Basically the whole gameplay)
    if len(characters) > 0:                                                                         
        mainCharacter = characters[0]
        for enemy in enemies:
            if len(characters) > 0:
                del characters[0]
        
        if event.type == pygame.KEYDOWN:                                           # Spawns new enemies if space pressed
            if event.key == pygame.K_SPACE:
                    randx = random.randint(200, 800)
                    randy = random.randint(200, 800)
                    color = random.randint(1, 3)
                    if color == 1:
                        enemies.append(["crocorange.png", randx, randy, True])
                    elif color == 2:
                        enemies.append(["croc.png", randx, randy, True])
                    else:
                        enemies.append(["crocpurple.png", randx, randy, True])
    
        keys = pygame.key.get_pressed()


        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:                               # Character movement
            if mainCharacter[1] < 880:
                mainCharacter[1] += playerSpeed
    
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if mainCharacter[1] > -10:
                mainCharacter[1] -= playerSpeed
    
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if mainCharacter[2] > 0:
                mainCharacter[2] -= playerSpeed
    
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if mainCharacter[2] < 800:
                mainCharacter[2] += playerSpeed
        
        characters.append(mainCharacter)


        for enemy in enemies:                                                     # Collision                                                                  
            if mainCharacter[1] + 100 > enemy[1] and mainCharacter[1] < enemy[1] + 50 and mainCharacter[2] + 200 > enemy[2] and mainCharacter[2] < enemy[2] + 50:
                gameOverImage[3] = True
                pygame.mixer.music.load('Smurf.wav')
                pygame.mixer.music.play(-1)
                del characters[0]
                canvas.fill((0, 0, 0))


def enemyMovement(enemies, speed):                                               # Controls the enemy movement
    for enemy in enemies:
        file, x, y, isDrawn = enemy
        if isDrawn:
            if x >= 1000:
                enemy[1] = -200
                enemy[2] = random.randint(0, 1000)
            enemy[1] += 1


def main():                                                                    # Main function
    characters = [["player.png", 100, 100, True]]                              # Defining the lists
    enemies = [["croc.png", 400, 400, True], ["crocorange.png", 400, 400, True]]
    gameOverImage = ["gameover.png", 250, 200, False]
    while True:                                                                # Main loop
        event = pygame.event.poll() 
        if event.type == pygame.QUIT:                                          # Lets you break the loop
            break


        canvas.fill((0, 50, 0))                                                # Makes the background green
        enemyMovement(enemies, 1)                                              # All the functions needed
        drawing(canvas, characters, enemies, gameOverImage)             
        control(characters, event, enemies, gameOverImage)
        if gameOverImage[3] == True:                                           # Makes you able to restart the game if you die
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    characters = [["player.png", 100, 100, True]]
                    enemies = [["croc.png", 400, 400, True], ["crocorange.png", 400, 400, True]]
                    gameOverImage = ["gameover.png", 250, 200, False]
                    pygame.mixer.music.stop()
        
        pygame.display.flip()

main()