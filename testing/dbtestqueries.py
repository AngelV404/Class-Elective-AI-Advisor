import sqlite3

def sv01_sv02(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [row[0] for row in cursor.fetchall()]

    # Define header
    header = [
        "Table", "Column", "Type", "NotNull", "PK",
        "FK_From", "FK_RefTable", "FK_RefCol", "FK_OnUpdate", "FK_OnDelete"
    ]

    # Prepare rows
    rows = []

    for table in tables:
        # Column info
        cursor.execute(f"PRAGMA table_info('{table}')")
        columns = cursor.fetchall()  # (cid, name, type, notnull, dflt_value, pk)

        # Foreign key info
        cursor.execute(f"PRAGMA foreign_key_list('{table}')")
        foreign_keys = cursor.fetchall()  # (id, seq, table, from, to, on_update, on_delete, match)
        fk_map = {fk[3]: fk for fk in foreign_keys}  # column name -> FK

        for col in columns:
            col_name = col[1]
            if col_name in fk_map:
                fk = fk_map[col_name]
                rows.append([
                    table, col_name, col[2], col[3], col[5],
                    fk[3], fk[2], fk[4], fk[5], fk[6]
                ])
            else:
                rows.append([
                    table, col_name, col[2], col[3], col[5],
                    "", "", "", "", ""
                ])

    # Compute column widths
    col_widths = [max(len(str(row[i])) for row in [header]+rows) for i in range(len(header))]

    # Print header
    print(" | ".join(str(header[i]).ljust(col_widths[i]) for i in range(len(header))))
    print("-+-".join('-'*w for w in col_widths))

    # Print rows
    for row in rows:
        if row[4] > 0 or row[5]:
            print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

def sv03(cursor):
    try:
        # Insert two users with the same email
        cursor.execute("INSERT INTO 'User' (id, username, degree, email, hashed_pw) VALUES (999, 'Test User1', 1, 'duplicate@email.com', 'abc321');")
        cursor.execute("INSERT INTO 'User' (id, username, degree, email, hashed_pw) VALUES (1000, 'Test User2', 1, 'duplicate@email.com', 'abc123');")
        print("Insertion successful")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

def sv04(cursor):
    try:
        # Create a new course
        cursor.execute("INSERT INTO Course (Code, Name, credits, department) VALUES (102,NULL, 4,'Computer Science');")
        print("Insertion Successful")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

def di01(cursor):
    try:
        # Create a new degree requirement
        cursor.execute("INSERT INTO DG_Requirements ('Degree_ID','Course','Type') VALUES (9999,'104','Core_Upper')")
        print("Insertion Successful")
    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")

def di02(cursor):
    try:
        # Create a new prerequisite
        cursor.execute("INSERT INTO Prerequisites ('Course_ID','Prereq_ID') VALUES (102,101)")
        print("Insertion Successful")
    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")

def di03(cursor):
    try:
        # Update registered users in a section
        cursor.execute("UPDATE section SET registered = 33, waitlist = 1 WHERE section_num = 2 AND course_id = 101")
        print("Insertion Successful")
    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")

def di04(cursor):
    try:
        # Insert a timeslot without a correct course and section ID
        cursor.execute("INSERT INTO Timeslots ('Section_ID','Course_ID','Day','Start_time','End_Time','Building','Room') VALUES (9999,9999,'Mon/Wed/Fri', '10:00:00', '11:50:00','Engineering','204')")
        print("Insertion Successful")
    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")

def ft01(cursor):
    try:
        # Grab degree name, course name, and requirement type
        cursor.execute("SELECT d.Name, c.Name, dr.Type FROM DG_Requirements dr LEFT JOIN Course c ON c.ID = dr.Course LEFT JOIN Degree d ON dr.Degree_ID = d.ID WHERE Degree_ID = 1")
        result = cursor.fetchall()

        header = ["Degree", "Course", "Type"]

        # Calculate column widths
        col_widths = [max(len(str(row[i])) for row in [header]+result) for i in range(len(header))]
        
        # Print header
        print(" | ".join(str(header[i]).ljust(col_widths[i]) for i in range(len(header))))
        print("-+-".join('-'*w for w in col_widths))

        # Print rows
        for row in result:
            print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")

def ft02(cursor):
    try:
        # Grab username, course code, and section number
        cursor.execute("SELECT u.Username, t.Course_ID, c.Code FROM User u LEFT JOIN Taken t ON u.ID = t.user_id LEFT JOIN Course c ON c.ID = t.Course_ID")
        result = cursor.fetchall()

        header = ["Username", "Course", "Code"]

        # Calculate column widths
        col_widths = [max(len(str(row[i])) for row in [header]+result) for i in range(len(header))]
        
        # Print header
        print(" | ".join(str(header[i]).ljust(col_widths[i]) for i in range(len(header))))
        print("-+-".join('-'*w for w in col_widths))

        # Print rows
        for row in result:
            print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")


def ft03(cursor):
    try:
        # Grab Course code and name and prerequisite code and name
        cursor.execute("SELECT c1.Code, c1.Name, c2.Code, c2.Name FROM prerequisites p LEFT JOIN course c1 ON p.Course_ID = c1.ID LEFT JOIN course c2 ON c2.ID = p.prereq_id WHERE c1.department = 'Biology';")
        result = cursor.fetchall()

        header = ["Course Code", "Course Name", "Prereq Code", "Prereq Name"]

        # Calculate column widths
        col_widths = [max(len(str(row[i])) for row in [header]+result) for i in range(len(header))]
        
        # Print header
        print(" | ".join(str(header[i]).ljust(col_widths[i]) for i in range(len(header))))
        print("-+-".join('-'*w for w in col_widths))

        # Print rows
        for row in result:
            print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")


def ft04(cursor):
    try:
        # Grab each degree and their ge-requirements
        cursor.execute("SELECT d.Name, gr.A_CR AS 'Core Competencies', gr.B_CR AS 'Scientific Inquiry', gr.C_CR AS 'Arts and Humanities', gr.D_CR AS 'Social Sciences', gr.E_CR AS 'Self Development', gr.F_CR AS 'Ethnic Studies' FROM Degree d LEFT JOIN GE_Requirements gr ON gr.Degree_ID = d.ID;")
        result = cursor.fetchall()

        header = ['Degree', 'Core Competencies','SCIENTIFIC INQUIRY...', 'Arts and Humanities', 'Social Sciences', 'Self Development', 'Ethnic Studies']

        # Calculate column widths
        col_widths = [max(len(str(row[i])) for row in [header]+result) for i in range(len(header))]
        
        # Print header
        print(" | ".join(str(header[i]).ljust(col_widths[i]) for i in range(len(header))))
        print("-+-".join('-'*w for w in col_widths))

        # Print rows
        for row in result:
            print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))

    except sqlite3.Error as e:
        print(f"SQL Error:  {e}")