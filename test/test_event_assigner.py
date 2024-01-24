import json
import unittest
from uuid import UUID
from test.services import *


class TestEventAssigner(unittest.TestCase):
    def setUp(self):
        cubeA = Cube("CubeA", CubeID(UUID('ed7161fa-03cd-4902-aabb-934f91ff0592')))
        cubeB = Cube("CubeB", CubeID(UUID('5368edad-f456-4d6f-b462-08c913d2c99e')))
        self.cubes = [cubeA, cubeB]
        self.player_rankings_data = []
        # Eight people who ranked A
        for i in range(9):
            self.player_rankings_data.append(
            PlayerRanking(
                player_id=PlayerID(),
                ranked_cubes=[cubeA.id],
                vetoed_cubes=set(),
                avoid_played_cubes=True
            ))
        # One person who vetoed B
        self.veto_person = uuid.uuid4()
        self.player_rankings_data.append(
        PlayerRanking(
            player_id=PlayerID(self.veto_person),
            ranked_cubes=[],
            vetoed_cubes=set([cubeB.id]),
            avoid_played_cubes=True
            ))
        # A few other people
        for i in range(6):
           self.player_rankings_data.append(PlayerRanking(
            player_id=PlayerID(),
            ranked_cubes=[],
            vetoed_cubes=set(),
            avoid_played_cubes=True
            )) 

    def test_generate_assignments(self):

        event_assigner = ConcreteEventAssigner()
        assignments = event_assigner.generate_assignments(
            self.player_rankings_data, self.cubes)

        self.assertEqual(len(assignments[self.cubes[0].id].players), 8,
                         "Didn't assign enough players to Cube A")
        cube_b_assignments = assignments[self.cubes[1].id]
        self.assertNotIn(self.veto_person, [player.id for player in cube_b_assignments.players],
                         "Put player #9 in Cube B even though they vetoed it")


if __name__ == '__main__':
    unittest.main()
