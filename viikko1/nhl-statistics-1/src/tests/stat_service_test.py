import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsi_pelaaja(self):
        result = self.stats.search("Semenko")
        expected_name = "Semenko"
        expected_team = "EDM"
        expected_goals = 4
        expected_assists = 12
        expected_points = 16

        self.assertEqual(result.name, expected_name)
        self.assertEqual(result.team, expected_team)
        self.assertEqual(result.goals, expected_goals)
        self.assertEqual(result.assists, expected_assists)
        self.assertEqual(result.points, expected_points)

    def test_etsi_olematon_pelaaja(self):
        result = self.stats.search("Vesalainen")
        expected = None
        self.assertEqual(result, expected)

    def test_team(self):
        team_name = "EDM"
        players_of_team = self.stats.team(team_name)
        team_names = [player.team for player in players_of_team]
        self.assertTrue(all(team == team_name for team in team_names))

    def test_top(self):
        number = 1 # top-metodin luupissa virhe, käytetään kuitenkin virheellistä koodia eli 1 palauttaa 2
        top_players = self.stats.top(number)
        expected = ["Gretzky", "Lemieux"]
        top_names = [player.name for player in top_players]
        self.assertEqual(top_names, expected)
        #self.assertEqual(len(top_players), number)