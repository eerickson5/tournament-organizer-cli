# lib/tournament_helpers.py
from models.tournament import Tournament

def view_all_tournaments():
    tourns = Tournament.all_tournaments()
    print(f"\n {len(tourns)} Tournaments:")
    for tourn in tourns:
        print(f"{tourn.name} - {len(tourn.games())} Games")
    print(f"\n")

def find_tournament():
    name = input("Tournament Name > ")
    tournaments = Tournament.find_by_name(name)
    if len(tournaments) == 0:
        print(f"No Tournaments with name {name} found.")
    elif len(tournaments) == 1:
        edit_tournament_menu(tournaments[0])
    else:
        print(f"{len(tournaments)} tournaments found.")
        counter = 1
        for tourn in tournaments:
            print(f"{counter}: {tourn.name} - {len(tourn.games())} Games")
            counter += 1
        choice = input("Choose a tournament to edit or enter 0 to return to main menu > ")
        edit_tournament_menu(tournaments[int(choice) - 1])

def edit_tournament_menu(tournament):
    print(f"\n===== Tournament Menu - {tournament.name} ======")
    print("0. Go Back to Main Menu")
    print("1. View All Games in Tournament")
    print("2. View All Teams in Tournament")
    print("3. Find and Edit a Game")
    print("4. Add a Game to Tournament")
    print("X. Delete Tournament")
    menu = {
            "0": go_back,
            "1": view_all_games,
            "2": view_all_teams,
            "3": find_game,
            "4": add_game,
            "X": delete_tournament
        }
    choice = input("> ")
    function = menu.get(choice)
    try:
        function(tournament)
    except TypeError:
        print("Invalid Option")

def view_all_games(tournament):
    games = tournament.games()
    print(f"\nGames in {tournament.name}:\n")
    for game in games:
        print(game.toString() + f"\n")
    edit_tournament_menu(tournament)

def view_all_teams(tournament):
    teams = tournament.teams()
    print(f"\nTeams in {tournament.name}:\n")
    for team in teams:
        print(team.name)
    edit_tournament_menu(tournament)

def add_game(tournament):
    from models.game import Game
    from game_helpers import input_score
    home_team = find_team("Home")
    away_team = find_team("Away")
    home_score = input_score(home_team.name)
    away_score = input_score(away_team.name)
    game = Game.create_game(home_team.id, away_team.id)
    game.add_scores(home_score, away_score)
    game.add_to_tournament(tournament.id)
    print("New game created!")
    print(f"{game.toString()}\n")
    edit_tournament_menu(tournament)

def find_team(type):
    from models.team import Team
    name = input(f"{type} Team Name > ")
    teams = Team.find_by_name(name)
    while teams == None:
        print(f"No teams with name {name} found.")
        name = input("Try again or input 0 to cancel > ")
        if name != "0":
            teams = Team.find_by_name(name)
        else:
            return None
    if len(teams) == 1:
        return teams[0]
    else:
        counter = 1
        for team in teams:
            print(f"{counter}. {team.name}")
            counter += 1
        choice = input(f"Choose {type} team or 0 to cancel > ")
        if choice == 0:
            return None
        else:
            return teams[choice - 1]

def delete_tournament(tournament):
    print("Are you sure you want to delete this tournament and all its data?")
    choice = input("Input y to delete and any other key to cancel > ")
    if choice == "y":
        games = tournament.games()
        for game in games:
            game.delete_game()
        tournament.delete_tournament()
        print(f"{tournament.name} deleted.")
    else:
        edit_tournament_menu(tournament)

def find_game(tournament):
    from models.game import Game
    from game_helpers import game_menu
    home_team = find_team("Home")
    away_team = find_team("Away")
    games = Game.find_game_by_tournament_and_teams(tournament.id, home_team.id, away_team.id)
    if len(games) == 0:
        print("No games occurred between these teams during this tournament.")
        edit_tournament_menu(tournament)
    elif len(games) == 1:
        game_menu(games[0])
        edit_tournament_menu(tournament)
    else:
        print(f"Multiple games exist between these teams during this tournament.")
        counter = 1
        for game in games:
            print(f"{counter}: {game.toString()}\n")
            counter += 1
        choice = input("Select game or 0 to exit > ")
        while choice >= counter:
            input("Invalid input.  Try again.")
        if choice == 0:
            edit_tournament_menu(tournament)
        else:
            game_menu(games[choice - 1])
            edit_tournament_menu(tournament)

def create_tournament():
    name = input("New Tournament Name > ")
    while len(name) < 3:
        print("Name must be longer than 2 characters.")
        name = input("New Tournament Name or input 0 to exit > ")
        if name == "0":
            return
    tournament = Tournament.create_tournament(name)
    print(f"\nTournament Created: {tournament.name}\n")
    edit_tournament_menu(tournament)



def go_back(tournament):
    print("...")