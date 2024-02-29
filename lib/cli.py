# lib/cli.py
import fire
from team_helpers import team_menu

from helpers import (
    exit_program
)

def main():
    while True:
        print_menu()
        menu = {
            "0": exit_program,
            "1": team_menu
        }
        choice = input("> ")
        function = menu.get(choice)
        if choice:
            function()
        else:
            print("Invalid Option")


def print_menu():
    print("=== Main Menu ===")
    print("0. Exit the program")
    print("1. Create / Modify / Find a Team")


if __name__ == "__main__":
    fire.Fire(main)
