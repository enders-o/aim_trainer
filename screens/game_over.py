import pygame
from components import Button, TextBox

from .base_screen import BaseScreen


class GameOverScreen(BaseScreen):
    def __init__(self, window):
        """
        The game over screen has two buttons and a textbox
        """
        super().__init__(window)
        self.sprites = pygame.sprite.Group()

        self.button1 = Button(200, 100, "Main Menu")
        self.button1.rect.x = 300
        self.button1.rect.y = 400

        self.button2 = Button(200, 100, "Quit")
        self.button2.rect.x = 300
        self.button2.rect.y = 550

        self.textbox = TextBox(value="", size=(500, 100), bgcolor=(255,255,255))
        self.textbox.rect.x = 100
        self.textbox.rect.y = 150

        self.sprites.add(self.button1, self.button2, self.textbox)

    def update(self):
        """Updates the sprites based on the persistent data in the game"""
        self.textbox.value = f"Your final score was {self.persistent['score']}!"
        self.textbox.update()

    def draw(self):
        """Draw the sprites"""
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        """Go back to the welcome screen if we click button 1"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            if self.button2.rect.collidepoint(event.pos):
                self.running = False
                pygame.quit()
