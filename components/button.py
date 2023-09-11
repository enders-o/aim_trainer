import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, text, bgcolor=(135,206,250), fgcolor=(0,0,0)):
        super().__init__()
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.image = pygame.Surface((width, height))
        self.image.fill(bgcolor)
        text_surface = font.render(text, True, fgcolor)
        text_size = font.size(text)
        # Place text into middle of the rectangle
        pos_x = (width - text_size[0]) / 2
        pos_y = (height - text_size[1]) / 2
        self.image.blit(text_surface, (pos_x, pos_y))
        self.rect = self.image.get_rect()
