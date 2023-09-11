import json
from pathlib import Path

import pygame


class Leaderboard(pygame.sprite.Sprite):
    def __init__(self, score, size=(500, 50), font_size=36):
        super().__init__()
        pygame.font.init()
        self.image = pygame.Surface(size)
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.rect = self.image.get_rect()
        self.score = score
        self.scores = []
        self.flick_scores = []
        self.track_scores = []
        self.prec_scores = []

    def update(self):
        self.load_scores()
        #  if scores is empty change first value of score to 0, meaning no score
        if not self.track_scores:
            self.track_scores = [0]
        if not self.prec_scores:
            self.prec_scores = [0]
        if not self.flick_scores:
            self.flick_scores = [0]
        # get high scores from getting first value in corresponding lists
        high_scores = {'tracking': self.track_scores[0], 'flickshot': self.flick_scores[0], 'precision': self.prec_scores[0]}
        text = f"{self.score} high score: {high_scores[self.score]}"
        font_surface = self.font.render(text, True, (0, 0, 0))
        self.image.fill((255, 255, 255))
        self.image.blit(font_surface, (0, 0))

    def load_scores(self):
        filename = Path('scores.json')
        if not filename.exists:
            self.scores = []
        else:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.scores = data
        #  loops through list of dictionaries and if category corresponds store it in new list
        #  after created list, store it descending order
        self.track_scores = sorted([q['score'] for q in self.scores if q['category'] == 'tracking'], reverse=True)
        self.flick_scores = sorted([q['score'] for q in self.scores if q['category'] == 'flickshot'], reverse=True)
        self.prec_scores = sorted([q['score'] for q in self.scores if q['category'] == 'precision'], reverse=True)
