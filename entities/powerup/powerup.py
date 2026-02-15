from pygame import Surface, Vector2, gfxdraw
from config import POWERUP_SIZE, POWERUP_LIFETIME
from core.resource_manager import ResourceManager
from entities.entity import Entity
from typing import Optional # --- python 3.9.6 ---
import pygame

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

    def draw_soft_glow(self, surface, center, radius, color):
        glow = pygame.Surface((radius*4, radius*4), pygame.SRCALPHA)
        pygame.draw.circle(glow, (*color, 60), (radius*2, radius*2), radius, 3)

        for scale in (1.3, 1.6, 2.0):
            g = pygame.transform.smoothscale(
                glow,
                (int(glow.get_width()*scale), int(glow.get_height()*scale))
            )
            surface.blit(g, g.get_rect(center=center), special_flags=pygame.BLEND_RGBA_ADD)


    def draw(self, surface: pygame.Surface):
        x, y = int(self.position.x), int(self.position.y)

        # --- glow ---
        # glow_surf = ResourceManager.glow_circle((*self.color[:3], 50), self.size)
        # surface.blit(glow_surf, glow_surf.get_rect(center=(x, y)), special_flags=pygame.BLEND_RGBA_ADD)

        # --- main circle ---
        gfxdraw.aacircle(surface, x, y, self.size, self.color)

        # --- icon ---
        if self.ICON_PATH is not None:
            icon_surf = ResourceManager.scaled_image(self.ICON_PATH, self.size*2)
            surface.blit(icon_surf, icon_surf.get_rect(center=(x, y)))


    def apply(self, player):
        pass

    def expire(self):
         self.active = False