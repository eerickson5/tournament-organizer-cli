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
    wreck = Team.create_team("Tech Wreck")
    ozone = Team.create_team("Ozone")
    other = Team.create_team("Wreck")
    tournament = Tournament.create_tournament("Round Robin")
    scrimmage = Game.create_game(magma.id, wreck.id, tournament.id)
    scrimmage.add_scores(15, 12)
    #create sample data
    

seed_database()
print("Database seeded.")
print(Team.find_by_name("Wreck"))