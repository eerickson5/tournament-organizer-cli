# lib/cli.py
import fire
from seed import seed_database
from tournament_helpers import view_all_tournaments, find_tournament, create_tournament
from team_helpers import get_all_teams, create_team, find_team

from helpers import (
    exit_program
)

def main():
    while True:
        print_menu()
        menu = {
            "0": exit_program,
            "1": view_all_tournaments,
            "2": find_tournament,
            "3": create_tournament,
            "4": get_all_teams,
            "5": find_team,
            "6": create_team
        }
        choice = input("> ")
        function = menu.get(choice)
        # try:
        function()
        # except TypeError:
        #     print("Invalid Option")


def print_menu():
    print("===== Main Menu =====")
    print("0. Exit the program")
    print("1. View All Tournaments")
    print("2. Find and Edit a Tournament")
    print("3. Create a Tournament")
    print("4. View All Teams")
    print("5. Find and Edit a Team")
    print("6. Create a Team")


if __name__ == "__main__":
    seed_database()
    fire.Fire(main)
