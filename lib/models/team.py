from models.__init__ import CURSOR, CONN
from models.game import Game

class Team:

    all = {}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Team(id={self.id}, name={self.name})"

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
    
    @classmethod
    def instance_from_row(cls, row):
        team = cls(row[1])
        team.id = row[0]
        cls.all[team.id] = team
        return team

    @classmethod
    def find_by_id(cls,id):
        sql = """
        SELECT * FROM teams
        WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_row(row)
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
        SELECT * FROM teams
        WHERE name LIKE ?
        """
        rows = CURSOR.execute(sql, (f"%{name}%",)).fetchall()
        return [cls.instance_from_row(row) for row in rows]
    
    @classmethod
    def teams_at_tournament(cls, tournament_id):
        games = Game.games_by_tournament(tournament_id)
        teams = []
        for game in games:
            if game.home_team not in teams:
                teams.append(game.home_team)
            if game.away_team not in teams:
                teams.append(game.away_team)
        return [cls.find_by_id(team) for team in teams]

    @classmethod
    def display_all_teams(cls):
        sql = """
        SELECT * 
        FROM teams
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_row(row) for row in rows]


    def save(self):
        if self.id and type(self).find_by_id(self.id):
            sql = """
            UPDATE teams
            SET name = ?
            WHERE ID = ?
            """
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()
        else:
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