-- =========================
-- Drop existing tables in dependency order
-- =========================
DROP TABLE IF EXISTS Taken;
DROP TABLE IF EXISTS GE_Requirements;
DROP TABLE IF EXISTS DG_Requirements;
DROP TABLE IF EXISTS PreRequisites;
DROP TABLE IF EXISTS Timeslots;
DROP TABLE IF EXISTS Section;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Degree;
DROP TABLE IF EXISTS Preferences;

-- =========================
-- Degree Table
-- =========================
CREATE TABLE Degree (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(255) NOT NULL,
    Level VARCHAR(255) NOT NULL,
    Dept VARCHAR(255)
);

-- =========================
-- User Table
-- =========================
CREATE TABLE User (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username VARCHAR(255) NOT NULL UNIQUE,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Hashed_Pw VARCHAR(255) NOT NULL,
    Created_At DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Degree INT,
    FOREIGN KEY (Degree) REFERENCES Degree(ID)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- =========================
-- Course Table
-- =========================
CREATE TABLE Course (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code VARCHAR(10) NOT NULL UNIQUE,
    Name VARCHAR(255) NOT NULL UNIQUE,
    Description TEXT,
    Credits INT,
    Department VARCHAR(255)
);

-- Index for quick lookup by Department
CREATE INDEX idx_course_dept ON Course(Department);

-- =========================
-- Section Table
-- =========================
CREATE TABLE Section (
    Section_num INT,
    Course_id INT,
    Instructor VARCHAR(255) NOT NULL,
    Capacity INT,
    Registered INT CHECK(Registered <= Capacity),
    Waitlist INT,
    PRIMARY KEY (Section_num, Course_id),
    FOREIGN KEY (Course_id) REFERENCES Course(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- =========================
-- Timeslots Table
-- =========================
CREATE TABLE Timeslots (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Section_ID INT NOT NULL,
	Course_ID INT NOT NULL,
    Day VARCHAR(50),
    Start_Time TIME,
    End_Time TIME,
    Building VARCHAR(255),
    Room VARCHAR(255),
    FOREIGN KEY (Section_ID, Course_ID) REFERENCES Section(Section_num, Course_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Index for faster queries by day/time
CREATE INDEX idx_timeslot_day_time ON Timeslots(Day, Start_Time, End_Time);

-- =========================
-- Prerequisites Table
-- =========================
CREATE TABLE PreRequisites (
    Course_ID INT NOT NULL,
    Prereq_ID INT NOT NULL,
    PRIMARY KEY (Course_ID, Prereq_ID),
    FOREIGN KEY (Course_ID) REFERENCES Course(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (Prereq_ID) REFERENCES Course(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- =========================
-- Degree Requirements Table
-- =========================
CREATE TABLE DG_Requirements (
    Req_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Degree_ID INT NOT NULL,
    Course INT NOT NULL,
    Type VARCHAR(255),
    FOREIGN KEY (Degree_ID) REFERENCES Degree(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (Course) REFERENCES Course(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Index for finding all courses required by a degree
CREATE INDEX idx_dg_req_degree ON DG_Requirements(Degree_ID);

-- =========================
-- GE Requirements Table
-- =========================
CREATE TABLE GE_Requirements (
    Degree_ID INTEGER PRIMARY KEY,
    A_CR INT,
    B_CR INT,
    C_CR INT,
    D_CR INT,
    E_CR INT,
    F_CR INT,
    FOREIGN KEY (Degree_ID) REFERENCES Degree(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- =========================
-- Taken Table (junction for User <-> Course)
-- =========================
CREATE TABLE Taken (
    User_ID INTEGER NOT NULL,
    Course_ID INT NOT NULL,
    PRIMARY KEY (User_ID, Course_ID),
    FOREIGN KEY (User_ID) REFERENCES User(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (Course_ID) REFERENCES Course(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Index for fast queries of all courses taken by a user
CREATE INDEX idx_taken_user ON Taken(User_ID);
CREATE INDEX idx_taken_course ON Taken(Course_ID);

-- =========================
-- Preferences Table
-- =========================
CREATE TABLE Preferences (
	User_ID INTEGER PRIMARY KEY,
	Time varchar(255),
	Days varchar(255),
	FOREIGN KEY (User_ID) REFERENCES User(ID)
		ON UPDATE CASCADE
		ON DELETE CASCADE
	
);