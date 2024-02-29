# lib/cli.py
import fire
from team_helpers import team_editor_menu, team_explorer

from helpers import (
    exit_program
)

def main():
    while True:
        print_menu()
        menu = {
            "0": exit_program,
            "1": team_editor_menu,
            "2": team_explorer
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
    print("1. Create / Modify a Team")
    print("2. Find / Learn About a Team")


if __name__ == "__main__":
    fire.Fire(main)
