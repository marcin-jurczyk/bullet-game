from config import POWERUP_COLOR_POSITIVE
from effects.shield import ShieldEffect
from entities.powerup.powerup import PowerUp


class ShieldPowerUp(PowerUp):
    ICON_PATH = 'assets/icons/shield.png'

    def __init__(self, position, color=POWERUP_COLOR_POSITIVE):
        super().__init__(position, color=color)

    def apply(self, player):
        player.add_effect(ShieldEffect())
        self.expire()

