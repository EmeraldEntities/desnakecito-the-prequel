#####
# - File Name: Desnakecito: The Prequel V0.5
# - Description: The full desnakecito experience!
# - Author: Joseph Wang
# - Date: 11/11/2018
#####
from random import randint, randrange
import pygame, time
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#-- SCREEN SETTINGS --#
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))
#-- SCREEN SETTINGS --#

#-- FUNCTIONS FOR VARIABLES --#
def createFont(font, size):
    #creates a new font
    newFont = pygame.font.SysFont(font, size)
    return newFont

def createTimeLimit(time):
    #creates a time limit for the game
    milliseconds = time*60000
    return milliseconds

def loadImage(image):
    #loads an image and converts it
    newImage = pygame.image.load(image).convert()
    return newImage

def loadImageTransparent(image):
    #loads a transparent image and converts it
    newImage = pygame.image.load(image).convert_alpha()
    return newImage
#-- FUNCTIONS FOR VARIABLES --#

#-- FONTS, IMAGES AND SOUND --#
comicSans40 = createFont("Comic Sans MS", 40)
comicSans30 = createFont("Comic Sans MS", 30)
comicSans20 = createFont("Comic Sans MS", 20)
comicSans15 = createFont("Comic Sans MS", 15)
comicSans10 = createFont("Comic Sans MS", 10)
droid25 = createFont("Droid Serif Pro", 25)
droid30 = createFont("Droid Serif Pro", 30)
droid60 = createFont("Droid Serif Pro", 60)
playbill100 = createFont("Playbill", 100)

titleScreen = loadImage("desnakecito.png")
extrasScreen = loadImage("Credits.png")
loadingBackground = loadImage("loadingBackground.png")
dirtSpawn = loadImage("dirt.png")
iceFields = loadImage("iceFields.png")
forgottenWoodlands = loadImage("woodland.png")
primeCity = loadImage("city.png")
spacialBattlegrounds = loadImage("space.png")
winScreen = loadImage("victory.png")

snowball = loadImageTransparent("snowball.png")
star = loadImageTransparent("star.png")
emerald = loadImageTransparent("emerald.png")
apple = loadImageTransparent("apple.png")
point = loadImageTransparent("pointIndicator.png")

rock = loadImageTransparent("rock.png")
asteroid = loadImageTransparent("asteroid.png")
pineTree = loadImageTransparent("pineTree.png")
tree = loadImageTransparent("tree.png")
building = loadImageTransparent("building.png")

gameLogo = loadImageTransparent("oofLogo.png")
objBackdrop = loadImageTransparent("OBJBackdrop.png")
timerBackdrop = loadImageTransparent("timerBackdrop.png")
            
titleMusic = 'Gentle Sprawl.ogg'
loadingMusic = 'Loading Sprawl.ogg'
sLoadingMusic = 'Slow Loading Sprawl.ogg'
dirtSpawnMusic = 'Dirt Sprawl.ogg'
iceFieldsMusic = 'Icy Sprawl.ogg'
forgottenWoodlandsMusic = 'Woodland Sprawl.ogg'
primeCityMusic = 'Urban Sprawl.ogg'
spacialBattlegroundsMusic = 'Space Sprawl.ogg'

textNoise = pygame.mixer.Sound('textPlay.wav')
textNoise.set_volume(0.1)
eatNoise = pygame.mixer.Sound('biteSound.wav')
eatNoise.set_volume(0.6)
appleNoise = pygame.mixer.Sound("spawnApple.wav")
appleNoise.set_volume(0.6)
deathNoise = pygame.mixer.Sound("deathSound.wav")
deathNoise.set_volume(0.6)
#-- FONTS, IMAGES AND SOUND --#

#-- HIGHSCORE SYSTEM --#
highscoreOpen = open('snakeHighscore.txt', 'r')
pastHighscore = highscoreOpen.readline()
highscoreOpen.close()
#-- HIGHSCORE SYSTEM --#

#-- LORE ANALYSIS --#
stage0Text = 'snakeStage0.txt'
stage1Text = 'snakeStage1.txt'
stage2Text = 'snakeStage2.txt'
stage3Text = 'snakeStage3.txt'
stage4Text = 'snakeStage4.txt'
stage5Text = 'snakeStage5.txt'
#-- LORE ANALYSIS --#

BLACK = (  0,  0,  0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CRIMSON = (65, 0, 0)
WHITE = (255, 255, 255)
BROWN = (210,105,30)
GRAY = (20, 20, 20)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
MALACHITE = (0, 255, 65)
DARK_GREEN = (0, 59, 0)
L_GREEN = (107, 183, 87)
L_GRAY = (219, 217, 217)
L_BLUE = (42, 39, 147)

BODY_COLOUR = RED
HEAD_COLOUR = (255, 183, 0)

#-- LISTS FOR LATER USE --#
textStorage = []

stages = [stage0Text, stage1Text, stage2Text, stage3Text, stage4Text, stage5Text]
levelMusic = [dirtSpawnMusic, dirtSpawnMusic, iceFieldsMusic, forgottenWoodlandsMusic, primeCityMusic, spacialBattlegroundsMusic]

scoreToGet = [7,7,9,11,11,13]

obstacleAmounts = [3,3,13,13,5,17]

obstacleTextures = [rock, rock, pineTree, tree, building, asteroid]

obstacleWidth = [20, 20, 20, 20, 40, 20]

backgroundTextures = [dirtSpawn, dirtSpawn, iceFields, forgottenWoodlands, primeCity, spacialBattlegrounds]

ballTextures = [emerald, emerald, snowball, apple, point, star]

gridColours = [GRAY, GRAY, L_GRAY, L_GREEN, GRAY, L_BLUE]
#-- LISTS FOR LATER USE --#

pygame.display.set_caption("Desnakecito: The Prequel (Deluxe Edition) (Collector's Edition) V.0.5")
pygame.display.set_icon(gameLogo)

TOP = 0
BOTTOM = HEIGHT
MIDDLE = int(WIDTH/2.0)

timeLimit = createTimeLimit(2) 

outline=0

clock = pygame.time.Clock()

#---------------------------------------#
# Functions                             #
#---------------------------------------#
def defineObstacles(stageNumber, obstaclesInGameX, obstaclesInGameY):
    #Generates obstacles that do not spawn in front of the player
    obsRedo = True
    while obsRedo:
        obstacleX = randrange(HSTEP, WIDTH-HSTEP, HSTEP)
        obstacleY = randrange(VSTEP, HEIGHT-VSTEP, VSTEP)
        obsRedo = False
        if obstacleY <= BOTTOM-VSTEP + 15*VSTEP and (obstacleX > MIDDLE-(HSTEP*2) and obstacleX < MIDDLE+(HSTEP*2)):
            obsRedo = True
        for obs in range(len(obstaclesInGameX)):
            if (obstacleX, obstacleY) == (obstaclesInGameX[obs], obstaclesInGameY[obs]):
                obsRedo = True
        
    obstaclesInGameX.append(obstacleX)
    obstaclesInGameY.append(obstacleY)
    
    return obstaclesInGameX, obstaclesInGameY

def drawButton(x, y, text, font, buttonColour, textColour, xPadding, yPadding):
    #Makes a button!
    textToRender, textCoords = drawCenteredText(x, y, text, font, textColour)
    buttonRect = pygame.draw.rect(gameWindow, buttonColour, (textCoords[0]-xPadding, textCoords[1]-yPadding, textToRender.get_width()+2*xPadding, textToRender.get_height()+2*yPadding))
    gameWindow.blit(textToRender, textCoords)
    return buttonRect

def isClicked(button):
    #Checks if a button is clicked
    return button.collidepoint(pygame.mouse.get_pos())

def drawCenteredText(x, y, text, font, fontColour):
    #Returns text that is centered
    fontLocation = font.size(text)
    fontRender = font.render(text, 1, fontColour)
    fontX = x - fontLocation[0] / 2
    fontY = y - fontLocation[1] / 2
    return fontRender, (fontX, fontY)

def drawGameScreen(allAppleX, allAppleY, ballTextures, stageNumber, obstaclesInGameX, obstaclesInGameY, obstacleTextures, obstacleWidth, backgroundTextures, gridColours):
    #The function that draws everything involving the "game" window
    gameWindow.blit(backgroundTextures[stageNumber], (0,0))
    for w in range(0, WIDTH, HSTEP):    #Draws the grid
        pygame.draw.line(gameWindow, gridColours[stageNumber], (w-10, 0), (w-10, HEIGHT), 1)
    for h in range(0, HEIGHT, VSTEP):
        pygame.draw.line(gameWindow, gridColours[stageNumber], (0, h-10),(WIDTH, h-10), 1)
        
    for apple in range(len(allAppleX)): #Draws the apples
        gameWindow.blit(ballTextures[stageNumber], (allAppleX[apple]-10, allAppleY[apple]-10))        
    for obstacle in range(len(obstaclesInGameX)):   #Draws the obstacles
        gameWindow.blit(obstacleTextures[stageNumber], (obstaclesInGameX[obstacle]-10, obstaclesInGameY[obstacle]-10))
    
    for i in range(len(segX)):
        pygame.draw.rect(gameWindow, BODY_COLOUR, (segX[i]-SEGMENT_R, segY[i]-SEGMENT_R, SEGMENT_R*2, SEGMENT_R*2), 2)
    pygame.draw.rect(gameWindow, HEAD_COLOUR, (segX[0]-SEGMENT_R, segY[0]-SEGMENT_R, SEGMENT_R*2, SEGMENT_R*2), outline)
    
    pygame.draw.rect(gameWindow, BROWN, (0, 0, HSTEP/2, HEIGHT,), outline)
    pygame.draw.rect(gameWindow, BROWN, (0, 0, WIDTH, VSTEP/2), outline)
    pygame.draw.rect(gameWindow, BROWN, (WIDTH, 0, -HSTEP/2, HEIGHT), outline)
    pygame.draw.rect(gameWindow, BROWN, (WIDTH, HEIGHT, -WIDTH, -VSTEP/2), outline)

    gameWindow.blit(objBackdrop, (250,0))
    gameWindow.blit(timerBackdrop, (0,0))

    scoreIndicator = comicSans40.render(str(score), 1, WHITE)
    gameWindow.blit(scoreIndicator, (HSTEP/2,0))
    timeLeft = comicSans20.render(str(timeRemaining), 1, WHITE)
    gameWindow.blit(timeLeft, (HSTEP/2, 50))

    if stageNumber != 5:
        gameWindow.blit(*drawCenteredText(WIDTH/2, 20, "Get " + str(scoreToGet[stageNumber]) + " points.", droid30, WHITE))
    else:
        if score < scoreToGet[stageNumber]:
            gameWindow.blit(*drawCenteredText(WIDTH/2, 20, "Get " + str(scoreToGet[stageNumber]) + " points.", droid30, WHITE))
        else:
            gameWindow.blit(*drawCenteredText(WIDTH/2, 20, "Survive." , droid30, WHITE))
    
def drawLoadingScreen(stageNumber, textAlreadyShown, textStorage):
    #Draws the loading screen
    gameWindow.blit(loadingBackground, (0,0))
    
    textAlreadyShown, textStorage = determineText(stageNumber, textAlreadyShown, stages, textStorage)
    return textAlreadyShown

def determineText(stageNumber, textAlreadyShown, stages, textStorage):
    #Figures out what text from what stage needs to be displayed on loading screen.
    textStorage = []
    yPos = 30
    txPos= 80
    while not textAlreadyShown:
        for i in range(len(stages)):
            if i == stageNumber:
                stageText = stages[i]
                
        drawStageText(txPos, yPos, stageText, textStorage, stageNumber)
        textAlreadyShown = True
             
    return textAlreadyShown, textStorage

def drawStageText(xPos, yPos, stageText, textStorage, stageNumber):
    #Actually draws all the text
    currentStory = open(stageText, "r")    #Opens a seperate file
    for line in currentStory:   #Make every line a new item in a list 
        textStorage.append(line[:-1])
    for line in textStorage:    #Make every letter a new item in a new list                        
        lineList = list(line)
        for letter in lineList:     #individually print out every letter
            gameWindow.blit(*drawCenteredText(xPos, yPos, letter, droid30, GREEN))
            textNoise.play()
            pygame.event.clear()
            pygame.time.wait(50)
            xPos = xPos + 10
            pygame.display.update()
        xPos = 80
        yPos = yPos + 30
        pygame.display.update()
        pygame.time.wait(200)
    currentStory.close()
    if stageNumber != 5:    
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-140, "Get", droid30, MALACHITE))
        gameWindow.blit(ballTextures[stageNumber+1], (WIDTH/2+50, HEIGHT - 150))
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-110, "Avoid", droid30, MALACHITE))
        gameWindow.blit(obstacleTextures[stageNumber+1], (WIDTH/2+50, HEIGHT - 120))
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-60, "Press ENTER to continue...", droid30, MALACHITE))
    pygame.display.update()


def drawDeathScreen(events, stageNumber):
    #Draws the screen shown when the player dies
    gameWindow.fill(RED)

    gameWindow.blit(*drawCenteredText(WIDTH/2, 50, "GAME OVER.", playbill100, CRIMSON))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2-30, "> Recollection interrupted.", droid60, CRIMSON))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+90, "Press ENTER to try again.", comicSans30, CRIMSON))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+120, "Or press ESC to escape the recollection.", comicSans15, CRIMSON))
    
    window = "Death"
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                window = "Game"
            elif event.key == pygame.K_ESCAPE:
                stageNumber = stageNumber - 1
                window = "Title"
    return window, stageNumber

def drawTitleScreen(events, gameStarted, gameCompleted, bypassThroughPassword):
    #Draws the title screen
    gameWindow.blit(titleScreen, (0,0))

    if not gameStarted:
        startButton = drawButton(WIDTH/2, HEIGHT/2 - 60, "Start", droid30, GRAY, WHITE, 30, 10)
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2-20, "Begin the recollection of events.", droid25, CRIMSON))
    else:
        startButton = drawButton(WIDTH/2, HEIGHT/2 - 60, "Resume", droid30, GRAY, WHITE, 30, 10)
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2-20, "Restart the recollection.", droid25, CRIMSON))
    
    otherButton = drawButton(WIDTH/2, HEIGHT/2 + 40, "Extras", droid30, GRAY, WHITE, 30, 10)
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+80, "Credits and music selection.", comicSans15, BLACK))
    if gameCompleted:
        freeplayButton = drawButton(WIDTH/2, HEIGHT/2 + 140, "Let me do Freeplay!", droid30, GRAY, WHITE, 30, 10)
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+180, "Starts freeplay! Thank you for completing the game :).", comicSans15, BLACK))
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+200, "This will launch stage 5 again.", comicSans15, BLACK))
    elif bypassThroughPassword:
        freeplayButton = drawButton(WIDTH/2, HEIGHT/2 + 140, "I don't care about lore! Freeplay!", droid30, GRAY, WHITE, 30, 10)
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+180, "This starts freeplay since you BYPASSED THE SYSTEM.", comicSans15, BLACK))
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+200, "This should be only you, Mr. Grigorov. Hi!", comicSans15, BLACK))
    else:
        freeplayButton = drawButton(WIDTH/2, HEIGHT/2 + 140, "Access Freeplay", droid30, GRAY, WHITE, 30, 10)
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+180, "Input a password in the console to access freeplay.", comicSans15, BLACK))
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+200, "Please don't skip the lore though :(", comicSans15, BLACK))
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2+220, "Note: will freeze the game, enter password to fix", comicSans15, BLACK))

    quitButton = drawButton(WIDTH/2, HEIGHT/2 +260, "Quit", droid30, GRAY, WHITE, 25, 8)
    
    window, shouldPlay = "Title", True
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                window = "Loading"
                gameStarted = True
            elif event.key == pygame.K_ESCAPE:
                shouldPlay = False
            elif event.key == pygame.K_i:
                window = "Extras"
        elif event.type == pygame.MOUSEBUTTONUP:
            if isClicked(startButton):
                window = "Loading"
                gameStarted = True
            if isClicked(otherButton):
                window = "Extras"
            if isClicked(freeplayButton):
                if not gameCompleted and not bypassThroughPassword:
                    checkIfTeacher = raw_input("Password?: ")
                    if checkIfTeacher == "nintendo":
                        print "Correct!"
                        bypassThroughPassword = True
                    else:
                        print "Wrong password!"
                else:
                    window = "FPLoading"
            if isClicked(quitButton):
                shouldPlay = False
                    
    return window, shouldPlay, gameStarted, bypassThroughPassword

def drawWinScreen(events, highscoreBeat, pastHighscore, score):
    #Draws the victory screen
    gameWindow.blit(winScreen, (0,0))
    
    gameWindow.blit(*drawCenteredText(WIDTH/2, 50, "VICTORY!", playbill100, WHITE))

    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-180, "> Recollection terminated.", droid60, RED))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-90, "Press ENTER to return to the title.", comicSans20, WHITE))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-60, "Or press ESC to escape the game.", comicSans20, WHITE))

    if highscoreBeat:
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-20, "You beat the highscore! New highscore: " + str(score), comicSans15, WHITE))
    else:
        gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-20, "Sorry, didn't beat the highscore. Current highscore: " + str(pastHighscore), comicSans15, WHITE))
    
    window, shouldPlay = "Win", True
    stageNumber = 0
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                window = "Title"
            elif event.key == pygame.K_ESCAPE:
                shouldPlay = False
         
    return window, shouldPlay, stageNumber

def drawExtrasScreen(events, lockedMusic):
    #draws the "extras" -- Instructions, music locking and credits
    gameWindow.blit(extrasScreen, (0,0))
    window = "Extras"
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/5-30, "Lore is revealed throughout the game.", droid30, WHITE))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/5, "Keep playing to uncover the true story of the despasnake.", droid25, WHITE))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/5+40, "Remember. No recollection is 100% accurate. You WILL notice slight changes.", droid25, RED))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/5+60, "Use WASD or arrow keys to move.", droid25, RED))
    
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2-60, "Created by: Joseph Wang", comicSans20, WHITE))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2-30, "All assets by: Joseph Wang", comicSans20, WHITE))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT/2, "Despacito: Despacito", comicSans15, WHITE))

    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT+-210, "Music Selector", comicSans20, WHITE))
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-190, "This will play one song continuously.", comicSans15, WHITE))
    backButton = drawButton(50, 25, "Back", droid30, GRAY, WHITE, 6, 6)

    lockedMusic = lockMusic(events, lockedMusic)
    gameWindow.blit(*drawCenteredText(WIDTH/2, HEIGHT-10, "Copyright Joseph Wang All Rights Reserved", comicSans10, WHITE))
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                window = "Title"
        elif event.type == pygame.MOUSEBUTTONUP:
            if isClicked(backButton):
                window = "Title"

    return window, lockedMusic

def lockMusic(events, lockedMusic):
    #locks one song and plays it continuously
    lockTitle = drawButton(WIDTH/8+20, HEIGHT-150, "Title", droid30, GRAY, WHITE, 6, 6)
    lockLoading = drawButton(WIDTH/8*2.5, HEIGHT-150, "Loading", droid30, GRAY, WHITE, 6, 6)
    lockSlowLoad = drawButton(WIDTH/8*4, HEIGHT-150, "Loading V2", droid30, GRAY, WHITE, 6, 6)
    lockDirt = drawButton(WIDTH/8*5.5, HEIGHT-150, "Dirt Spawn", droid30, BROWN, WHITE, 6, 6)
    lockIce  = drawButton(WIDTH/8*7, HEIGHT-150, "Ice Fields", droid30, L_GRAY, BLACK, 6, 6)
    lockWoodland = drawButton(WIDTH/8*2, HEIGHT-100, "Forgotten Woodlands", droid30, MALACHITE, BLACK, 6, 6)
    lockCity = drawButton(WIDTH/8*4, HEIGHT-100, "Prime City", droid30, BLACK, WHITE, 6, 6)
    lockSpace = drawButton(WIDTH/8*6, HEIGHT-100, "Spacial Battlegrounds", droid30, L_BLUE, WHITE, 6, 6)
    
    unlockAll = drawButton(WIDTH/2, HEIGHT-40, "Reset Music", droid30, RED, WHITE, 6, 6)
    
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            if isClicked(lockTitle):
                loadMusic(titleMusic)
                lockedMusic = True
            if isClicked(lockDirt):
                loadMusic(dirtSpawnMusic)
                lockedMusic = True
            if isClicked(lockIce):
                loadMusic(iceFieldsMusic)
                lockedMusic = True
            if isClicked(lockWoodland):
                loadMusic(forgottenWoodlandsMusic)
                lockedMusic = True
            if isClicked(lockCity):
                loadMusic(primeCityMusic)
                lockedMusic = True
            if isClicked(lockSpace):
                loadMusic(spacialBattlegroundsMusic)
                lockedMusic = True
            if isClicked(lockLoading):
                loadMusic(loadingMusic)
                lockedMusic = True
            if isClicked(lockSlowLoad):
                loadMusic(sLoadingMusic)
                lockedMusic = True
            if isClicked(unlockAll):
                loadMusic(titleMusic)
                lockedMusic = False
                    
    return lockedMusic

def processLoadingEvents(events, stageNumber, textAlreadyShown, snakeSpeed, startSnakeSpeed, levelMusic, lockedMusic):
    #The function that processes what the player does during the loading screen
    startTime = time.time()
    window = "Loading"
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                if stageNumber == 5:
                    window = "Win"
                    textAlreadyShown = False
                    if not lockedMusic:
                        loadMusic(titleMusic)
                else:
                    window = "Game"
                    stageNumber = stageNumber + 1
                    textAlreadyShown = False
                    startSnakeSpeed = startSnakeSpeed + 1
                    snakeSpeed = startSnakeSpeed
                    if not lockedMusic:
                        loadMusic(levelMusic[stageNumber])
                
            elif event.key == pygame.K_ESCAPE:
                window = "Title"
                textAlreadyShown = False
                if not lockedMusic:
                    loadMusic(titleMusic)
                    
    return window, stageNumber, startTime, textAlreadyShown, snakeSpeed, startSnakeSpeed

def resetGame(startSnakeSpeed, obstacleAmounts, stageNumber):
    #resets the game
    startTime = time.time()
    snakeSpeed = startSnakeSpeed
    stepX = 0
    stepY = -VSTEP                          # initially the snake moves upwards
    segX, segY = [], []
    allAppleX, allAppleY = [], []
    obstaclesInGameX, obstaclesInGameY = [], []
    backKey = "Down"
    amountOfObstacles = obstacleAmounts[stageNumber] + randint(1, 6)
    for obstacle in range(amountOfObstacles):
        obstaclesInGameX, obstaclesInGameY = defineObstacles(stageNumber, obstaclesInGameX, obstaclesInGameY)
    for i in range(4):                      # add coordinates for the head and 3 segments
        segX.append(MIDDLE)
        segY.append(BOTTOM-VSTEP + i*VSTEP)
        
    score = 0
    
    return stepX, stepY, segX, segY, allAppleX, allAppleY, score, backKey, startTime, snakeSpeed, obstaclesInGameX, obstaclesInGameY

def determineGameOutcome(segX, segY, width, height, headLocation, score, scoreToGet, stageNumber, obstaclesInGameX, obstaclesInGameY, obstacleWidth):
    #The function that tells the game whether the player died or succeeded
    #The 5th stage is special -- it won't end if you get the score limit.
    window = "Game"
    highscoreBeat = False
    for w in range(1, len(segX)):
        #If the head hits its own body
        if headLocation == (segX[w], segY[w]):
            if stageNumber != 5:
                window = "Death"
            else:
                if score >= scoreToGet[stageNumber]:
                    window = "Loading"
                else:
                    window = "Death"
                highscoreBeat = checkHighscore(score, pastHighscore)

    for obs in range(0, len(obstaclesInGameX)):
        #If the head hits an obstacle
        if headLocation[0] >= obstaclesInGameX[obs]-10 and headLocation[1] >= obstaclesInGameY[obs]-10 and headLocation[0] <= (obstaclesInGameX[obs] + obstacleWidth[stageNumber]-10) and headLocation[1] <= (obstaclesInGameY[obs] + obstacleWidth[stageNumber]-10):
            if stageNumber != 5:
                window = "Death"
            else:
                if score >= scoreToGet[stageNumber]:
                    window = "Loading"
                else:
                    window = "Death"
                highscoreBeat = checkHighscore(score, pastHighscore)
            
    if timeRemaining <= 0:
        #If the time runs out
        if stageNumber != 5:
            window = "Death"
        else:
            if score >= scoreToGet[stageNumber]:
                window = "Loading"
            else:
                window = "Death"
        highscoreBeat = checkHighscore(score, pastHighscore)
        
    if segX[0] > width - HSTEP/2 or segX[0]<HSTEP/2:
        #If the head hits the barrier
        if stageNumber != 5:
            window = "Death"
        else:
            if score >= scoreToGet[stageNumber]:
                window = "Loading"
            else:
                window = "Death"
            highscoreBeat = checkHighscore(score, pastHighscore)
        
    if segY[0] > height - VSTEP/2 or segY[0] < VSTEP/2:
        #If the head hits the barrier
        if stageNumber != 5:
            window = "Death"
        else:
            if score >= scoreToGet[stageNumber]:
                window = "Loading"
            else:
                window = "Death"
            highscoreBeat = checkHighscore(score, pastHighscore)

    if score >= scoreToGet[stageNumber] and stageNumber != 5:
        #Check to see if we should advance
        window = "Loading"

    if window == "Death":
        deathNoise.play()
    if window == "Loading":
        if not lockedMusic:
            loadMusic(sLoadingMusic)
    return window, highscoreBeat

def processApple(allAppleX, allAppleY, headLocation, score, scoreChecked, segX, segY, timeTillNewApple, appleAdded):
    #processes all apple events
    checkAppleX = allAppleX[:]
    checkAppleY = allAppleY[:]
    for apple in range(len(checkAppleX)):
        #If the apple is eaten what should happen
        applePos = (checkAppleX[apple], checkAppleY[apple])
        if headLocation == applePos:
            eatNoise.play()
            allAppleX.pop(apple)
            allAppleY.pop(apple)         
            score = score + 1
            scoreChecked = False
            
            for bodyPart in range(3):
                segX.append(segX[-1])
                segY.append(segY[-1])

    if timeTillNewApple % 2 == 0 and not appleAdded:
        #spawn in a new apple
        appleNoise.play()
        appleAdded = True
        newAppleLocation(segX, segY, allAppleX, allAppleY, obstaclesInGameX, obstaclesInGameY)

    return allAppleX, allAppleY, score, scoreChecked, appleAdded

def checkForSpeedIncrease(score, snakeSpeed, scoreChecked):
    #increases the speed gradually
    if score % 5 == 0:
        snakeSpeed = snakeSpeed + 2
    scoreChecked = True
    return snakeSpeed, scoreChecked

def newAppleLocation(segX, segY, allAppleX, allAppleY, obstaclesInGameX, obstaclesInGameY):
    #gets a new location for any new apples
    appleRedo = True
    
    while appleRedo:
        appleX = randrange(HSTEP, WIDTH-HSTEP, HSTEP)
        appleY = randrange(VSTEP, HEIGHT-VSTEP, VSTEP)
        applePos = (appleX, appleY)
        appleRedo = False
        for w in range(len(segX)):
            #check to make sure the apple is not in the body
            bodyPos = (segX[w], segY[w])
            if applePos == bodyPos:
                appleRedo = True
        for apple in range(len(allAppleX)):
            #check to make sure that the apple is not in another apple
            newApplePos = (allAppleX[apple], allAppleY[apple])
            if applePos == newApplePos:
                appleRedo = True
        for obs in range(len(obstaclesInGameX)):
            #check to make sure that the apple isn't in an obstacle
            if applePos[0] >= obstaclesInGameX[obs]-10 and applePos[1] >= obstaclesInGameY[obs]-10 and applePos[0] <= (obstaclesInGameX[obs] + obstacleWidth[stageNumber]-10) and applePos[1] <= (obstaclesInGameY[obs] + obstacleWidth[stageNumber]-10):
                    appleRedo = True
        
    allAppleX.append(appleX)
    allAppleY.append(appleY)

def checkHighscore(score, pastHighscore):
    #checks to see if the player has set a high score
    if score > int(pastHighscore):
        highscoreBeat = True
        editHighscore = open('snakeHighscore.txt', 'w')
        editHighscore.write(str(score))
        editHighscore.close()
    else:
        highscoreBeat = False
    return highscoreBeat

def loadMusic(music):
    #loads music
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)    
                    
#---------------------------------------#
# Main Program                          #
#---------------------------------------#

# snake's properties and game's properties
score = 0
scoreCheck = score 
appleAdded, scoreChecked = False, True
SEGMENT_R = 10
APPLE_R = 10
HSTEP = 20
VSTEP = 20

lastAppleCounterTime = timeLimit/1000

allAppleX = []
allAppleY = []
obstaclesInGameX = []
obstaclesInGameY = []

TILEHEIGHT = HEIGHT/VSTEP
TILEWIDTH = WIDTH/HSTEP

startSnakeSpeed = 12
snakeSpeed = startSnakeSpeed
stageNumber = 0
textAlreadyShown, lockedMusic, gameStarted, skipLore, gameCompleted, bypassThroughPassword = False, False, False, False, False, False
shouldResetLevel = False

window = "Title"
backKey = "Down"

#------ THE ACTUAL LOOP ------#
loadMusic(titleMusic)

inPlay = True
while inPlay:
    if window == "Title":
        if shouldResetLevel:
            stageNumber = 0
        pygame.mixer.music.set_volume(0.8)
        #what should happen if the title comes up
        skipLore = False
        window, inPlay, gameStarted, bypassThroughPassword = drawTitleScreen(pygame.event.get(), gameStarted, gameCompleted, bypassThroughPassword)
        
    elif window == "Loading":
        #what should happen if the loading screen comes up
        if not skipLore:
            pygame.mixer.music.set_volume(0.6)
            textAlreadyShown = drawLoadingScreen(stageNumber, textAlreadyShown, textStorage)
            if stageNumber != 5:
                stepX, stepY, segX, segY, allAppleX, allAppleY, score, backKey, startTime, snakeSpeed, obstaclesInGameX, obstaclesInGameY = resetGame(startSnakeSpeed, obstacleAmounts, stageNumber)
            window, stageNumber, startTime, textAlreadyShown, snakeSpeed, startSnakeSpeed = processLoadingEvents(pygame.event.get(), stageNumber, textAlreadyShown, snakeSpeed, startSnakeSpeed, levelMusic, lockedMusic)
        else:
            window = "Win"
            textAlreadyShown = False
            if not lockedMusic:
                loadMusic(titleMusic)

    elif window == "Death":
        #what should happen if the death screen comes up
        pygame.mixer.music.set_volume(0.4)
        stepX, stepY, segX, segY, allAppleX, allAppleY, score, backKey, startTime, snakeSpeed, obstaclesInGameX, obstaclesInGameY = resetGame(startSnakeSpeed, obstacleAmounts, stageNumber)
        
        window, stageNumber = drawDeathScreen(pygame.event.get(), stageNumber)

    elif window == "Win":
        #what should happen if the win screen comes up
        startSnakeSpeed = 12
        gameStarted = False
        if not bypassThroughPassword:
            gameCompleted = True
        window, inPlay, stageNumber = drawWinScreen(pygame.event.get(), highscoreBeat, pastHighscore, score)
    
    elif window == "Extras":
        #what should happen if the "extras" screen comes up
        window, lockedMusic = drawExtrasScreen(pygame.event.get(), lockedMusic)
        
    elif window == "FPLoading":
        shouldResetLevel = True
        #what should happen during the freeplay loading
        stageNumber = 5
        stepX, stepY, segX, segY, allAppleX, allAppleY, score, backKey, startTime, snakeSpeed, obstaclesInGameX, obstaclesInGameY = resetGame(startSnakeSpeed, obstacleAmounts, stageNumber)
        if not lockedMusic:
            loadMusic(levelMusic[randint(1,5)])
        window = "Game"
        skipLore = True
        
    elif window == "Game":
        #How to actually run the game
        pygame.mixer.music.set_volume(0.8)
        
        elapsed = round(time.time() - startTime, 2)
        timeRemaining = timeLimit/1000 - elapsed
        
        appleTimeCounter = round(timeRemaining, 0)          #This is to make sure only one apple is added
        if appleTimeCounter != lastAppleCounterTime:
            appleAdded = False
        lastAppleCounterTime = appleTimeCounter

        keyAlreadyInput = False                             #Important so that people don't spam keys to kill the snake
        headLocation = (segX[0], segY[0])

        if not scoreChecked:
            snakeSpeed, scoreChecked = checkForSpeedIncrease(score, snakeSpeed, scoreChecked)
        clock.tick(snakeSpeed)          #speeds up the snake
        
        window, highscoreBeat = determineGameOutcome(segX, segY, WIDTH, HEIGHT, headLocation, score, scoreToGet, stageNumber, obstaclesInGameX, obstaclesInGameY, obstacleWidth)
        
        appleX, appleY, score, scoreChecked, appleAdded = processApple(allAppleX, allAppleY, headLocation, score, scoreChecked, segX, segY, appleTimeCounter, appleAdded)

        pygame.event.clear()
        keys = pygame.key.get_pressed()

        drawGameScreen(allAppleX, allAppleY, ballTextures, stageNumber, obstaclesInGameX, obstaclesInGameY, obstacleTextures, obstacleWidth, backgroundTextures, gridColours)

        if keys[pygame.K_ESCAPE]:
            window = "Title"
            stageNumber = stageNumber - 1
            if not lockedMusic:
                loadMusic(titleMusic)
        #Checks movement of the snake
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if backKey != "Left" and not keyAlreadyInput:
                stepX = -HSTEP
                stepY = 0
                backKey = "Right"
                keyAlreadyInput = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if backKey != "Right" and not keyAlreadyInput:
                stepX = HSTEP
                stepY = 0
                backKey = "Left"
                keyAlreadyInput = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if backKey != "Up" and not keyAlreadyInput:
                stepX = 0
                stepY = -VSTEP
                backKey = "Down"
                keyAlreadyInput = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if backKey != "Down" and not keyAlreadyInput:
                stepX = 0
                stepY = VSTEP
                backKey = "Up"
                keyAlreadyInput = True

    #Coving the segments
        lastIndex = len(segX)-1
        for i in range(lastIndex,0,-1):     # starting from the tail, and going backwards:
            segX[i]=segX[i-1]               # every segment takes the coordinates
            segY[i]=segY[i-1]               # of the previous one
    #Moving the head
        segX[0] = segX[0] + stepX
        segY[0] = segY[0] + stepY
        
    if not textAlreadyShown:
        pygame.display.update()

#---------------------------------------#
pygame.quit()
