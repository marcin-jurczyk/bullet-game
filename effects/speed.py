from effects.base import Effect
from config import SPEED_POWERUP_TIME, SPEED_POWERUP_VALUE, PLAYER_MAX_SPEED


class SpeedEffect(Effect):
    key = "speed"
    removes = ["slow"]

    def __init__(self):
        super().__init__(duration=SPEED_POWERUP_TIME, value=SPEED_POWERUP_VALUE)

    def on_apply(self, player):
        player.speed += self.value

    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.speed -= self.value
