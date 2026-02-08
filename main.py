import sys
import pygame
import config

from entities.player.base import Player
from factories.powerup_factory import PowerUpFactory

# =============================================
# DEBUG FOOTER
# =============================================
def draw_debug_footer(surface, player, powerups, font):

    BOARD_WIDTH = surface.get_width()
    BOARD_HEIGHT = surface.get_height()
    FOOTER_HEIGHT = 60

    pygame.draw.rect(surface, (30, 30, 30), (0, BOARD_HEIGHT - FOOTER_HEIGHT, BOARD_WIDTH, FOOTER_HEIGHT))

    effects_texts = []
    for e in player.effect_manager.active_effects:
        remaining = round(e.remaining_time, 1)
        effects_texts.append(f"{type(e).__name__} ({remaining}s)")
    effects_line = "Active Effects: " + (", ".join(effects_texts) if effects_texts else "None")
    text_surface = font.render(effects_line, True, (255, 255, 255))
    surface.blit(text_surface, (10, BOARD_HEIGHT - FOOTER_HEIGHT + 5))

    # Statystyki PowerUpów na planszy
    stats = {}
    for p in powerups:
        name = type(p).__name__
        stats[name] = stats.get(name, 0) + 1
    stats_line = "PowerUps on board: " + (", ".join([f"{k}: {v}" for k,v in stats.items()]) if stats else "None")
    stats_surface = font.render(stats_line, True, (200, 200, 200))
    surface.blit(stats_surface, (10, BOARD_HEIGHT - FOOTER_HEIGHT + 30))

# =============================================
# MAIN
# =============================================
def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 20)

    screen = pygame.display.set_mode(
        (config.BOARD_WIDTH, config.BOARD_HEIGHT)
    )
    pygame.display.set_caption("Class-Driven Game")

    clock = pygame.time.Clock()
    running = True

    # --- PLAYER ---
    player = Player()

    # --- POWERUPS ---
    powerups = []

    SPAWN_INTERVAL = 1.0  # Power Up interval
    spawn_timer = 0.0

    # --- GAME LOOP ---
    while running:
        dt = clock.tick(config.FPS) / 1000.0
        spawn_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- UPDATE ---
        player.update(dt)

        # spawn PowerUp
        if spawn_timer >= SPAWN_INTERVAL:
            new_powerup = PowerUpFactory.create_random()
            powerups.append(new_powerup)
            spawn_timer = 0.0

        # update PowerUpów
        for powerup in powerups[:]:
            powerup.update(dt)
            if player.check_collision(powerup) and powerup.active:
                powerup.apply(player)

        # usuń zebrane lub wygasłe PowerUpy
        powerups = [p for p in powerups if p.active]

        # --- DRAW ---
        screen.fill(config.BACKGROUND_COLOR)
        player.draw(screen)
        for powerup in powerups:
            powerup.draw(screen)

        draw_debug_footer(screen, player, powerups, font)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
