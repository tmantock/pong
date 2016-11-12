import pygame, sys
form pygame.locals import *

#Number of frames per second
#Change this value to speed up or slow down the speed of the game

FPS = 200

#Global varaible for use throughout program later change to use classes
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

#main function for game
def main():
    pygame.init()
    global DISPLAYSURF

    FPSCLOCK = pygame.time.clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pong')

    while True: #main game loop
        for event in pygame.event.get():
            pygame.quit()
            sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
