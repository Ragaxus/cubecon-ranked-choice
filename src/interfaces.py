from abc import ABC, abstractmethod
from typing import List

from src.models import *


class EventAssigner(ABC):
    @abstractmethod
    def generate_assignments(self, player_rankings: List['PlayerRanking'], cubes: List['Cube']) -> dict[uuid.UUID,'CubeAssignment']:
        pass
