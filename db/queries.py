import sqlite3

def get_courses(code, name):
    # Connect to db and generate a cursor
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        print("connection successful")
        name = name.get()
        code = code.get()
        query = "SELECT code, name FROM course"

        if code != "" or name != "":
            query += " WHERE "
            if code and not name:
                query += "code LIKE '" + code + "%'"
            elif name and not code:
                query += "name LIKE '" + name + "%'"
            else:
                query += "code LIKE '" + code + "%' AND name LIKE '" + name + "%'"
        cursor.execute(query)
        results = cursor.fetchall()

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        con.close()
        return results