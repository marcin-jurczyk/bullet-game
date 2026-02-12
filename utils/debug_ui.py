import pygame

# =========================
# PANEL CONFIG
# =========================
DEBUG_PANEL_WIDTH = 300
DEBUG_PANEL_HEIGHT = 400           # fixed height
MARGIN = 10                        # margin from right and top
RADIUS = 10                        # corner radius
DEBUG_BG_COLOR = (0, 0, 0, 100)   # black with alpha 180
HEADER_COLOR = (0, 255, 255)       # cyan
KEY_COLOR = (255, 255, 0)          # yellow
VALUE_COLOR = (255, 255, 255)      # white
PADDING_X = 12
PADDING_Y = 12
LINE_HEIGHT = 16                    # very small font spacing
SECTION_SPACING = 110               # vertical spacing between sections

# =========================
# FONT
# =========================
def load_debug_font(size=14):
    return pygame.font.SysFont("Menlo", size)

# =========================
# DRAW FUNCTION
# =========================
def draw_debug_panel(surface, player, powerups, bullets, font):
    width = surface.get_width()
    height = surface.get_height()
    x = width - DEBUG_PANEL_WIDTH - MARGIN
    y_offset = MARGIN

    # -------------------------
    # BACKGROUND PANEL WITH ROUNDED CORNERS
    # -------------------------
    panel_surf = pygame.Surface((DEBUG_PANEL_WIDTH, DEBUG_PANEL_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(panel_surf, DEBUG_BG_COLOR,
                     (0, 0, DEBUG_PANEL_WIDTH, DEBUG_PANEL_HEIGHT),
                     border_radius=RADIUS)
    surface.blit(panel_surf, (x, y_offset))

    # -------------------------
    # HELPER: draw a line
    # -------------------------
    def draw_line(y, key, value="", bold=False):
        key_surf = font.render(key, True, KEY_COLOR)
        surface.blit(key_surf, (x + PADDING_X, y_offset + y))
        if value:
            value_surf = font.render(value, True, VALUE_COLOR)
            surface.blit(value_surf, (x + PADDING_X + 150, y_offset + y))

    # -------------------------
    # HELPER: draw header & divider
    # -------------------------
    def draw_header(y, text):
        header_surf = font.render(text, True, HEADER_COLOR)
        surface.blit(header_surf, (x + PADDING_X, y_offset + y))
        # divider line below
        pygame.draw.line(surface, HEADER_COLOR,
                         (x + PADDING_X, y_offset + y + LINE_HEIGHT),
                         (x + DEBUG_PANEL_WIDTH - PADDING_X, y_offset + y + LINE_HEIGHT))
        return y + LINE_HEIGHT + 6  # small spacing

    # -------------------------
    # PLAYER SECTION
    # -------------------------
    y = 0
    y = draw_header(y, "PLAYER")
    draw_line(y, "HP:", f"{round(player.health,1)}")
    y += LINE_HEIGHT
    draw_line(y, "Speed:", f"{round(player.speed,2)}")
    y += LINE_HEIGHT

    effects = player.effect_manager.active_effects
    draw_line(y, "Effects:")
    y += LINE_HEIGHT
    if effects:
        for e in effects:
            stacks = f"x{e.stacks}" if getattr(e, "stacks",1) > 1 else ""
            draw_line(y, f"{type(e).__name__}{stacks}", f"{round(e.remaining_time,1)}s")
            y += LINE_HEIGHT
    else:
        draw_line(y, "", "None")
        y += LINE_HEIGHT

    # -------------------------
    # POWERUPS SECTION
    # -------------------------
    y = SECTION_SPACING
    y = draw_header(y, "POWERUPS")
    powerup_stats = {}
    for p in powerups:
        name = type(p).__name__
        powerup_stats[name] = powerup_stats.get(name,0) + 1

    if powerup_stats:
        for name,count in powerup_stats.items():
            draw_line(y, name, str(count))
            y += LINE_HEIGHT
    else:
        draw_line(y, "", "None")
        y += LINE_HEIGHT

    # -------------------------
    # BULLETS SECTION
    # -------------------------
    y = SECTION_SPACING * 2
    y = draw_header(y, "BULLETS")
    bullet_stats = {}
    total_damage = 0.0
    total_speed = 0.0

    for b in bullets:
        name = type(b).__name__
        bullet_stats[name] = bullet_stats.get(name,0)+1
        total_damage += getattr(b, "damage",0)
        total_speed += getattr(b, "speed",0)

    bullet_count = len(bullets)

    if bullet_stats:
        for name,count in bullet_stats.items():
            draw_line(y, name, str(count))
            y += LINE_HEIGHT
        if bullet_count:
            draw_line(y, "Avg dmg:", f"{round(total_damage / bullet_count,2)}")
            y += LINE_HEIGHT
            draw_line(y, "Avg speed:", f"{round(total_speed / bullet_count,1)}")
            y += LINE_HEIGHT
    else:
        draw_line(y, "", "None")
