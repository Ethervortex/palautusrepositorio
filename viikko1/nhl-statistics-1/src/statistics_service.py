from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by_points(player):
    return player.points


class StatisticsService:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, by_what=None):
        if by_what == SortBy.POINTS:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=lambda player: player.points)
        elif by_what == SortBy.GOALS:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=lambda player: player.goals)
        elif by_what == SortBy.ASSISTS:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=lambda player: player.assists)
        else:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_points)

        return sorted_players[:how_many]
        """
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
        """
