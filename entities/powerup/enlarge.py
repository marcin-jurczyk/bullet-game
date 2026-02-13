from effects.enlarge import EnlargeEffect
from effects.shrink import ShrinkEffect
from entities.powerup.powerup import PowerUp


class EnlargePowerUp(PowerUp):
    ICON_PATH = 'assets/icons/enlarge.png'

    def __init__(self, position, color=(0, 255, 255)):
        super().__init__(position, color=color)

    def apply(self, player):
        # player.remove_effect(ShrinkEffect)
        player.add_effect(EnlargeEffect())
        self.expire()

