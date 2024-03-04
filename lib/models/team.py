from models.__init__ import CURSOR, CONN


class Team:

    all = {}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # return f"Team(id={self.id}, name={self.name})"
        return f"\nTeam({self.id}) {self.name}\n"

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
        if rows:
            return [cls.instance_from_row(row) for row in rows]
        
    def games(self):
        from models.game import Game
        sql = """
        SELECT * FROM games
        WHERE home_team = ?
        OR away_team = ?
        """
        rows = CURSOR.execute(sql, (self.id, self.id)).fetchall()
        return[Game.instance_from_row(row) for row in rows]
    
    def games_won(self):
        games = self.games()
        games_won = []
        for game in games:
            if game.winner() == self.id:
                games_won.append(game)
        return games_won
    
    def home_games(self):
        from models.game import Game
        sql = """
        SELECT * FROM games
        WHERE home_team = ?
        """
        rows = CURSOR.execute(sql, (self.id, self.id)).fetchall()
        return[Game.instance_from_row(row) for row in rows]
    
    def away_games(self):
        from models.game import Game
        sql = """
        SELECT * FROM games
        OR away_team = ?
        """
        rows = CURSOR.execute(sql, (self.id, self.id)).fetchall()
        return[Game.instance_from_row(row) for row in rows]
        
    def tournaments(self):
        from models.game import Game
        from models.tournament import Tournament
        games = Game.games_by_team(self.id)
        tournaments = []

        for game in games:
            if game.tournament_id not in tournaments:
                tournaments.append(game.tournament_id)
                
        return [Tournament.find_by_id(tournament) for tournament in tournaments]

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