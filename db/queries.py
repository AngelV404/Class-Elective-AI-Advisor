import sqlite3

def get_user(email):
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = f"SELECT * FROM user WHERE email = '{email}';"
        cursor.execute(query)
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        con.close()
        return results[0][0]

def get_courses(code, name):
    # Connect to db and generate a cursor
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        name = name.get()
        code = code.get()
        query = "SELECT code, name, description, id FROM course"

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
    
def get_sections(id):
    # Connect to db and generate a cursor
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = f"SELECT c.code, c.name, s.section_num, c.credits, c.Department, c.Description, s.instructor, s.Capacity, s.Registered, s.Waitlist, c.id FROM Section s LEFT JOIN Course c ON s.course_id = c.id WHERE course_id = {id}"
        cursor.execute(query)
        results = cursor.fetchall()

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        con.close()
        return results
    
def get_prereq_status(course, user):
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = f"SELECT c.code, c.name, CASE WHEN (t.status = 'taken' AND t.user_id = '{user}') THEN 1 WHEN (t.status = 'in-progress' AND t.user_id = '{user}') THEN 2 ELSE 0 END AS fulfilled FROM Prerequisites p LEFT JOIN Course c ON c.id = p.prereq_id LEFT JOIN Taken t ON t.course_id = p.prereq_id WHERE p.course_id = '{course}'"
        cursor.execute(query)
        results = cursor.fetchall()

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        con.close()
        return results
    
def get_saved(user):
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = f"SELECT c.code, c.name, t.status, c.id FROM Taken t LEFT JOIN Course c ON t.course_id = c.id WHERE user_id = '{user}' AND status = 'wishlist' UNION SELECT c.code, c.name, 'Degree Requirement' AS status, d.course FROM DG_Requirements d LEFT JOIN Course c ON d.course = c.id WHERE degree_id = (SELECT degree FROM user WHERE id = '{user}') AND d.course NOT IN (SELECT course_id FROM taken WHERE user_id = '{user}')"
        cursor.execute(query)
        results = cursor.fetchall()

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        con.close()
        return results
    
def get_course_details(course):
    try:
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = f"SELECT * FROM Course WHERE id = '{course}'"
        cursor.execute(query)
        results = cursor.fetchall()

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        cursor.close()
        con.close()
        return results