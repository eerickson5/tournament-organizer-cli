#!/usr/bin/env python3
from models.team import Team
from models.game import Game
from models.tournament import Tournament
from models.__init__ import CONN, CURSOR

def seed_database():
    Team.drop_table()
    Team.create_table()
    Game.drop_table()
    Game.create_table()
    Tournament.drop_table()
    Tournament.create_table()

    magma = Team.create_team("Magma")
    ozone = Team.create_team("Ozone")
    emory = Team.create_team("Emory Luna")
    wreck = Team.create_team("Tech Wreck")

    tournament = Tournament.create_tournament("Round Robin")

    scrimmage = Game.create_game(magma.id, ozone.id)
    scrimmage.add_scores(15, 12)
    scrimmage.add_to_tournament(tournament.id)

    derby = Game.create_game(wreck.id, emory.id)
    derby.add_scores(15, 3)
    derby.add_to_tournament(tournament.id)

    my_teams_scrim = Game.create_game(magma.id, wreck.id)
    my_teams_scrim.add_scores(14, 12)
    my_teams_scrim.add_to_tournament(tournament.id)

def current_test():
    
    print(Game.games_won_by_team(1))
    

seed_database()
print("Database seeded.")
current_test()