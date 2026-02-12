from effects.slow import SlowEffect
from entities.powerup.powerup import PowerUp
from config import POWERUP_COLOR_NEGATIVE


class SlowPowerUp(PowerUp):
    ICON_PATH = 'assets/icons/slow.png'

    def __init__(self, position, color=POWERUP_COLOR_NEGATIVE):
        super().__init__(position, color=color)

    def apply(self, player):
        player.add_effect(SlowEffect())
        self.expire()