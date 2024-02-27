import sqlite3

CONN = sqlite3.connect('tournament_manager.db')
CURSOR = CONN.cursor()
