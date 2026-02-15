import pygame
from pygame import gfxdraw
from typing import Dict, Tuple

class ResourceManager:
    _images: Dict[str, pygame.Surface] = {}  # original images
    _scaled_images: Dict[Tuple[str, int], pygame.Surface] = {}  # scaled cache
    _glows: Dict[Tuple[Tuple[int,int,int,int], int], pygame.Surface] = {}  # glow cache

    @classmethod
    def image(cls, path: str) -> pygame.Surface:
        """Load the original image (full resolution)."""
        if path not in cls._images:
            surface = pygame.image.load(path)
            if pygame.display.get_init():
                surface = surface.convert_alpha()
            cls._images[path] = surface
        return cls._images[path]

    @classmethod
    def scaled_image(cls, path: str, size: int) -> pygame.Surface:
        """
        Return a surface scaled to (size x size) pixels.
        Caches scaled images per size to avoid rescaling each frame.
        """
        key = (path, size)
        scale = 0.6
        if key not in cls._scaled_images:
            original = cls.image(path)
            cls._scaled_images[key] = pygame.transform.smoothscale(original, (size*scale, size*scale))
        return cls._scaled_images[key]

    @classmethod
    def glow_circle(cls, color: Tuple[int,int,int,int], radius: int) -> pygame.Surface:
        """
        Return a pre-rendered glow Surface for a circle of a given radius and color.
        Caches the glow to avoid recalculating.
        """
        key = (color, radius)
        if key not in cls._glows:
            # Local surface for glow
            surface_size = radius*4
            glow_surf = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
            cx = cy = surface_size // 2

            # Outer and inner glow like your draw method
            outer_radius = radius + 12
            inner_radius = max(0, radius - 12)
            max_alpha = color[3] if len(color) == 4 else 50

            # Outer glow
            outer_steps = outer_radius - radius
            for i, r in enumerate(range(radius, outer_radius)):
                t = i / outer_steps
                alpha = int(max_alpha * (1 - t) ** 0.96)
                gfxdraw.aacircle(glow_surf, cx, cy, r, (*color[:3], alpha))

            # Inner glow
            inner_steps = radius - inner_radius
            for i, r in enumerate(range(radius, inner_radius, -1)):
                t = i / inner_steps
                alpha = int(max_alpha * (1 - t) ** 0.96)
                gfxdraw.aacircle(glow_surf, cx, cy, r, (*color[:3], alpha))

            cls._glows[key] = glow_surf
        return cls._glows[key]