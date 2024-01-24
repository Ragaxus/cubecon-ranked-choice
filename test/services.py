from typing import List

from src.interfaces import EventAssigner
from src.models import *


class ConcreteEventAssigner(EventAssigner):
    def generate_assignments(self, player_rankings: List['PlayerRanking'], cubes: List['Cube']) -> dict[uuid.UUID, 'CubeAssignment']:
        assignments = {cube_id: CubeAssignment(cube_id, []) for cube_id in [cube.id for cube in cubes]}
        for ranking in player_rankings:
            found_cube_id = None
            for curr_cube_id in ranking.ranked_cubes:
                if len(assignments[curr_cube_id].players) < 8:
                    found_cube_id = curr_cube_id
                    break
            if found_cube_id is None:
                found_cube_id = next(cube.id for cube in cubes if len(assignments[cube.id].players) < 8)
            assignments[found_cube_id].players.append(ranking.player_id)

        return assignments
