import json
from pathlib import Path

import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, value=0, size=(200,50), font_size=24, bgcolor = (135,206,250)):
        super().__init__()
        self.value = value
        self.bgcolor = bgcolor
        pygame.font.init()
        self.image = pygame.Surface(size)
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.rect = self.image.get_rect()

    def update(self):
        text = "Score: "+str(self.value)
        font_surface = self.font.render(text, True, (0,0,0))
        self.image.fill(self.bgcolor)
        self.image.blit(font_surface, (0, 10))
    def write_score(self, scores):
        categories = {0:'flickshot',1:'tracking',2:'precision'}
        filename = Path('scores.json')
        # if file doesn't exists, create file and write to it
        if not filename.exists():
            with open(filename,'w') as file:
                # from the scores given, will be in form eg:[-1, 15, -1]
                # this line finds the first index where the value is NOT -1 and returns the index
                # index corresponds to where score is from
                index = scores.index(next(filter(lambda score: score != -1, scores)))
                # append json to file
                json.dump([{'category': categories[index], 'score': scores[index]}], file)
        else:
            # if file exists open file
            with open(filename,'r') as file:
                # get json object from file
                obj = json.load(file)
                index = scores.index(next(filter(lambda score: score != -1, scores)))
                # append new score to object
                obj.append({'category': categories[index], 'score': scores[index]})
                # overwrite file with new object appended
                with open(filename, 'w') as f:
                    json.dump(obj, f)