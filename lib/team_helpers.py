# lib/team_helpers.py
from models.team import Team

def edit_team_menu(team):
    print(f" ===== Team Menu - {team.name} ===== ")
    print("0. Back to Main Menu")
    print("1. View All Games")
    print("2. View All Tournaments")
    print("3. View Record")
    print("4. Rename Team")
    print("X. Delete Team")
    menu = {
        "0": go_back,
        "1": get_all_games,
        "2": get_all_tournaments,
        "3": get_record,
        "4": rename_team,
        "X": delete_team
    }
    choice = input("> ")
    function = menu.get(choice)
    if choice:
        function(team)
    else:
        print("Invalid Option")

def get_all_teams():
    teams = Team.display_all_teams()

    if not teams:
        print("No teams exist yet.")
    else:
        print("Teams:")
        for team in teams:
            print(team.to_string())
    go_back()

def create_team():
    name = input("New Team Name > ")

    while len(name) < 3:
        print(f"Team names must be longer than 2 characters.")
        name = input("Team Name or 0 to exit > ")
        if name == "0":
            return

    team = Team.create_team(name)
    print(f"Team Created: {team.name}")
    edit_team_menu(team)

def find_team():
    name = input("Team Name > ")
    teams = Team.find_by_name(name)
    if len(teams) == 0:
        print(f"No teams called {name} found.")
    elif len(teams) == 1:
        edit_team_menu(teams[0])
    else:
        print(f"{len(teams)} teams found.")
        counter = 1
        for team in teams:
            print(f"{counter}: {team.to_string()}")
            counter += 1
        choice = input("Choose a team to view or enter 0 to return to main menu > ")
        if choice == "0":
            go_back(None)
        else:
            edit_team_menu(teams[int(choice) - 1])

def get_all_games(team):
    games = team.games()
    print(f"\nAll games played by {team.name}:")
    for game in games:
        print(game.to_string())
    print(f"\n")
    edit_team_menu(team)

def get_all_tournaments(team):
    tournaments = team.tournaments()
    print(f"\nTournaments:")
    for tournament in tournaments:
        print(tournament.name)
    print(f"\n")
    edit_team_menu(team)

def get_record(team):
    print(f"\n{team.to_string()}\n")
    edit_team_menu(team)

def rename_team(team):
    name = input("New Team Name > ")
    while len(name) < 3:
        print("Name must be longer than 2 characters.")
        name = input("New Team Name or input 0 to exit > ")
        if name == "0":
            return
    team.name = name
    team.save()
    print(f"Success! Team renamed to {team.name}")
    edit_team_menu(team)

def get_teams_from_name():
    name = input("Name to Search > ")
    if teams := Team.find_by_name(name):
        print(f"... Team(s) Found: {teams}")
    else:
        print(f"... No teams with name {name} exist.")

def delete_team(team):
    print("Are you sure you want to delete this team and all games it played?")
    choice = input("Input y to delete and any other key to cancel > ")
    if choice == "y":
        games = team.games()
        for game in games:
            game.delete_game()
        team.delete_team()
        print(f"{team.name} deleted.")
    else:
        edit_team_menu(team)
    go_back()

def go_back(team):
    print("...")

def go_back():
    print("...")
