import pygame
import config
from effects.effects_manager import EffectManager
from entities.entity import Entity


class Player(Entity):
    def __init__(self):
        start_position = pygame.math.Vector2(config.BOARD_WIDTH // 2, config.BOARD_HEIGHT // 2)

        super().__init__(
            position=start_position,
            size=config.PLAYER_START_SIZE,
            color=config.PLAYER_COLOR
        )

        self.health = config.PLAYER_START_HEALTH
        self.speed = config.PLAYER_START_SPEED
        self.has_shield = False
        self.effect_manager = EffectManager(self)
        self.is_dead = False
        self.points = 0

    def receive_points(self, amount: int):
        self.points += amount

    def add_effect(self, effect):
        self.effect_manager.add(effect)

    def remove_effect(self, effect_key: str):
        self.effect_manager.remove_by_key(effect_key)

    def draw(self, surface):
        super().draw(surface)
        self.effect_manager.draw(surface)

    def update(self, dt: float):
        self.handle_input(dt)
        self.clamp_to_board()
        self.effect_manager.update(dt)

    def handle_input(self, dt: float):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_RIGHT]:
            direction.x += 1
        if keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_DOWN]:
            direction.y += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()

        self.position += direction * self.speed * dt

    def clamp_to_board(self):
        min_x = float(self.size)
        max_x = float(config.BOARD_WIDTH - self.size)
        min_y = float(self.size)
        max_y = float(config.BOARD_HEIGHT - self.size)

        self.position.x = max(min_x, min(max_x, self.position.x))
        self.position.y = max(min_y, min(max_y, self.position.y))
