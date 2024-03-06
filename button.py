import pygame


class Button():
    def __init__(self, window, x: float, y: float, width: float, height: float, text: str = "", color: tuple = (50, 50, 50), textColor: tuple = (255, 255, 255)):
        self.WINDOW = window
        self.WINDOW_WIDTH: int = window.get_width()
        self.WINDOW_HEIGHT: int = window.get_height()

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.string = text

        self.color = color
        self.textColor = textColor

        self.FONT = pygame.font.SysFont("comicsan", 25)
        self.text = self.FONT.render(self.string, True, self.textColor)

        self.hitbox = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)

    def press(self) -> bool:
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()

            if self.hitbox.collidepoint(mouse[0], mouse[1]):
                return True
    
    def draw(self) -> None:
        pygame.draw.rect(self.WINDOW, self.color, self.hitbox)
        self.WINDOW.blit(self.text, (self.x - self.text.get_width()/2, self.y - self.text.get_height()/2))
