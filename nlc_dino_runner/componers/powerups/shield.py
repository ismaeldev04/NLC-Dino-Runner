from nlc_dino_runner.componers.powerups.power_up import PowerUp
from nlc_dino_runner.utils.constants import SHIELD


class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = 'shield'
        super().__init__(self.image, self.type)
