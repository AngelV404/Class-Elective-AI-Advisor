-- Degrees
INSERT INTO Degree (id, name, level) VALUES
(1, 'Computer Science B.S.', 'Bachelor'),
(2, 'Biology B.S.', 'Bachelor'),
(3, 'Data Science M.S.', 'Master');

-- Courses
INSERT INTO Course (id, code, name, credits, Department) VALUES
(101, 'CS101', 'Intro to Programming', 3, 'Computer Science'),
(102, 'CS201', 'Data Structures', 4, 'Computer Science'),
(103, 'CS301', 'Algorithms', 4, 'Computer Science'),
(104, 'CS401', 'Machine Learning', 3, 'Computer Science'),
(201, 'BIO101', 'General Biology I', 3, 'Biology'),
(202, 'BIO201', 'Genetics', 3, 'Biology');

-- Sections
INSERT INTO Section (section_num, course_id, instructor, Capacity, Registered, Waitlist) VALUES
(1, 101, 'Dr. Smith',31,29,0),
(2, 101, 'Dr. Johnson',32,27,0),
(3, 102, 'Prof. Martinez',40,40,2),
(4, 201, 'Dr. Chen',36,36,1);

-- Users
INSERT INTO "User" (username, Email, Hashed_Pw, Degree) VALUES
('Alice Johnson', 'temp1@gmail.com', 'test1',2),
('Bob Williams', 'temp2@gmail.com', 'test2',1),
('Carol Smith', 'temp3@gmail.com', 'test3',3),
('David Martinez', 'temp4@gmail.com', 'test4',2),
('Edwin Shum', 'temp5@gmail.com', 'test5',3);

-- Prerequisites
INSERT INTO Prerequisites (prereq_id, course_id) VALUES
(102, 101),
(103, 102),
(104, 103),
(202, 201);
