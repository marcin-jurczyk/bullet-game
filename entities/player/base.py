import pygame
import config

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

        self.is_dead = False

    def update(self, dt: float):
        self.handle_input(dt)
        self.clamp_to_board()

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
        self.position.x = max(
            self.size,
            min(config.BOARD_WIDTH - self.size, self.position.x)
        )
        self.position.y = max(
            self.size,
            min(config.BOARD_HEIGHT - self.size, self.position.y)
        )