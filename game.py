import pygame
from player import *
from spike import *
from button import *


pygame.font.init()

class Game():
    def __init__(self, window):
        self.WINDOW = window
        self.WINDOW_WIDTH: int = window.get_width()
        self.WINDOW_HEIGHT: int = window.get_height()

        self.FONT_GAMEOVER = pygame.font.SysFont("comicsan", 50)
        self.FONT_POINTS = pygame.font.SysFont("comicsan", 100)
        self.FONT_METERS = pygame.font.SysFont("comicsan", 30)

        self.gameover: bool = False

        self.player = Player(self.WINDOW)
        self.spikes: list[Spike] = [Spike(self.WINDOW), Spike(self.WINDOW), Spike(self.WINDOW)]

        self.getSpikeVelocity()

        self.points: int = 0
        self.meters: int = 0
        self.vel: float = 0

        self.pause: bool = False

        self.restartButton = Button(self.WINDOW, self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2, 100, 40, "RESTART", (100, 100, 100))
    
    def restartGame(self) -> None:
        self.gameover = False
        self.pause = False
        self.spikes = [Spike(self.WINDOW), Spike(self.WINDOW), Spike(self.WINDOW)]

        self.points = 0
        self.meters = 0
    
    def jumpSpike(self, spike: Spike) -> bool:
        if self.player.x > spike.x and not spike.jumped:
            return True
    
    def addPoint(self) -> None:
        for spike in self.spikes:
            if self.jumpSpike(spike):
                self.points += 1
                spike.jumped = True
    
    def getSpikeVelocity(self):
        self.vel = self.spikes[0].vel/20
    
    def changeWindow(self, window) -> None:
        self.WINDOW = window
        self.WINDOW_WIDTH = window.get_width()
        self.WINDOW_HEIGHT = window.get_height()

        self.player.changeWindow(window)

        for spike in self.spikes:
            spike.changeWindow(window)
        
        self.restartButton = Button(self.WINDOW, self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2, 80, 40, "RESTART", (100, 100, 100))

    def update(self) -> None:
        if not self.pause:
            self.getSpikeVelocity()
            self.meters += self.vel

            self.player.update()

            self.addPoint()

            for spike in self.spikes:
                spike.update()

                if self.player.hitbox.colliderect(spike.hitbox):
                    self.gameover = True
                
                for spike2 in self.spikes:
                    if spike != spike2:
                        if spike.hitbox.colliderect(spike2.hitbox):
                            spike.regenerate()
        else:
            if self.restartButton.press():
                self.restartGame()
        

        if self.gameover:
            self.pause = True

    def draw(self) -> None:
        self.WINDOW.fill((50, 50, 150))

        self.player.draw()
        
        for spike in self.spikes:
            spike.draw()

        pointsText = self.FONT_POINTS.render(f"{self.points}", 1, (255, 255, 0))
        self.WINDOW.blit(pointsText, (self.WINDOW_WIDTH/2 - pointsText.get_width()/2, 10))

        metersText = self.FONT_METERS.render(f"{round(self.meters)}m", 1, (255, 255, 255))
        self.WINDOW.blit(metersText, (10, 10))
        
        if self.gameover:
                lostText = self.FONT_GAMEOVER.render("GAME OVER", 1, (255, 0, 0))
                self.WINDOW.blit(lostText, (self.WINDOW_WIDTH/2 - lostText.get_width()/2, self.WINDOW_HEIGHT/4 - lostText.get_height()/2))

                self.restartButton.draw()
