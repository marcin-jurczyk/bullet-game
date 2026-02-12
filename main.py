import sys
import pygame
import config

from entities.player.base import Player
from factories.powerup_factory import PowerUpFactory
from factories.bullet_factory import BulletFactory
from utils.debug_ui import draw_debug_panel


def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 18)

    screen = pygame.display.set_mode(
        (config.BOARD_WIDTH, config.BOARD_HEIGHT)
    )
    pygame.display.set_caption("Class-Driven Game")

    clock = pygame.time.Clock()
    running = True

    # =========================
    # GAME OBJECTS
    # =========================
    player = Player()
    bullets = []
    powerups = []

    # =========================
    # TIMERS
    # =========================
    powerup_spawn_timer = 0.0
    bullet_spawn_timer = 0.0

    # =========================
    # GAME LOOP
    # =========================
    while running:
        dt = clock.tick(config.FPS) / 1000.0
        powerup_spawn_timer += dt
        bullet_spawn_timer += dt

        # ---------------------
        # EVENTS
        # ---------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ---------------------
        # UPDATE
        # ---------------------
        player.update(dt)

        # spawn PowerUps
        if powerup_spawn_timer >= config.POWERUP_SPAWN_INTERVAL:
            powerups.append(PowerUpFactory.create_random(player=player, existing_powerups=powerups))
            powerup_spawn_timer = 0.0

        # spawn Bullets
        if bullet_spawn_timer >= config.BULLET_SPAWN_INTERVAL:
            bullets.append(BulletFactory.create(player.position))
            bullet_spawn_timer = 0.0

        # update PowerUps
        for p in powerups[:]:
            p.update(dt)
            if p.active and player.check_collision(p):
                p.apply(player)

        powerups = [p for p in powerups if p.active]

        # update Bullets
        for b in bullets[:]:
            b.update(dt, player)
            if b.destroyed:
                bullets.remove(b)

        # ---------------------
        # DRAW
        # ---------------------
        screen.fill(config.BACKGROUND_COLOR)

        player.draw(screen)

        for p in powerups:
            p.draw(screen)

        for b in bullets:
            b.draw(screen)

        draw_debug_panel(screen, player, powerups, bullets, font)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
