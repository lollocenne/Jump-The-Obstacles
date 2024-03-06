import pygame
import random


class Spike:
    def __init__(self, window) -> None:
        self.WINDOW = window
        self.WINDOW_WIDTH: int = window.get_width()
        self.WINDOW_HEIGHT: int = window.get_height()

        self.width: int = 30
        self.height: int = 30

        self.x: float = random.randint(self.WINDOW_WIDTH, self.WINDOW_WIDTH* 1.5)
        self.y: float = self.WINDOW_HEIGHT - self.height

        self.vel = 5

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        self.jumped = False
    
    def move(self) -> None:
        self.x -= self.vel
        self.vel += 0.01

    def outOfScreen(self) -> bool:
        if self.x + self.width <= 0:
            return True
    
    def regenerate(self) -> None:
        self.x = random.randint(self.WINDOW_WIDTH, self.WINDOW_WIDTH* 1.5)
        self.jumped = False
    
    def regenerateOutOfScreen(self) -> None:
        if self.outOfScreen():
            self.regenerate()
    
    def changeWindow(self, window) -> None:
        self.WINDOW = window
        self.WINDOW_WIDTH = window.get_width()
        self.WINDOW_HEIGHT = window.get_height()

        self.y = self.WINDOW_HEIGHT - self.height
        self.hitbox.y = self.y
    
    def update(self):
        self.move()

        self.regenerateOutOfScreen()

        self.hitbox.x = self.x

    def draw(self):
        pygame.draw.rect(self.WINDOW, (50, 50, 50), pygame.Rect(self.x, self.y, self.width, self.height))
