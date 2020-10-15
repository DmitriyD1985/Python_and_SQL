import sqlite3


def makeConnection():
    return sqlite3.connect("database.db")
