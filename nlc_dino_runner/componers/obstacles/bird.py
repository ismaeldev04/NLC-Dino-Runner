from nlc_dino_runner.utils.constants import BIRD
from nlc_dino_runner.componers.obstacles.obstacle import Obstacle


class Birds(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.image_birds = BIRD[0]
        super().__init__(image, self.type)
        self.rect.y = 280
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0

        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1