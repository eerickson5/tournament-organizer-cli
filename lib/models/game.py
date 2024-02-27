class Game:

    all = []
    
    def __init__(self, home_team_id, away_team_id):
        self.home_team = home_team_id
        self.away_team = away_team_id
        self.all.append(self)

    def add_score(self, home_score, away_score):
        if type(home_score) == int and type(away_score == int):
            self.home_score = home_score
            self.away_score = away_score
        else:
            raise TypeError("Scores must be submitted as ints.")
        
    def add_to_bracket(self, tournament_id):
        # and there exists a tournament with that id
        if type(tournament_id) == int:
            self.tournament_id = tournament_id
        else:
            raise TypeError("Tournament IDs must be of type int.")

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