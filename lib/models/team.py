from models.__init__ import CURSOR, CONN
from models.game import Game

class Team:

    all = {}

    def __init__(self, name):
        self.name = name

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

    @classmethod
    def create_team(cls, name):
        team = cls(name)
        team.save()
        return team

    def save(self):
        sql = """
        INSERT INTO teams (name)
        VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete_team(self):
        sql = """
        DELETE FROM teams
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            raise TypeError("Team name must be a nonempty string.")