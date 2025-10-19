import os
import sqlite3
import dbtestqueries as dbq

# Connect to db and generate a cursor
def db_cursor():
    try:
        con = sqlite3.connect("test.db")
        cursor = con.cursor()
        con.execute("PRAGMA foreign_keys = ON;")
        yield cursor
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

# Test Case SV-01 and SV-02
# EXPECTED: 10 distinct tables, 7 with Primary Keys, 3 with Composite Keys, 12 Foreign Keys
def test_sv01_sv02(db_cursor): dbq.sv01_sv02(db_cursor)


# Test Case SV-03
# EXPECTED: SQL Error UNIQUE constraint failed: User.Email
def test_sv03(db_cursor): dbq.sv03(db_cursor)

# Test Case SV-04
# EXPECTED: SQL Error NOT NUL constraint failed: Course.Name
def test_sv04(db_cursor): dbq.sv04(db_cursor)

# Test Case DI-01
# EXPECTED: SQL Error Foreign Key constraint failed
def test_di01(db_cursor): dbq.di01(db_cursor)

# Test Case DI-02
# EXPECTED: SQL Error Unique Constraint failed
def test_di02(db_cursor): dbq.di02(db_cursor)

# Test Case DI-03
# EXPECTED: SQL Error Check Constraint failed
def test_di03(db_cursor): dbq.di03(db_cursor)

# Test Case DI-04
# EXPECTED: SQL Error Foreign Key constraint failed
def test_di04(db_cursor): dbq.di04(db_cursor)

# Test Case FT-01
# EXPECTED: Table of all required courses for Computer Science Degree
def test_ft01(db_cursor): dbq.ft01(db_cursor)

# Test Case FT-02
# EXPECTED: Table of all users enrolled in CS301-01
# def test_ft01(db_cursor): dbq.ft02(db_cursor)

# Test Case FT-03
# EXPECTED: Table of all prerequisites for Biology courses
def test_ft03(db_cursor): dbq.ft03(db_cursor)

# Test Case FT-04
# EXPECTED: Table of all ge_requirements for each degree
def test_ft04(db_cursor): dbq.ft04(db_cursor)
