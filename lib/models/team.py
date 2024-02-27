from models.__init__ import CURSOR, CONN
from models.game import Game

class Team:

    all = {}

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS teams
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO teams(name)
        VALUES (?)
        """
        CURSOR.execute(sql, (self.name))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self