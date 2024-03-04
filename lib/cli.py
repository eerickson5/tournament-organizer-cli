# lib/cli.py
import fire
from team_helpers import team_editor_menu, team_explorer
from game_helpers import change_game_score
from tournament_helpers import view_all_tournaments

from helpers import (
    exit_program
)

def main():
    while True:
        print_menu()
        menu = {
            "0": exit_program,
            "1": view_all_tournaments,
            "2": team_explorer,
            "3": change_game_score
        }
        choice = input("> ")
        function = menu.get(choice)
        if choice:
            function()
        else:
            print("Invalid Option")


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
    fire.Fire(main)
