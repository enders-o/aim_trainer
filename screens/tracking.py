import random

import pygame
from components import Circle, TextBox, Timer

from .base_screen import BaseScreen


class TrackGameScreen(BaseScreen):
    def __init__(self, window):
        """The game screen has a shape that moves, and a score box"""
        super().__init__(window)

        self.sprites = pygame.sprite.Group()
        self.shape = Circle(25, speedx=5,speedy=5,fgcolor=(255,0,0),limits=window.get_size())
        self.shape.rect.top = random.randint(50,625)
        self.shape.rect.left = random.randint(0,1030)
        self.scorebox = TextBox()
        self.scorebox.rect.x = 220
        self.timer = Timer()
        self.sprites.add(self.scorebox)
        self.sprites.add(self.timer)
        self.tempval = 0

    def update(self):
        """Deal with key presses outside of the event loop"""
        self.timer.update()
        self.shape.move()
        if self.timer.finished == True:
            self.persistent["score"] = self.scorebox.value
            self.scorebox.write_score([-1,self.scorebox.value,-1])
            self.running = False
            self.next_screen = 'game_over'
        if self.shape.rect.collidepoint(pygame.mouse.get_pos()):
            self.window.fill((255,255,255))
            self.scorebox.value += 1
            self.tempval += 1
        if self.tempval > 30:
            self.tempval = 0
            self.window.fill((255,255,255))
            self.shape.rect.top = random.randint(50,625)
            self.shape.rect.left = random.randint(0,1025)
            pygame.display.update()

        self.scorebox.update()

    def draw(self):
        """Draw the screen"""
        self.window.fill((255, 255, 255))
        self.window.blit(self.button.image, self.button.rect)
        # Draw the sprites
        self.window.blit(self.shape.image, self.shape.rect)
        self.sprites.draw(self.window)
    def manage_event(self, event):
        """
        Event management for the game screen.
        Pressing space increases the speed of the shape.
        Clicking the mouse stops the game.
        """
        pass