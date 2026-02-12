from effects.enlarge import EnlargeEffect
from effects.shrink import ShrinkEffect
from entities.powerup.powerup import PowerUp


class ShrinkPowerUp(PowerUp):
    def __init__(self, position, color=(255, 255, 0)):
        super().__init__(position, color=color)

    def apply(self, player):
        # player.remove_effect(EnlargeEffect)
        player.add_effect(ShrinkEffect())
        self.expire()

