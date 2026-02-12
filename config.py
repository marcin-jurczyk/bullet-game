# ==================================================
# BOARD / GAME
# ==================================================
BOARD_WIDTH = 1280
BOARD_HEIGHT = 720
BACKGROUND_COLOR = (20, 20, 20)

FPS = 60

# ==================================================
# SCORE
# ==================================================
SCORE_PER_SECOND = 100

# ==================================================
# PLAYER
# ==================================================
PLAYER_START_SIZE = 15
PLAYER_MIN_SIZE = 8
PLAYER_START_HEALTH = 100
PLAYER_START_SPEED = 250
PLAYER_MIN_SPEED = 50
PLAYER_MAX_SPEED = 600
PLAYER_COLOR = (255, 255, 255)

# Range (px) for bullet target offset
PLAYER_OFFSET_RANGE = 30

# ==================================================
# BULLET – GENERAL
# ==================================================
BULLET_TARGET_PLAYER_CHANCE = 0.5
BULLET_TURN_RATE = 0.1
BULLET_SPAWN_INTERVAL = 0.2

# ==================================================
# NORMAL BULLET
# ==================================================
NORMAL_BULLET_SIZE = 8
NORMAL_BULLET_SPEED = 300
NORMAL_BULLET_DAMAGE = 0.20
NORMAL_BULLET_TRAIL_LENGTH = 20
NORMAL_BULLET_COLOR = (255, 255, 200)

# ==================================================
# LIGHT BULLET
# ==================================================
LIGHT_BULLET_SIZE = 6
LIGHT_BULLET_SPEED = 380
LIGHT_BULLET_DAMAGE = 0.10
LIGHT_BULLET_TRAIL_LENGTH = 10
LIGHT_BULLET_COLOR = (180, 120, 255)

# ==================================================
# HARD BULLET
# ==================================================
HARD_BULLET_SIZE = 12
HARD_BULLET_SPEED = 220
HARD_BULLET_DAMAGE = 0.30
HARD_BULLET_TRAIL_LENGTH = 35
HARD_BULLET_COLOR = (255, 80, 80)

# ==================================================
# ENLARGE BULLET
# ==================================================
ENLARGE_BULLET_SIZE = 8
ENLARGE_BULLET_SPEED = 300
ENLARGE_BULLET_DAMAGE = 0.10
ENLARGE_BULLET_TRAIL_LENGTH = 20
ENLARGE_BULLET_COLOR = (255, 220, 0)

# ==================================================
# SLOW BULLET
# ==================================================
SLOW_BULLET_SIZE = 10
SLOW_BULLET_SPEED = 250
SLOW_BULLET_DAMAGE = 0.10
SLOW_BULLET_TRAIL_LENGTH = 20
SLOW_BULLET_COLOR = (80, 255, 120)

# ==================================================
# EFFECTS – ENLARGE
# ==================================================
ENLARGE_OFFSET = 4
ENLARGE_TIME = 6.0
MAX_ENLARGE_EFFECTS = 3

# ==================================================
# EFFECTS – SLOW
# ==================================================
DECREASE_SPEED_VALUE = 100
DECREASE_SPEED_TIME = 5.0
MAX_DECREASE_SPEED_EFFECTS = 2

# ==================================================
# EFFECTS – SPEED (POWER UP)
# ==================================================
SPEED_POWERUP_VALUE = 300
SPEED_POWERUP_TIME = 5.0

# ==================================================
# EFFECTS – SHIELD
# ==================================================
SHIELD_RADIUS_OFFSET = 30
SHIELD_POWERUP_TIME = 6.0

# ==================================================
# EFFECTS – SHRINK
# ==================================================
SHRINK_POWERUP_SIZE = 5
SHRINK_POWERUP_TIME = 6.0

# ==================================================
# POWER UPS – GENERAL
# ==================================================
HEALTH_POWERUP_VALUE = 25
POWERUP_LIFETIME = 15.0
POWERUP_SIZE = 25
POWERUP_COLOR_POSITIVE = (0,255,0)
POWERUP_COLOR_NEGATIVE = (255,0,0)
POWERUP_SPAWN_INTERVAL = 3.0