import os
import sqlite3
import tests

# Connect to db and generate a cursor
try:
    con = sqlite3.connect("test.db")
    cursor = con.cursor()
    print("connection successful")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")

# Find current working directory
cwd = os.path.dirname(os.getcwd())

# Open and run db setup file
try:
    with open(cwd+'/db.sql', 'r') as file:
        script = file.read()
    cursor.executescript(script)
    con.commit()
    print("Tables Created")
except sqlite3.Error as e:
    print(f"SQLite Error: {e}")
except FileNotFoundError:
    print("file not found")

# Import test data into the db 
try:
    with open('testdata.sql', 'r') as file:
        script = file.read()
    cursor.executescript(script)
    con.commit()
    print("Data inputed")
except sqlite3.Error as e:
    print(f"SQLite Error: {e}")
except FileNotFoundError:
    print("file not found")

con.execute("PRAGMA foreign_keys = ON;")

# Test Case SV-01 and SV-02
# EXPECTED: 10 distinct tables, 7 with Primary Keys, 3 with Composite Keys, 12 Foreign Keys
print("\nTest Case SV-01 and SV-02")
tests.sv01_sv02(cursor)

# Test Case SV-03
# EXPECTED: SQL Error UNIQUE constraint failed: User.Email
print("\nTest Case SV-03")
tests.sv03(cursor)

# Test Case SV-04
# EXPECTED: SQL Error NOT NUL constraint failed: Course.Name
print("\nTest Case SV-04")
tests.sv04(cursor)

# Test Case DI-01
# EXPECTED: SQL Error Foreign Key constraint failed
print("\nTest Case DI-01")
tests.di01(cursor)

# Test Case DI-02
# EXPECTED: SQL Error Unique Constraint failed
print("\nTest Case DI-02")
tests.di02(cursor)

# Test Case DI-03
# EXPECTED: SQL Error Check Constraint failed
print("\nTest Case DI-03")
tests.di03(cursor)

# Test Case DI-04
# EXPECTED: SQL Error Foreign Key constraint failed
print("\nTest Case DI-04")
tests.di04(cursor)

# Test Case FT-01
# EXPECTED: Table of all required courses for Computer Science Degree
print("\nTest Case FT-01")
tests.ft01(cursor)

# Test Case FT-02
# EXPECTED: Table of all users enrolled in CS301-01
print("\nTest Case FT-02")
tests.ft02(cursor)

# Test Case FT-03
# EXPECTED: Table of all users enrolled in CS301-01
print("\nTest Case FT-03")
tests.ft03(cursor)

# Test Case FT-04
# EXPECTED: Table of all ge_requirements for each degree
print("\nTest Case FT-04")
tests.ft04(cursor)

if con:
    con.close()