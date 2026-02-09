import pygame
from typing import Dict, Tuple

class ResourceManager:
    _images: Dict[str, pygame.Surface] = {}  # original images
    _scaled_images: Dict[Tuple[str, int], pygame.Surface] = {}  # scaled cache

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
