from nlc_dino_runner.utils.constants import HEART
from pygame.sprite import Sprite


class Life(Sprite):
    def __init__(self):
        self.life = []
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset_life(self):
        self.life = []
