from entities.powerup.powerup import PowerUp
from effects.speed import SpeedEffect
from config import POWERUP_COLOR_POSITIVE


class SpeedPowerUp(PowerUp):
    ICON_PATH = 'assets/icons/speed.png'

    def __init__(self, position, color=POWERUP_COLOR_POSITIVE):
        super().__init__(position, color=color)

    def apply(self, player):
        player.add_effect(SpeedEffect())
        self.expire()