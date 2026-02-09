import pygame

FOOTER_HEIGHT = 60
BG_COLOR = (30, 30, 30)

PLAYER_COLOR = (255, 255, 255)
POWERUP_COLOR = (200, 200, 200)
BULLET_COLOR = (255, 180, 180)


def draw_debug_footer(surface, player, powerups, bullets, font):
    width = surface.get_width()
    height = surface.get_height()
    padding = 10

    # =========================
    # BACKGROUND
    # =========================
    pygame.draw.rect(
        surface,
        BG_COLOR,
        (0, height - FOOTER_HEIGHT, width, FOOTER_HEIGHT),
    )

    # =========================
    # LEFT – PLAYER
    # =========================
    effects_texts = [
        f"{type(e).__name__}({round(e.remaining_time,1)}s)"
        for e in player.effect_manager.active_effects
    ]

    player_lines = [
        f"HP: {round(player.health,1)}",
        f"Speed: {round(player.speed,1)}",
        f"Effects: {', '.join(effects_texts) if effects_texts else 'None'}",
    ]

    for i, line in enumerate(player_lines):
        text = font.render(line, True, PLAYER_COLOR)
        surface.blit(
            text,
            (padding, height - FOOTER_HEIGHT + 5 + i * 18),
        )

    # =========================
    # CENTER – POWERUPS (JAK WCZEŚNIEJ)
    # =========================
    stats = {}
    for p in powerups:
        name = type(p).__name__
        stats[name] = stats.get(name, 0) + 1

    powerups_line = "PowerUps on board: " + (
        ", ".join(f"{k}: {v}" for k, v in stats.items()) if stats else "None"
    )

    text = font.render(powerups_line, True, POWERUP_COLOR)
    rect = text.get_rect(center=(width // 2, height - FOOTER_HEIGHT + 15))
    surface.blit(text, rect)

    # =========================
    # RIGHT – BULLETS (ROZSZERZONE)
    # =========================
    bullet_stats = {}
    total_damage = 0.0
    total_speed = 0.0

    for b in bullets:
        name = type(b).__name__
        bullet_stats[name] = bullet_stats.get(name, 0) + 1
        total_damage += getattr(b, "damage", 0)
        total_speed += getattr(b, "speed", 0)

    bullet_count = len(bullets)
    avg_damage = round(total_damage / bullet_count, 2) if bullet_count else 0
    avg_speed = round(total_speed / bullet_count, 1) if bullet_count else 0

    bullets_line_1 = "Bullets: " + (
        ", ".join(f"{k}:{v}" for k, v in bullet_stats.items())
        if bullet_stats
        else "None"
    )

    bullets_line_2 = f"Avg dmg: {avg_damage} | Avg speed: {avg_speed}"

    text1 = font.render(bullets_line_1, True, BULLET_COLOR)
    text2 = font.render(bullets_line_2, True, BULLET_COLOR)

    surface.blit(
        text1,
        text1.get_rect(
            right=width - padding,
            top=height - FOOTER_HEIGHT + 5,
        ),
    )
    surface.blit(
        text2,
        text2.get_rect(
            right=width - padding,
            top=height - FOOTER_HEIGHT + 28,
        ),
    )
