import os
import sqlite3

def connectdb():
    # Connect to db and generate a cursor
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        print("connection successful")

    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")


    # Find current working directory
    cwd = os.getcwd()
    print(cwd)

    # Open and run db setup file
    try:
        with open('./db/db.sql', 'r') as file:
            script = file.read()
        cursor.executescript(script)
        con.commit()
        print("Tables Created")
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
    except FileNotFoundError:
        print("Setup File not found")

    # Import data into the db 
    try:
        with open('./db/data.sql', 'r') as file:
            script = file.read()
        cursor.executescript(script)
        con.commit()
        print("Data inputed")
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
    except FileNotFoundError:
        print("Data file not found")

    con.execute("PRAGMA foreign_keys = ON;")
    con.commit()
    cursor.close()
    con.close()