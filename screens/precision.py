import random

import pygame
from components import Circle, TextBox, Timer

from .base_screen import BaseScreen


class PrecGameScreen(BaseScreen):
    def __init__(self, window):
        """The game screen has a shape that moves, and a score box"""
        super().__init__(window)
        self.sprites = pygame.sprite.Group()
        # create 4 shapes
        self.shapes = []
        for x in range(0,6):
            circle = Circle(10, fgcolor=(255,0,0))
            circle.rect.top = random.randint(50,625)
            circle.rect.left = random.randint(0,1025)
            self.sprites.add(circle)
            self.shapes.append(circle)
        self.scorebox = TextBox()
        self.scorebox.rect.x = 300
        self.timer = Timer()
        self.sprites.add(self.scorebox)
        self.sprites.add(self.timer)

    def update(self):
        """Deal with key presses outside of the event loop"""

        # Make sure we update our scorebox
        self.timer.update()
        self.scorebox.update()
        if self.timer.finished == True:
            self.persistent["score"] = self.scorebox.value
            self.scorebox.write_score([-1,-1,self.scorebox.value])
            self.running = False
            self.next_screen = 'game_over'

    def draw(self):
        """Draw the screen"""
        self.window.fill((255, 255, 255))
        self.window.blit(self.button.image, self.button.rect)

        # Draw the sprites
        self.sprites.draw(self.window)
        for shape in self.shapes:
            self.window.blit(shape.image, shape.rect)

    def manage_event(self, event):
        """
        Event management for the game screen.
        Pressing space increases the speed of the shape.
        Clicking the mouse stops the game.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            for shape in self.shapes:
                if shape.rect.collidepoint(event.pos):
                    self.window.fill((255,255,255))
                    shape.rect.top = random.randint(50,625)
                    shape.rect.left = random.randint(0,1025)
                    self.scorebox.value += 10
                    pygame.display.update()
