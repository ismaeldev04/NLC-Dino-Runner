import pygame.time
import random

from nlc_dino_runner.componers.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LIFES, BIRD
from nlc_dino_runner.componers.obstacles.bird import Birds


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.lifes = LIFES
        self.option_numbers = list(range(1, 10))
        self.game_speed = 15

    def update(self, game):
        if len(self.obstacles) == 0:
            if self.game_speed <= 50:
                self.game_speed += 1
            random.shuffle(self.option_numbers)
            if self.option_numbers[0] <= 6:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Birds(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles, self.game_speed)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif self.lifes > 1:
                    self.lifes -= 1
                    self.obstacles.remove(obstacle)
                else:
                    pygame.mixer.music.load("dead_sound.wav")
                    pygame.mixer.music.play(1)
                    pygame.mixer.music.set_volume(0.5)
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    self.lifes = LIFES
                    self.game_speed = 15
                    break

            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

