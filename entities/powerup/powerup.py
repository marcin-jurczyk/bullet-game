from pygame import Surface, Vector2, gfxdraw
from config import POWERUP_SIZE, POWERUP_LIFETIME
from entities.entity import Entity


class PowerUp(Entity):
    def __init__(self, position: Vector2, size: int = POWERUP_SIZE, color=(255, 255, 255), lifetime: float = POWERUP_LIFETIME):
        super().__init__(position, size, color)
        self.lifetime = lifetime
        self.active = True
        self.timer = 0.0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.lifetime:
            self.expire()
    
    def draw(self, surface: Surface):
        x, y = int(self.position.x), int(self.position.y)
        gfxdraw.aacircle(surface, x, y, self.size, self.color)
    
    def apply(self, player):
        pass

    def expire(self):
         self.active = False