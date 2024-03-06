import pygame


class Player():
    def __init__(self, window):
        self.WINDOW = window
        self.WINDOW_WIDTH: int = window.get_width()
        self.WINDOW_HEIGHT: int = window.get_height()

        self.width: int = 50
        self.height: int = 50

        self.x: float = self.WINDOW_WIDTH/6 - self.width/2
        self.y: float = self.WINDOW_HEIGHT - self.height

        self.vel: int = 5
        self.jumpVel: float = 15
        self.vely: float = 0

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move(self) -> None:
        self.jump()

        self.vely = self.gravity(self.vely)

        if self.y + self.height + self.vely <= self.WINDOW_HEIGHT:
            self.y += self.vely
        else:
            self.y = self.WINDOW_HEIGHT - self.height
            self.vely = 0
    
    @staticmethod
    def gravity(v: float) -> float:
        g = 0.6
        return v + g

    def jump(self) -> None:
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.y + self.height == self.WINDOW_HEIGHT:
            self.vely -= self.jumpVel
    
    def changeWindow(self, window) -> None:
        self.WINDOW = window
        self.WINDOW_WIDTH = window.get_width()
        self.WINDOW_HEIGHT = window.get_height()

        self.y = self.WINDOW_HEIGHT - self.height
    
    def update(self):
        self.move()
        
        self.hitbox.y = self.y

    def draw(self):
        pygame.draw.rect(self.WINDOW, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
