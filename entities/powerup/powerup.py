from pygame import Surface, Vector2, gfxdraw
from config import POWERUP_SIZE, POWERUP_LIFETIME
from core.resource_manager import ResourceManager
from entities.entity import Entity
from typing import Optional # --- python 3.9.6 ---


class PowerUp(Entity):
    ICON_PATH: Optional[str] = None

    def __init__(
        self,
        position: Vector2,
        size: int = POWERUP_SIZE,
        color=(255, 255, 255),
        lifetime: float = POWERUP_LIFETIME,
    ):
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

        if self.ICON_PATH is not None:
            icon_surf = ResourceManager.scaled_image(self.ICON_PATH, self.size * 2)
            icon_rect = icon_surf.get_rect(center=(x, y))
            surface.blit(icon_surf, icon_rect)

    def apply(self, player):
        pass

    def expire(self):
         self.active = False