import pygame

class Entity:
    def __init__(self, position, size, color):
        self.position = pygame.math.Vector2(position)
        self.size = size
        self.color = color
        self.destroyed = False

    def update(self, dt: float):
        pass

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, self.color, self.position, self.size)
    
    def check_collision(self, other: "Entity") -> bool:
        distance = self.position.distance_to(other.position)
        return distance <= self.size + other.size
    
    def on_collision(self, other: "Entity"):
        pass

    
    

                                   