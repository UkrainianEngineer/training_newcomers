import sqlite3

# Create database connector.
connector = sqlite3.connect("user.db")

# Create SQLite3 cursor from connector.
cursor = connector.cursor()
