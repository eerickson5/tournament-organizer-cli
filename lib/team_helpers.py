# lib/team_helpers.py
from models.team import Team
from models.game import Game

def team_editor_menu():
    print(" ===== Team Menu ===== ")
    print("0. Back to Main Menu")
    print("1. Add a Team")
    print("2. Rename a Team")
    print("3. Delete a Team")
    menu = {
        "0": go_back,
        "1": add_team,
        "2": rename_team
    }
    choice = input("> ")
    function = menu.get(choice)
    if choice:
        function()
    else:
        print("Invalid Option")

def team_explorer():
    print(" ===== Team Explorer ===== ")
    print("0. Back to Main Menu")
    print("1. Search Team by ID")
    print("2. Search Team(s) by Name")
    print("3. Get Games Played by a Team")
    print("4. Get Games Won by a Team")
    print("5. Get Home Games by a Team")
    print("6. Get Away Games by a Team")
    print("7. Get Tournaments Played by a Team")
    menu = {
        "0": go_back,
        "1": get_team_from_id,
        "2": get_teams_from_name,
        "3": get_games_from_team_id,
        "4": get_games_won_from_team_id,
        "5": get_home_games_from_team_id,
        "6": get_away_games_from_team_id,
    }
    choice = input("> ")
    function = menu.get(choice)
    if choice:
        function()
    else:
        print("Invalid Option")

def add_team():
    name = input("Team Name > ")
    try:
        team = Team.create_team(name)
        print(f"... Success! Team Created: {team}")
    except TypeError:
        print(f"... Failed. Invalid Team Name.")

def rename_team():
    id = input("ID of Team to Rename > ")
    if team := validate_team_from_id(id):
        try:
            team.name = input("New Team Name > ")
            team.save()
            print(f"... Success! Team renamed to {team.name}")
        except TypeError:
            print("... Failed. Invalid Team Name.")

def get_team_from_id():
    team = validate_team_id()
    print(f"... Team Found: {team}")

def get_teams_from_name():
    name = input("Name to Search > ")
    if teams := Team.find_by_name(name):
        print(f"... Team(s) Found: {teams}")
    else:
        print(f"... No teams with name {name} exist.")

def get_games_from_team_id():
    team = validate_team_id()
    print(f"Games Played: {Game.games_by_team(team.id)}")

def get_games_won_from_team_id():
    team = validate_team_id()
    games = Game.games_won_by_team(team.id)
    if games:    
        print(f"-- {len(games)} games won:")   
        print(f"Games Won: {games}")
    else:
        print(f"This team has not won any games.")

def get_away_games_from_team_id():
    team = validate_team_id()
    games = Game.away_games_by_team(team.id)
    if games:       
        print(f"-- {len(games)} away games played:")  
        print(f"Away Games: {games}")
    else:
        print(f"This team has not played any away games.")

def get_home_games_from_team_id():
    team = validate_team_id()
    games = Game.home_games_by_team(team.id)
    if games:       
        print(f"-- {len(games)} home games played:")  
        print(f"Home Games {games}")
    else:
        print(f"This team has not played any home games.")

# def get_tournaments_from_team_id():
#     id = input("ID of Team > ")
#     team = validate_team_from_id
#     games

def validate_team_id():
    id = input("ID of Team > ")
    team = Team.find_by_id(id)
    while not team:
        id = input("Invalid ID. Try again or input 0 to exit > ")
        if id == "0":
            go_back()
            return
        else:
            team = Team.find_by_id(id)
    return team

def go_back():
    print("...")
