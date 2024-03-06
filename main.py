import pygame
import pyautogui
from game import *


pygame.font.init()

FONT_GAMEOVER = pygame.font.SysFont("comicsan", 50)

WINDOW_WIDTH: int = pyautogui.size()[0]/2
WINDOW_HEIGHT: int = pyautogui.size()[1]/2
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Jump The Obstacles")

game = Game(WINDOW)

def checkWindowChange() -> bool:
    if WINDOW_WIDTH != WINDOW.get_width() or WINDOW_HEIGHT != WINDOW.get_height():
        return True

def update() -> None:
    if checkWindowChange():
        game.changeWindow(WINDOW)
        global WINDOW_WIDTH
        global WINDOW_HEIGHT
        
        WINDOW_WIDTH = WINDOW.get_width()
        WINDOW_HEIGHT = WINDOW.get_height()

    game.update()

def draw() -> None:
    game.draw()

    pygame.display.update()

def main() -> None:
    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        update()
        draw()
    
    pygame.quit()


if __name__ == "__main__":
    main()
