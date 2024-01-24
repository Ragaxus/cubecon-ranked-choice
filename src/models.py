from typing import List, Set
import uuid

class PlayerID:
    def __init__(self, player_id: uuid.UUID = uuid.uuid4()):
        self.id = player_id

class CubeID:
    def __init__(self, cube_id: uuid.UUID = uuid.uuid4()):
        self.id = cube_id

class PlayerRanking:
    def __init__(self, player_id: 'PlayerID', ranked_cubes: List['CubeID'], vetoed_cubes: Set['CubeID'], avoid_played_cubes: bool):
        self.player_id = player_id
        self.ranked_cubes = ranked_cubes
        self.vetoed_cubes = vetoed_cubes
        self.avoid_played_cubes = avoid_played_cubes

class CubeAssignment:
    def __init__(self, cube_id: 'CubeID', players: List['PlayerID']):
        self.cube_id = cube_id
        self.players = players

class Player:
    def __init__(self, name: str, player_id: 'PlayerID' = PlayerID(), history: List['RankPlacement'] = []):
        self.name = name
        self.id = player_id
        self.history = history

class RankPlacement:
    def __init__(self, ranked_cubes_count: int, placed_cube_index: int, placed_cube: 'CubeID'):
        self.ranked_cubes_count = ranked_cubes_count
        self.placed_cube_index = placed_cube_index
        self.placed_cube = placed_cube

class Cube:
    def __init__(self, name: str, cube_id: 'CubeID' = CubeID()):
        self.id = cube_id
        self.name = name
