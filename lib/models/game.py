from models.__init__ import CURSOR, CONN
from models.tournament import Tournament

class Game:

    all = {}

    def __init__(self, home_team_id, away_team_id, tournament_id = None):
        self.home_team = home_team_id
        self.away_team = away_team_id
        if tournament_id:
            self.tournament_id = tournament_id

    def __repr__(self):
        string = f"Game(id={self.id}, home_team={self.home_team}, away_team={self.away_team}" 
        if self.away_score and self.home_score:
            string += f", home_score={self.home_score}, away_score={self.away_score}"
        try:
            string += f", tournament_id={self.tournament_id})"
        except AttributeError:
            string += ")"
        return string
    
    def add_to_bracket(self, tournament_id):
        # and there exists a tournament with that id
        if type(tournament_id) == int:
            self.tournament_id = tournament_id
        else:
            raise TypeError("Tournament IDs must be of type int.")
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Game instances """
        sql = """
            CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            home_team INTEGER, 
            away_team INTEGER,
            tournament_id INTEGER,
            home_score INTEGER,
            away_score INTEGER,
            FOREIGN KEY (home_team) REFERENCES teams(id)
            FOREIGN KEY (away_team) REFERENCES teams(id)
            FOREIGN KEY (tournament_id) REFERENCES tournaments(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS games
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_game(cls, home_team_id, away_team_id, tournament_id = None):
        game = cls(home_team_id, away_team_id, tournament_id)
        game.save()
        return game
    
    @classmethod
    def instance_from_row(cls, row):
        game = cls(row[1], row[2], row[3])
        game.id = row[0]
        if row[4] and row[5]:
            game.home_score = row[4]
            game.away_score = row[5]
        cls.all[game.id] = game
        return game

    
    @classmethod
    def display_all_games(cls):
        sql = """
        SELECT * FROM games
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_row(row) for row in rows]

    def save(self):
        sql = """
            INSERT INTO games (home_team, away_team)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.home_team, self.away_team))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def delete_game(self):
        sql = """
        DELETE FROM games
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    def add_to_tournament(self, tournament):
        #and not already in a tournment ?
        if type(tournament) == int and Tournament.find_by_id(tournament):
            self.tournament_id = tournament
            sql = """
                UPDATE games SET tournament_id = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.tournament_id, self.id))
            CONN.commit()
        else:
            raise AttributeError("No tournament exists with that ID. Tournament ID should be an int.")

    def add_scores(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score
        sql = """
            UPDATE games
            SET home_score = ?, away_score = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.home_score, self.away_score, self.id))
        CONN.commit()


    # home team property
    @property
    def home_team(self):
        return self._home_team
    @home_team.setter
    def home_team(self, home_team_id):
        # and there exists a team with that ID
        if type(home_team_id) == int:
            self._home_team = home_team_id
        else:
            raise TypeError("Team IDs must be type int.")
        

    # away team property
    @property
    def away_team(self):
        return self._away_team
    @away_team.setter
    def away_team(self, away_team_id):
        # and there exists a team with that ID
        if type(away_team_id) == int:
            self._away_team = away_team_id
        else:
            raise TypeError("Team IDs must be type int.")
        
    @property
    def home_score(self):
        try:
            return self._home_score
        except AttributeError:
            return None
    
    @home_score.setter
    def home_score(self, score):
        if type(score) == int and score >= 0:
            self._home_score = score
        else:
            raise AttributeError("Scores must be non-negative integers.")
        
    @property
    def away_score(self):
        try:
            return self._away_score
        except AttributeError:
            return None
    
    @away_score.setter
    def away_score(self, score):
        if type(score) == int and score >= 0:
            self._away_score = score
        else:
            raise AttributeError("Scores must be non-negative integers.")