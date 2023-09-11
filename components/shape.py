import pygame


class Circle(pygame.sprite.Sprite):
    def __init__(self, radius, center=(0,0), speedx=0, speedy=0, bgcolor=(255, 255, 255), fgcolor=(255, 255, 255), limits=None):
        super().__init__()
        self.image = pygame.Surface((radius*2, radius*2))
        self.image.fill((bgcolor))
        pygame.draw.circle(self.image, fgcolor, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.speedx = speedx
        self.speedy = speedy
        self.limits = limits

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.check_limits()

    def check_limits(self):
        if not self.limits:
            return
        # shape should collide if it hits the boundaries of window
        if self.rect.left < 0 or self.rect.right > self.limits[0]:
            self.speedx *= -1
        #  top limit is set to 50 because there is a top bar
        if self.rect.top < 50 or self.rect.bottom > self.limits[1]:
            self.speedy *= -1
