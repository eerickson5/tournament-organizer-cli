# lib/game_helpers.py

from models.game import Game

def game_menu(game):
    print(f"\n===== Game Menu - {game.to_string()} ======")
    print("0. Go Back to Tournament Menu")
    print("1. Change Game Score")
    print("2. Get Game Winner")
    print("X. Delete Game")
    menu = {
            "0": go_back,
            "1": change_game_score,
            "2": get_winner,
            "X": delete_game
        }
    choice = input("> ")
    function = menu.get(choice)
    try:
        function(game)
    except:
        print("Invalid Option")

def get_winner(game):
    from models.team import Team
    team = Team.find_by_id(game.winner())
    print(f"{team.name} won this game.")
    game_menu(game)

def change_game_score(game):
    from models.team import Team
    home_team = Team.find_by_id(game.home_team)
    home_score = input_score(home_team.name)

    away_team = Team.find_by_id(game.away_team)
    away_score = input_score(away_team.name)

    game.home_score = home_score
    game.away_score = away_score
    game.save()

    game_menu(game)

def input_score(team_name):
    score = input(f"{team_name} team score > ")
    try:
        score = int(score)
        if score >= 0:
            return score
        else:
            raise Exception
    except:
        print("Try again.  Scores must be non-negative integers.")
        return input_score(team_name)
    
def delete_game(game):
    game.delete_game()
    print("Game deleted...")
    go_back(game)

def go_back(game):
    print("...")
