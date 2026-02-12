from effects.base import Effect
from config import DECREASE_SPEED_TIME, DECREASE_SPEED_VALUE, PLAYER_MIN_SPEED


class SlowEffect(Effect):
    key = "slow"
    removes = ["speed"]

    def __init__(self):
        super().__init__(duration=DECREASE_SPEED_TIME, value=DECREASE_SPEED_VALUE)

    def on_apply(self, player):
        player.speed -= self.value

    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.speed += self.value
