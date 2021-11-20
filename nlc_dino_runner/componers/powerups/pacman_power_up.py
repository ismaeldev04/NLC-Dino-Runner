from nlc_dino_runner.componers.powerups.power_up import PowerUp
from nlc_dino_runner.utils.constants import PACMAN_POWER_UP


class Pacman(PowerUp):
    def __init__(self):
        self.image = PACMAN_POWER_UP
        self.type = "pacman"
        super().__init__(self.image, self.type)
