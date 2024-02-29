# lib/team_helpers.py
from models.team import Team

def team_menu():
    print(" === Team Menu === ")
    print("0. Back to Main Menu")
    print("1. Add a Team")
    print("2. Rename a Team")
    print("3. Search Team by ID")
    print("4. Search Team(s) by Name")
    print("3. Delete a Team")
    menu = {
        "0": go_back,
        "1": add_team,
        "2": rename_team,
        "3": get_team_from_id,
        "4": get_teams_from_name
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
    id = input("ID to Search > ")
    if team := validate_team_from_id(id):
        print(f"... Team Found: {team}")

def get_teams_from_name():
    name = input("Name to Search > ")
    if teams := Team.find_by_name(name):
        print(f"... Team(s) Found: {teams}")
    else:
        print(f"... No teams with name {name} exist.")

def validate_team_from_id(id):
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
