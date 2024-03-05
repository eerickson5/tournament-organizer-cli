# lib/team_helpers.py
from models.team import Team

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

def get_all_teams():
    teams = Team.display_all_teams()

    if not teams:
        print("No teams exist yet.")
    else:
        print("Teams:")
        for team in teams:
            record = team.record()
            print(f"{team.name} {record[0]}-{record[1]}-{record[2]}")
    go_back()

def add_team():
    name = input("Team Name > ")
    try:
        team = Team.create_team(name)
        print(f"... Success! Team Created: {team}")
    except TypeError:
        print(f"... Failed. Invalid Team Name.")

def rename_team():
    id = input("ID of Team to Rename > ")
    if team := validate_team_id(id):
        try:
            team.name = input("New Team Name > ")
            team.save()
            print(f"... Success! Team renamed to {team.name}")
        except TypeError:
            print("... Failed. Invalid Team Name.")

def get_teams_from_name():
    name = input("Name to Search > ")
    if teams := Team.find_by_name(name):
        print(f"... Team(s) Found: {teams}")
    else:
        print(f"... No teams with name {name} exist.")

def go_back():
    print("...")
