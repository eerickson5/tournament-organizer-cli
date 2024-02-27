from models.__init__ import CURSOR, CONN
from models.game import Game

class Team:

    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Team instances """
        sql = """
            CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT
        """
        CURSOR.execute(sql)
        CONN.commit()