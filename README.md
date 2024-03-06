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

---

## Running the CLI

The CLI script exists in lib/cli.py.
Run `python lib/cli.py` in your terminal to open and run the Tournament Organizer interface, then follow the instructions.


### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Languages / Tools
- Python
- Pip
- SQL

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
