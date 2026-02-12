from effects.base import Effect
from config import ENLARGE_OFFSET, ENLARGE_TIME


class EnlargeEffect(Effect):
    key = "enlarge"
    removes = ["shrink"]

    def __init__(self):
        super().__init__(duration=ENLARGE_TIME, value=ENLARGE_OFFSET)

    def on_apply(self, player):
        player.size += self.value
    
    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.size -= self.value
