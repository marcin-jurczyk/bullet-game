class EffectManager:
    def __init__(self, player):
        self.player = player
        self.active_effects = []

    def add(self, effect):
        existing = next(
            (e for e in self.active_effects if isinstance(e, type(effect))),
            None,
        )

        if existing:
            existing.refresh()
        else:
            effect.on_apply(self.player)
            self.active_effects.append(effect)

    def remove_by_type(self, effect_type):
        remaining = []

        for effect in self.active_effects:
            if isinstance(effect, effect_type):
                effect.on_expire(self.player)
            else:
                remaining.append(effect)

        self.active_effects = remaining

    def update(self, dt: float):
        remaining = []

        for effect in self.active_effects:
            effect.remaining_time -= dt
            effect.on_update(self.player, dt)

            if effect.remaining_time <= 0:
                effect.on_expire(self.player)
            else:
                remaining.append(effect)

        self.active_effects = remaining