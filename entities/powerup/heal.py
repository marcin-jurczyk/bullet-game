from config import HEAL_POWERUP_VALUE, POWERUP_COLOR_POSITIVE
from effects.shield import ShieldEffect
from entities.powerup.powerup import PowerUp


class HealPowerUp(PowerUp):
    ICON_PATH = 'assets/icons/heal.png'

    def __init__(self, position, color=POWERUP_COLOR_POSITIVE):
        super().__init__(position, color=color)

    def apply(self, player):
        player.health += HEAL_POWERUP_VALUE
        self.expire()

