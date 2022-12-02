"""Ignore file. Used to populate the menu table because somehow importing the csv wasn't working as expected.
"""
import os

from util import create_db_connection
with open("data/menu.csv", 'r') as f:
    data = f.readlines()
    rows = []
    with open("sql/insert-menu.sql", 'w') as fp:

        for line in data:
            r = ""
            for _ in [row for row in line.strip().split(",")]:
                r += f"\"{_}\", "
            entry = f"INSERT INTO MENU VALUES({r.strip()[: -1]});"
            fp.write(entry + os.linesep)
        