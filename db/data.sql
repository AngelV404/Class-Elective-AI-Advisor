-- Degrees
INSERT INTO Degree (id, name, level) VALUES
(1, 'Computer Science B.S.', 'Bachelor'),
(2, 'Biology B.S.', 'Bachelor'),
(3, 'Data Science M.S.', 'Master');

-- Courses
INSERT INTO Course (id, code, name, credits, Department, Description) VALUES
(101, 'CPSC101', 'Intro to Programming', 3, 'Computer Science','This is a short description meant to be replaced later'),
(102, 'CPSC201', 'Data Structures', 4, 'Computer Science','This is a short description meant to be replaced later'),
(103, 'CPSC301', 'Algorithms', 4, 'Computer Science','This is a short description meant to be replaced later'),
(104, 'CPSC401', 'Machine Learning', 3, 'Computer Science','This is a short description meant to be replaced later'),
(201, 'BIO101', 'General Biology I', 3, 'Biology','This is a short description meant to be replaced later'),
(202, 'BIO201', 'Genetics', 3, 'Biology','This is a short description meant to be replaced later');

-- Sections
INSERT INTO Section (section_num, course_id, instructor, Capacity, Registered, Waitlist) VALUES
(1, 101, 'Dr. Smith',31,29,0),
(2, 101, 'Dr. Johnson',32,27,0),
(1, 102, 'Prof. Martinez',40,40,2),
(1, 201, 'Dr. Chen',38,32,0),
(1, 103, 'Dr. Paige',37,31,0),
(1, 202, 'Dr. Viktor',36,35,0);

-- Users
INSERT INTO "User" (username, Email, Hashed_Pw, Degree) VALUES
('Alice Johnson', 'temp1@gmail.com', 'test1',2),
('Bob Williams', 'temp2@gmail.com', 'test2',1),
('Carol Smith', 'temp3@gmail.com', 'test3',3),
('David Martinez', 'temp4@gmail.com', 'test4',2),
('Edwin Shum', 'temp5@gmail.com', 'test5',3);

-- Prerequisites
INSERT INTO Prerequisites (prereq_id, course_id) VALUES
(101, 102),
(102, 103),
(103, 104),
(201, 202);

INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
(1, 101, "Core-Lower"),
(1, 102, "Core-Lower"),
(1, 103, "Core-Upper"),
(1, 104, "Core-Upper");

INSERT INTO Taken (User_ID, Course_ID, Section_ID, Status) VALUES
(5, 101, NULL,"taken"),
(5, 102, NULL,"taken"),
(5, 201, NULL,"taken"),
(3, 103, 1, "in-progress"),
(4, 103, 1, "in-progress"),
(5, 103, 1, "in-progress"),
(1, 202, 1, "in-progress"),
(2, 202, 1, "in-progress"),
(5, 202, 1, "in-progress"),
(5, 104, NULL,"wishlist");

INSERT INTO GE_Requirements (Degree_ID, A_CR, B_CR, C_CR, D_CR, E_CR, F_CR) VALUES
(1, 6, 12, 9, 6, 0, 3),
(2, 9, 3, 6, 7, 7, 3),
(3, 6, 12, 9, 6, 0, 3);