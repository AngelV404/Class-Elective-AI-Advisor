-- Degrees
INSERT INTO Degree (id, name, level) VALUES
(1, 'Computer Science B.S.', 'Bachelor'),
(2, 'Biology B.S.', 'Bachelor'),
(3, 'Data Science M.S.', 'Master'),
(4, 'Mathematics B.S.', 'Bachelor'),
(5, 'Physics B.S.', 'Bachelor'),
(6, 'Economics B.S.', 'Bachelor'),
(7, 'Psychology B.S.', 'Bachelor');

-- Courses
INSERT INTO Course (id, code, name, credits, Department, Description) VALUES
-- Computer Science
(101, 'CPSC101', 'Intro to Programming', 3, 'Computer Science', 'Introduction to fundamental programming concepts using Python, including variables, control structures, and functions.'),
(102, 'CPSC201', 'Data Structures', 4, 'Computer Science', 'Covers arrays, linked lists, stacks, queues, trees, and hash tables with implementation and analysis in Java.'),
(103, 'CPSC301', 'Algorithms', 4, 'Computer Science', 'Study of algorithm design and analysis, including sorting, graph algorithms, and dynamic programming.'),
(104, 'CPSC401', 'Machine Learning', 3, 'Computer Science', 'Explores supervised and unsupervised learning, neural networks, and model evaluation techniques.'),
(105, 'CPSC310', 'Operating Systems', 4, 'Computer Science', 'Focus on process management, memory, file systems, and concurrency in modern operating systems.'),
(106, 'CPSC320', 'Database Systems', 3, 'Computer Science', 'Covers relational databases, SQL, normalization, and basic database design principles.'),
(107, 'CPSC330', 'Computer Networks', 3, 'Computer Science', 'Introduction to networking protocols, the OSI model, and Internet architecture.'),
(108, 'CPSC350', 'Software Engineering', 3, 'Computer Science', 'Examines the software development lifecycle, including design, testing, and project management.'),
(109, 'CPSC495', 'Artificial Intelligence Capstone', 4, 'Computer Science', 'Team-based project integrating machine learning and AI applications to solve real-world problems.'),
(110, 'CPSC211L', 'Data Structures Lab', 1, 'Computer Science', 'Hands-on implementation and performance testing of data structures using C++.'),

-- Biology
(201, 'BIO101', 'General Biology I', 3, 'Biology', 'Fundamental principles of biology including cell structure, genetics, and evolution.'),
(202, 'BIO201', 'Genetics', 3, 'Biology', 'Inheritance patterns, DNA structure, and molecular mechanisms of gene expression.'),
(203, 'BIO202', 'Microbiology', 4, 'Biology', 'Study of microorganisms including bacteria, viruses, and fungi with emphasis on human health.'),
(204, 'BIO301', 'Cell Biology', 3, 'Biology', 'Explores organelles, membranes, and molecular mechanisms controlling cellular function.'),
(205, 'BIO302', 'Ecology', 3, 'Biology', 'Relationships between organisms and their environments, focusing on ecosystems and biodiversity.'),
(206, 'BIO401', 'Molecular Biology', 4, 'Biology', 'Advanced exploration of DNA replication, transcription, and protein synthesis regulation.'),
(207, 'BIO405', 'Immunology', 3, 'Biology', 'Study of immune system components and mechanisms in health and disease.'),
(208, 'BIO111L', 'General Biology Lab I', 1, 'Biology', 'Experimental techniques in cell biology, microscopy, and molecular analysis.'),
(209, 'BIO301L', 'Cell Biology Lab', 1, 'Biology', 'Lab experience in cell fractionation, enzyme assays, and microscopy.'),

-- Chemistry
(301, 'CHEM101', 'General Chemistry I', 4, 'Chemistry', 'Principles of atomic structure, bonding, stoichiometry, and chemical reactions.'),
(302, 'CHEM102', 'General Chemistry II', 4, 'Chemistry', 'Continuation of CHEM101 with focus on thermodynamics, kinetics, and equilibrium.'),
(303, 'CHEM201', 'Organic Chemistry I', 4, 'Chemistry', 'Introduction to structure, nomenclature, and reactions of carbon-based compounds.'),
(304, 'CHEM202', 'Organic Chemistry II', 4, 'Chemistry', 'Advanced study of reaction mechanisms and multi-step organic synthesis.'),
(305, 'CHEM301', 'Analytical Chemistry', 3, 'Chemistry', 'Quantitative analysis techniques including titration, spectroscopy, and chromatography.'),
(306, 'CHEM401', 'Physical Chemistry', 4, 'Chemistry', 'Thermodynamics, quantum mechanics, and molecular spectroscopy.'),
(307, 'CHEM450', 'Biochemistry', 3, 'Chemistry', 'Chemical processes within and related to living organisms.'),
(308, 'CHEM101L', 'General Chemistry Lab I', 1, 'Chemistry', 'Laboratory experiments on chemical reactions, stoichiometry, and solution chemistry.'),
(309, 'CHEM201L', 'Organic Chemistry Lab I', 1, 'Chemistry', 'Hands-on organic synthesis, purification, and spectroscopy.'),

-- Mathematics
(401, 'MATH101', 'Calculus I', 4, 'Mathematics', 'Differential calculus with applications to physical and social sciences.'),
(402, 'MATH102', 'Calculus II', 4, 'Mathematics', 'Integral calculus, sequences, and series.'),
(403, 'MATH201', 'Linear Algebra', 3, 'Mathematics', 'Vector spaces, matrices, eigenvalues, and linear transformations.'),
(404, 'MATH301', 'Probability and Statistics', 3, 'Mathematics', 'Probability distributions, hypothesis testing, and regression analysis.'),
(405, 'MATH401', 'Numerical Analysis', 3, 'Mathematics', 'Numerical solutions for equations, interpolation, and approximation methods.'),
(406, 'MATH410', 'Abstract Algebra', 3, 'Mathematics', 'Study of groups, rings, and fields.'),
(407, 'MATH420', 'Real Analysis', 3, 'Mathematics', 'Rigorous study of limits, continuity, and convergence.'),
(408, 'MATH499', 'Mathematics Seminar', 1, 'Mathematics', 'Weekly discussion and presentation of advanced mathematical topics.'),

-- Physics
(501, 'PHYS101', 'General Physics I', 4, 'Physics', 'Mechanics, motion, and energy with applications to engineering and science.'),
(502, 'PHYS102', 'General Physics II', 4, 'Physics', 'Electricity, magnetism, and wave phenomena.'),
(503, 'PHYS201', 'Modern Physics', 3, 'Physics', 'Introduction to relativity and quantum theory.'),
(504, 'PHYS301', 'Thermodynamics', 3, 'Physics', 'Study of heat, work, and the laws governing energy transformations.'),
(505, 'PHYS401', 'Quantum Mechanics', 4, 'Physics', 'Wave-particle duality, Schrödinger equation, and quantum systems.'),
(506, 'PHYS101L', 'General Physics Lab I', 1, 'Physics', 'Experiments on kinematics, forces, and conservation laws.'),
(507, 'PHYS201L', 'Modern Physics Lab', 1, 'Physics', 'Lab experiments in atomic spectra and radioactive decay.'),

-- Economics
(601, 'ECON101', 'Principles of Microeconomics', 3, 'Economics', 'Study of supply, demand, and market equilibrium at the individual level.'),
(602, 'ECON102', 'Principles of Macroeconomics', 3, 'Economics', 'National income, inflation, unemployment, and fiscal policy.'),
(603, 'ECON201', 'Intermediate Microeconomics', 3, 'Economics', 'Consumer theory, production, and market structures.'),
(604, 'ECON301', 'Econometrics', 4, 'Economics', 'Application of statistical methods to economic data and hypothesis testing.'),
(605, 'ECON401', 'International Economics', 3, 'Economics', 'Trade theory, exchange rates, and globalization.'),
(606, 'ECON410', 'Financial Economics', 3, 'Economics', 'Asset pricing, risk management, and market efficiency.'),

-- Psychology
(701, 'PSYC101', 'Introduction to Psychology', 3, 'Psychology', 'Overview of psychological principles, human behavior, and mental processes.'),
(702, 'PSYC201', 'Cognitive Psychology', 3, 'Psychology', 'Study of perception, memory, language, and problem-solving.'),
(703, 'PSYC301', 'Abnormal Psychology', 3, 'Psychology', 'Examination of psychological disorders and treatment approaches.'),
(704, 'PSYC310', 'Developmental Psychology', 3, 'Psychology', 'Psychological development from infancy through adulthood.'),
(705, 'PSYC401', 'Neuropsychology', 3, 'Psychology', 'Relationship between brain function and behavior.'),
(706, 'PSYC495', 'Senior Research Seminar', 1, 'Psychology', 'Capstone research project involving experimental design and analysis.');


-- Sections
INSERT INTO Section (section_num, course_id, instructor, Capacity, Registered, Waitlist) VALUES
-- Computer Science
(1, 101, 'Dr. Smith', 31, 29, 0),
(2, 101, 'Dr. Johnson', 32, 27, 0),
(1, 102, 'Prof. Martinez', 40, 40, 2),
(2, 102, 'Dr. Allen', 35, 34, 1),
(1, 103, 'Dr. Paige', 37, 31, 0),
(2, 103, 'Dr. Kaur', 36, 36, 3),
(1, 104, 'Dr. Lee', 30, 28, 0),
(2, 104, 'Dr. Morgan', 28, 26, 0),
(1, 105, 'Prof. Taylor', 33, 32, 1),
(2, 105, 'Dr. Ahmed', 32, 30, 0),
(1, 106, 'Dr. Brown', 35, 34, 0),
(2, 106, 'Dr. Green', 36, 35, 0),
(1, 107, 'Dr. Clark', 30, 29, 0),
(2, 107, 'Dr. Davis', 31, 31, 1),
(1, 108, 'Dr. Wilson', 28, 27, 0),
(2, 108, 'Dr. White', 29, 28, 0),
(1, 109, 'Dr. Harris', 25, 24, 0),
(2, 109, 'Prof. Robinson', 26, 25, 0),
(1, 110, 'Dr. Young', 20, 18, 0),

-- Biology
(1, 201, 'Dr. Chen', 38, 32, 0),
(2, 201, 'Dr. Li', 35, 33, 1),
(1, 202, 'Dr. Viktor', 36, 35, 0),
(2, 202, 'Dr. Zhao', 34, 32, 0),
(1, 203, 'Dr. Allen', 30, 28, 0),
(2, 203, 'Dr. Patel', 32, 31, 0),
(1, 204, 'Dr. Nguyen', 33, 30, 0),
(2, 204, 'Dr. Lopez', 34, 33, 0),
(1, 205, 'Dr. Roberts', 28, 27, 0),
(2, 205, 'Dr. Clark', 29, 28, 0),
(1, 206, 'Dr. Stewart', 30, 28, 0),
(2, 206, 'Dr. Adams', 31, 29, 0),
(1, 207, 'Dr. Simmons', 27, 26, 0),
(2, 207, 'Dr. Ramirez', 28, 27, 0),
(1, 208, 'Dr. Kim', 20, 18, 0),
(1, 209, 'Dr. Thompson', 18, 16, 0),

-- Chemistry
(1, 301, 'Dr. Perez', 36, 34, 0),
(2, 301, 'Dr. Scott', 35, 33, 0),
(1, 302, 'Dr. Baker', 38, 35, 1),
(2, 302, 'Dr. Rivera', 36, 34, 0),
(1, 303, 'Dr. Murphy', 32, 30, 0),
(2, 303, 'Dr. Foster', 30, 29, 0),
(1, 304, 'Dr. Jenkins', 28, 27, 0),
(2, 304, 'Dr. Sanders', 29, 28, 0),
(1, 305, 'Dr. Long', 33, 32, 0),
(2, 305, 'Dr. Hughes', 34, 33, 0),
(1, 306, 'Dr. Price', 25, 24, 0),
(2, 306, 'Dr. Patterson', 26, 25, 0),
(1, 307, 'Dr. Bell', 28, 27, 0),
(2, 307, 'Dr. Coleman', 29, 28, 0),
(1, 308, 'Dr. Kelly', 18, 17, 0),
(1, 309, 'Dr. Howard', 16, 15, 0),

-- Mathematics
(1, 401, 'Dr. Ramirez', 40, 38, 0),
(2, 401, 'Dr. Torres', 38, 36, 0),
(1, 402, 'Dr. Morgan', 35, 33, 0),
(2, 402, 'Dr. Sanders', 36, 34, 0),
(1, 403, 'Dr. Perry', 32, 30, 0),
(2, 403, 'Dr. Watson', 33, 31, 0),
(1, 404, 'Dr. Boyd', 30, 28, 0),
(2, 404, 'Dr. Gray', 31, 29, 0),
(1, 405, 'Dr. Murray', 28, 27, 0),
(2, 405, 'Dr. Webb', 29, 28, 0),
(1, 406, 'Dr. Porter', 25, 24, 0),
(2, 406, 'Dr. Jenkins', 26, 25, 0),
(1, 407, 'Dr. Newman', 28, 27, 0),
(2, 407, 'Dr. Cooper', 29, 28, 0),
(1, 408, 'Dr. Hughes', 20, 18, 0),

-- Physics
(1, 501, 'Dr. Riley', 36, 34, 0),
(2, 501, 'Dr. Reed', 35, 33, 0),
(1, 502, 'Dr. Perry', 38, 36, 0),
(2, 502, 'Dr. Simmons', 37, 35, 0),
(1, 503, 'Dr. Cox', 32, 30, 0),
(2, 503, 'Dr. Howard', 33, 31, 0),
(1, 504, 'Dr. Ward', 28, 27, 0),
(2, 504, 'Dr. Foster', 29, 28, 0),
(1, 505, 'Dr. Coleman', 25, 24, 0),
(2, 505, 'Dr. Powell', 26, 25, 0),
(1, 506, 'Dr. Gray', 18, 17, 0),
(1, 507, 'Dr. Bell', 16, 15, 0),

-- Economics
(1, 601, 'Dr. Bryant', 40, 38, 0),
(2, 601, 'Dr. Brooks', 38, 36, 0),
(1, 602, 'Dr. Knight', 35, 33, 0),
(2, 602, 'Dr. Spencer', 36, 34, 0),
(1, 603, 'Dr. Hamilton', 32, 30, 0),
(2, 603, 'Dr. Fisher', 33, 31, 0),
(1, 604, 'Dr. Arnold', 28, 27, 0),
(2, 604, 'Dr. Hamilton', 29, 28, 0),
(1, 605, 'Dr. Chapman', 25, 24, 0),
(2, 605, 'Dr. Barber', 26, 25, 0),
(1, 606, 'Dr. Hopkins', 28, 27, 0),
(2, 606, 'Dr. Francis', 29, 28, 0),

-- Psychology
(1, 701, 'Dr. Hamilton', 36, 34, 0),
(2, 701, 'Dr. Ellis', 35, 33, 0),
(1, 702, 'Dr. Simmons', 32, 30, 0),
(2, 702, 'Dr. Martin', 33, 31, 0),
(1, 703, 'Dr. Brooks', 28, 27, 0),
(2, 703, 'Dr. Perry', 29, 28, 0),
(1, 704, 'Dr. Jenkins', 25, 24, 0),
(2, 704, 'Dr. Cooper', 26, 25, 0),
(1, 705, 'Dr. Long', 28, 27, 0),
(2, 705, 'Dr. Bailey', 29, 28, 0),
(1, 706, 'Dr. Hughes', 20, 18, 0);


-- Users
INSERT INTO "User" (username, Email, Hashed_Pw, Degree) VALUES
('Alice Johnson', 'temp1@gmail.com', 'test1',2),
('Bob Williams', 'temp2@gmail.com', 'test2',1),
('Carol Smith', 'temp3@gmail.com', 'test3',3),
('David Martinez', 'temp4@gmail.com', 'test4',1),
('Edwin Shum', 'a@csu.fullerton.edu', 'test5',2);

-- Prerequisites
INSERT INTO Prerequisites (prereq_id, course_id) VALUES
(101, 102),
(102, 103),
(103, 104),
(110, 103),
(201, 202),
(208, 202),
(202, 203),
(203, 204),
(204, 209),
(301, 302),
(302, 303),
(303, 304),
(303, 309),
(401, 402),
(403, 404),
(501, 502),
(502, 503),
(503, 507),
(601, 603),
(604, 606),
(701, 702),
(702, 703),
(703, 705),
(705, 706);


INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
(1, 101, "Core-Lower"),
(1, 102, "Core-Lower"),
(1, 103, "Core-Upper"),
(1, 104, "Core-Upper");

INSERT INTO GE_Requirements (Degree_ID, A_CR, B_CR, C_CR, D_CR, E_CR, F_CR) VALUES
(1, 6, 12, 9, 6, 0, 3),
(2, 9, 3, 6, 7, 7, 3),
(3, 6, 12, 9, 6, 0, 3);

-- Degree Requirements
INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
-- Computer Science B.S. (Degree_ID = 1)
(1, 101, 'lower'),
(1, 102, 'lower'),
(1, 103, 'upper'),
(1, 104, 'upper'),
(1, 105, 'upper'),
(1, 106, 'upper'),
(1, 108, 'upper'),
(1, 109, 'upper'),
(1, 110, 'lower'),
(1, 107, 'elective'),

-- Biology B.S. (Degree_ID = 2)
(2, 201, 'lower'),
(2, 202, 'lower'),
(2, 203, 'upper'),
(2, 204, 'upper'),
(2, 205, 'upper'),
(2, 206, 'upper'),
(2, 207, 'upper'),
(2, 208, 'lower'),
(2, 209, 'upper'),
(2, 302, 'elective'),

-- Chemistry B.S. (Degree_ID = 3)
(3, 301, 'lower'),
(3, 302, 'lower'),
(3, 303, 'upper'),
(3, 304, 'upper'),
(3, 305, 'upper'),
(3, 306, 'upper'),
(3, 307, 'upper'),
(3, 308, 'lower'),
(3, 309, 'upper'),
(3, 405, 'elective'),

-- Mathematics B.S. (Degree_ID = 4)
(4, 401, 'lower'),
(4, 402, 'lower'),
(4, 403, 'lower'),
(4, 404, 'upper'),
(4, 405, 'upper'),
(4, 406, 'upper'),
(4, 407, 'upper'),
(4, 408, 'upper'),
(4, 505, 'elective'),

-- Physics B.S. (Degree_ID = 5)
(5, 501, 'lower'),
(5, 502, 'lower'),
(5, 503, 'upper'),
(5, 504, 'upper'),
(5, 505, 'upper'),
(5, 506, 'lower'),
(5, 507, 'upper'),
(5, 406, 'elective'),

-- Economics B.A. (Degree_ID = 6)
(6, 601, 'lower'),
(6, 602, 'lower'),
(6, 603, 'upper'),
(6, 604, 'upper'),
(6, 605, 'upper'),
(6, 606, 'upper'),
(6, 404, 'elective'),
(6, 403, 'elective'),

-- Psychology B.A. (Degree_ID = 7)
(7, 701, 'lower'),
(7, 702, 'upper'),
(7, 703, 'upper'),
(7, 704, 'upper'),
(7, 705, 'upper'),
(7, 706, 'upper'),
(7, 404, 'elective'),
(7, 201, 'elective');

INSERT INTO Taken (User_ID, Course_ID, Status) VALUES
(5, 201, 'taken'),
(5, 202, 'taken'),
(5, 208, 'taken'),
(5, 301, 'taken'),
(5, 302, 'taken'),
(5, 401, 'taken'),
(5, 404, 'taken'),
(5, 203, 'in-progress'),
(5, 204, 'in-progress'),
(5, 209, 'in-progress'),
(5, 303, 'in-progress'),
(5, 305, 'in-progress'),
(5, 205, 'wishlist'),
(5, 304, 'wishlist'),
(5, 307, 'wishlist'),
(5, 505, 'wishlist');
