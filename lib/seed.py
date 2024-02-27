#!/usr/bin/env python3

from models.team import Team
from models.game import Game
from models.tournament import Tournament
from models.__init__ import CONN, CURSOR

def seed_database():
    #drop each table to clear it
    #create new tables
    #create sample data