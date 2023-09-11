import pygame
from components import Button, Leaderboard

from .base_screen import BaseScreen


class ScoresScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        self.sprites = pygame.sprite.Group()
        self.track = Leaderboard(score='tracking')
        self.track.rect.x = 100
        self.track.rect.y = 300

        self.flick = Leaderboard(score='flickshot')
        self.flick.rect.x = 100
        self.flick.rect.y = 100

        self.prec = Leaderboard(score='precision')
        self.prec.rect.x = 100
        self.prec.rect.y = 200
        self.button1 = Button(200, 100, "Main Menu")
        self.button1.rect.x = 300
        self.button1.rect.y = 400

        self.button2 = Button(200, 100, "Quit")
        self.button2.rect.x = 300
        self.button2.rect.y = 550

        self.sprites.add(self.button1, self.button2)

        # self.sprites.add(self.scores)

    def draw(self):
        self.track.update()
        self.prec.update()
        self.flick.update()
        self.window.fill((255,255,255))
        self.window.blit(self.track.image, self.track.rect)
        self.window.blit(self.prec.image, self.prec.rect)
        self.window.blit(self.flick.image, self.flick.rect)
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
