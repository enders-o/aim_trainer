import pygame
from components import Button

from .base_screen import BaseScreen


class WelcomeScreen(BaseScreen):
    def __init__(self, window):
        """
        Creates two buttons on the screen.
        """
        super().__init__(window)
        self.sprites = pygame.sprite.Group()

        self.button1 = Button(200, 100, "Flickshot")
        self.button1.rect.x = 100
        self.button1.rect.y = 300

        self.button2 = Button(200, 100, "Tracking")
        self.button2.rect.x = 400
        self.button2.rect.y = 300

        self.button3 = Button(200, 100, "Precision")
        self.button3.rect.x = 700
        self.button3.rect.y = 300

        self.button4 = Button(200, 100, "Quit")
        self.button4.rect.x = 800
        self.button4.rect.y = 500

        self.button5 = Button(200, 100, "High Scores")
        self.button5.rect.x = 400
        self.button5.rect.y = 500



        self.sprites.add(self.button1)
        self.sprites.add(self.button2)
        self.sprites.add(self.button3)
        self.sprites.add(self.button4)
        self.sprites.add(self.button5)

    def draw(self):
        """Draws the screen"""
        self.window.fill((255, 255, 255))
        self.window.blit(self.button.image, self.button.rect)
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clicked on the buttons? Go to the next screen.
            if self.button1.rect.collidepoint(event.pos): 
                self.running = False
                self.next_screen = "flickshot"
            if self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "tracking"
            if self.button3.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "precision"
            if self.button5.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "scores"
            if self.button4.rect.collidepoint(event.pos):
                self.running = False
                pygame.quit()
            # Button 1 clicked
            if self.button1.rect.collidepoint(event.pos):
                self.persistent["game_type"] = 'flickshot'
            # Button 2 clicked
            if self.button2.rect.collidepoint(event.pos):
                self.persistent["game_type"] = 'tracking'

            if self.button3.rect.collidepoint(event.pos):
                self.persistent["game_type"] = 'precision'
