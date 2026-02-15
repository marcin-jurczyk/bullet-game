import config
from entities.player.base import Player
from factories.bullet_factory import BulletFactory
from factories.powerup_factory import PowerUpFactory
from factories.point_factory import PointFactory


class World:
    def __init__(self):
        self.player = Player()
        self.bullets = []
        self.powerups = []
        self.points = []

        self.bullet_timer = 0.0
        self.powerup_timer = 0.0
        self.point_timer = 0.0

    def update(self, dt: float):
        self.player.update(dt)

        self._spawn(dt)
        self._update_entities(dt)

    def _spawn(self, dt: float):
        self.bullet_timer += dt
        self.powerup_timer += dt
        self.point_timer += dt

        if self.bullet_timer >= config.BULLET_SPAWN_INTERVAL:
            self.bullets.append(
                BulletFactory.create(self.player.position)
            )
            self.bullet_timer = 0.0

        if self.powerup_timer >= config.POWERUP_SPAWN_INTERVAL:
            self.powerups.append(
                PowerUpFactory.create_random(
                    player=self.player,
                    existing_powerups=self.powerups
                )
            )
            self.powerup_timer = 0.0

        if self.point_timer >= 0.05:
            point = PointFactory.create(existing_points=self.points)
            if point:
                self.points.append(point)
            self.point_timer = 0.0

    def _update_entities(self, dt: float):
        for b in self.bullets[:]:
            b.update(dt, self.player)
            if b.destroyed:
                self.bullets.remove(b)

        for p in self.powerups[:]:
            p.update(dt)
            if p.active and self.player.check_collision(p):
                p.apply(self.player)
        self.powerups = [p for p in self.powerups if p.active]

        for pt in self.points[:]:
            pt.update(dt)
            if self.player.check_collision(pt):
                pt.on_collision(self.player)
            if pt.destroyed:
                self.points.remove(pt)

    def draw(self, surface, font):
        surface.fill(config.BACKGROUND_COLOR)

        self.player.draw(surface)

        for pt in self.points:
            pt.draw(surface)

        for p in self.powerups:
            p.draw(surface)

        for b in self.bullets:
            b.draw(surface)

        self._draw_hud(surface, font)

    def _draw_hud(self, surface, font):
        lines = [
            f"Health: {self.player.health:.0f}",
            f"Points: {self.player.points}",
        ]

        y = 10
        for line in lines:
            label = font.render(line, True, (255, 255, 255))
            surface.blit(label, (10, y))
            y += font.get_height() + 4
