import pygame


class Timer(pygame.sprite.Sprite):
    def __init__(self,round_time=60, size=(220, 50), font_size=24, bgcolor = (135,206,250)):
        super().__init__()
        self.bgcolor = bgcolor
        self.start = pygame.time.get_ticks()
        self.round_time = round_time
        self.image = pygame.Surface(size)
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.rect = self.image.get_rect()
        self.finished = False
        self.seconds_passed = 0

    def update(self):
        self.seconds_passed = (pygame.time.get_ticks() - self.start)/1000
        if self.seconds_passed > self.round_time:
            self.finished = True
        text = f"Time Left: {str(self.seconds_passed)}"
        font_surface = self.font.render(text, True, (0,0,0))
        self.image.fill(self.bgcolor)
        self.image.blit(font_surface, (10,10))
