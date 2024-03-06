# Tournament Organizer CLI

## Introduction

Tournament Organizer CLI is an interface tool for league and tournament organizers to add and organize teams, games, and tournaments.  Games are comprised of a home and away team object, and each team's score.  Games can be added to tournaments.  

Users can access a teams games played and tournaments participated in.  For each game, users can access the teams, score, and winner.  Users can also access a tournament's games and which teams participated in the tournament. 

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── team.py
    │   ├── tournament.py
    │   └── game.py
    ├── cli.py
    ├── debug.py
    ├── seed.py
    ├── game_helpers.py    
    ├── team_helpers.py    
    ├── tournament_helpers.py    
    └── helpers.py
```

Access to the CLI main menu exists in cli.py.  An exit helper method is in helpers.py.  The main menu leads to either the tournament menu, which is in tournament_helpers.py or the team menu, which is in team_helpers.  The tournament menu may lead to a game menu, which is in game_helpers.  All the helper functions for these menus exist in these 3 files.

seed.py holds some code for populating the SQL database with starter data.

In the models folder, team.py holds the Team class and all its methods.  The same goes for tournament.py and game.py and the Tournament and Game classes respectively.  Each class has getter and setter methods, as well as some calculated properties and relational methods for interacting with the other classes.

---

## Running the CLI

The CLI script exists in lib/cli.py.
Run `python lib/cli.py` in your terminal to open and run the Tournament Organizer interface, then follow the instructions.

---

## Languages / Tools
- Python
- Pip
- SQL

