import sys
import pygame
import config

from entities.player.player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (config.BOARD_WIDTH, config.BOARD_HEIGHT)
    )
    pygame.display.set_caption("Class-Driven Game")

    clock = pygame.time.Clock()
    running = True

    player = Player()

    while running:
        dt = clock.tick(config.FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- UPDATE ---
        player.update(dt)

        # --- DRAW ---
        screen.fill(config.BACKGROUND_COLOR)
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
