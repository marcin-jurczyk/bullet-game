from effects.base import Effect
from config import SHRINK_POWERUP_TIME, SHRINK_POWERUP_SIZE

class ShrinkEffect(Effect):
    def __init__(self):
        super().__init__(duration=SHRINK_POWERUP_TIME, value=SHRINK_POWERUP_SIZE)

    def on_apply(self, player):
        player.size -= self.value
    
    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.size += self.value
