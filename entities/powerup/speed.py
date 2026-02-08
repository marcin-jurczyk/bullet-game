from effects.slow import SlowEffect
from entities.powerup.powerup import PowerUp
from effects.speed import SpeedEffect
from config import POWERUP_COLOR_POSITIVE


class SpeedPowerUp(PowerUp):
    def __init__(self, position, color=POWERUP_COLOR_POSITIVE):
        super().__init__(position, color=color)

    def apply(self, player):
        player.remove_effect(SlowEffect)
        player.add_effect(SpeedEffect())
        self.expire()