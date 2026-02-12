from abc import ABC, abstractmethod
from typing import Optional

class Effect(ABC):
    key: Optional[str] = None
    removes: list[str] = []

    def __init__(self, duration: float, value: float):
        self.duration = duration
        self.remaining_time = duration
        self.value = value

    @abstractmethod
    def on_apply(self, player):
        pass

    @abstractmethod
    def on_update(self, player, dt: float):
        pass

    @abstractmethod
    def on_expire(self, player):
        pass

    def refresh(self):
        self.remaining_time = self.duration