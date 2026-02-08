from effects.base import Effect
from config import SPEED_POWERUP_TIME, SPEED_POWERUP_VALUE, PLAYER_MAX_SPEED

class SpeedEffect(Effect):
    def __init__(self):
        super().__init__(duration=SPEED_POWERUP_TIME, value=SPEED_POWERUP_VALUE)
        self.actual_increase = 0

    def on_apply(self, player):
        self.actual_increase = min(self.value, PLAYER_MAX_SPEED - player.speed)
        player.speed += self.actual_increase

    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.speed -= self.actual_increase
