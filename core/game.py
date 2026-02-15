import pygame
import config
from core.world import World


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(
            (config.BOARD_WIDTH, config.BOARD_HEIGHT)
        )
        pygame.display.set_caption("Class-Driven Game")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        self.world = World()

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(config.FPS) / 1000.0
            self.handle_events()
            self.world.update(dt)
            self.world.draw(self.screen, self.font)
            pygame.display.flip()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
