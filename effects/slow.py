from effects.base import Effect
from config import DECREASE_SPEED_TIME, DECREASE_SPEED_VALUE, PLAYER_MIN_SPEED

class SlowEffect(Effect):
    def __init__(self):
        super().__init__(duration=DECREASE_SPEED_TIME, value=DECREASE_SPEED_VALUE)
        self.actual_reduction = 0

    def on_apply(self, player):
        self.actual_reduction = min(self.value, player.speed - PLAYER_MIN_SPEED)
        player.speed -= self.actual_reduction

    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.speed += self.actual_reduction
