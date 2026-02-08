from config import ENLARGE_OFFSET, ENLARGE_TIME
from effects.base import Effect


class EnlargeEffect(Effect):
    def __init__(self):
        super().__init__(duration=ENLARGE_TIME, value=ENLARGE_OFFSET)

    def on_apply(self, player):
        player.size += self.value
    
    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.size -= self.value
