
INSERT INTO Prerequisites (Course_ID, Prereq_ID) VALUES
(1002, 1001), -- Calc II requires Calc I
(1004, 1001), -- Physics I requires Calc I
(1005, 1004), -- Physics II requires Physics I
(1005, 1001), -- Physics II requires Calc I
(1007, 1001), -- Discrete Math requires Calc I
(1008, 1006), -- Data Structures requires Intro to Programming
(1008, 1007), -- Data Structures also requires Discrete Math
(1009, 1006), -- Computer Organization requires programming basics
(1010, 1006), -- Software Development Fundamentals requires Intro to Programming
(1011, 1006), -- Intro to Databases requires Intro to Programming
(1012, 1006), -- Networks requires programming basics
(1013, 1008), -- Algorithms requires Data Structures
(1014, 1008), -- Operating Systems requires Data Structures
(1015, 1006), -- Software Engineering requires Intro to Programming
(1016, 1011), -- Database Systems requires Intro to Databases
(1017, 1008), -- Computer Security requires Data Structures
(1018, 1013), -- ML Fundamentals requires Algorithms
(1019, 1006), -- HCI requires Intro to Programming
(1020, 1014), -- Capstone requires Operating Systems
(1020, 1015), -- Capstone also requires Software Engineering
(1021, 1008), -- Data Structures Lab requires Data Structures
(1022, 1014), -- Parallel & Distributed Computing requires OS
(1022, 1013), -- Also requires Algorithms
(1023, 1013), -- Computational Biology requires Algorithms
(1025, 1024), -- Digital Logic requires Intro
(1026, 1024), -- Data Structures requires Intro
(1027, 1025), -- Assembly requires Digital Logic
(1028, 1027), -- Embedded Systems I requires Assembly
(1029, 1025), -- Signals & Systems requires Digital Logic
(1030, 1025), -- Intro Electronics requires Digital Logic
(1031, 1026), -- Networks for Engineers requires Data Structures
(1032, 1026), -- OS for Engineers requires Data Structures
(1033, 1025), -- VLSI requires Digital Logic
(1034, 1027), -- Microprocessors requires Assembly
(1035, 1028), -- Embedded Systems II requires Embedded Systems I
(1036, 1028), -- Capstone I requires Embedded Systems I
(1037, 1036), -- Capstone II requires Capstone I
(1038, 1029), -- DSP requires Signals and Systems
(1039, 1028), -- Networked Embedded requires Embedded Systems I
(1040, 1033), -- FPGA Elective requires VLSI
(1041, 1028), -- Embedded Systems Lab requires Embedded Systems I
(1043, 1042), -- Circuit Analysis I requires Intro EE
(1044, 1043), -- Circuit Analysis II requires Circuit Analysis I
(1045, 1043), -- Electronics I requires Circuit Analysis I
(1046, 1002), -- Signals & Systems requires Calculus II
(1047, 1042), -- Digital Logic requires Intro EE
(1048, 1002), -- Electromagnetics requires Calculus II
(1049, 1043), -- Instrumentation requires Circuits I
(1050, 1046), -- Control Systems requires Systems & Signals
(1051, 1044), -- Power Systems requires Circuits II
(1053, 1045), -- Microelectronics requires Electronics I
(1054, 1045), -- Capstone I requires Electronics I
(1055, 1054), -- Capstone II requires Capstone I
(1056, 1046), -- Communication Systems requires Systems & Signals
(1057, 1051), -- Renewable Energy Elective requires Power Systems
(1058, 1043), -- Circuits Lab requires Circuits I
(1060, 1059), -- Statics requires Intro CEE
(1061, 1060), -- Mechanics of Materials requires Statics
(1062, 1059), -- Surveying requires Intro CEE
(1063, 1060), -- Hydraulics requires Statics
(1064, 1061), -- Structural Analysis I requires Mechanics of Materials
(1065, 1059), -- Environmental Engineering Fundamentals requires Intro CEE
(1066, 1059), -- Construction Materials requires Intro CEE
(1067, 1061), -- Geotechnical Engineering requires Mechanics of Materials
(1068, 1064), -- Structural Design requires Structural Analysis I
(1069, 1060), -- Transportation Engineering requires Statics
(1070, 1063), -- Water Resources requires Hydraulics
(1071, 1066), -- Capstone I requires Construction Materials
(1072, 1071), -- Capstone II requires Capstone I
(1074, 1066), -- Materials Lab requires Construction Materials
(2002, 2001), -- Organismal Biology requires Cell & Molecular Biology
(2004, 2001), -- Intro Biology Lab requires Cell & Molecular Biology
(2003, 2001), -- Biological Research Foundations requires Cell & Molecular Biology
(2006, 2005), -- General Chemistry II requires General Chemistry I
(2007, 1001), -- Applied Calculus for Life Sciences requires Calculus I
(2008, 1002), -- Statistics requires Calculus II
(2009, 2001), -- Genetics requires Cell & Molecular Biology
(2010, 2001), -- Microbiology requires Cell & Molecular Biology
(2011, 2002), -- Human Physiology requires Organismal Biology
(2012, 2002), -- Ecology requires Organismal Biology
(2013, 2002), -- Evolution requires Organismal Biology
(2014, 2003), -- Bioinformatics requires Biological Research Foundations
(2015, 2001), -- Advanced Cell Biology requires Cell & Molecular Biology
(2016, 2003), -- Senior Research Capstone requires Biological Research Foundations
(2016, 2004); -- Senior Research Capstone also requires Intro Biology Lab


INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
-- Computer Science (Degree_ID = 26)
(26, 1001, 'Core-Lower'),
(26, 1002, 'Core-Lower'),
(26, 1003, 'Core-Lower'),
(26, 1004, 'Core-Lower'),
(26, 1005, 'Core-Lower'),
(26, 1006, 'Core-Lower'),
(26, 1007, 'Core-Lower'),
(26, 1008, 'Core-Lower'),
(26, 1021, 'Core-Lower'),
(26, 1009, 'Core-Upper'),
(26, 1010, 'Core-Upper'),
(26, 1011, 'Core-Upper'),
(26, 1012, 'Core-Upper'),
(26, 1013, 'Core-Upper'),
(26, 1014, 'Core-Upper'),
(26, 1015, 'Core-Upper'),
(26, 1020, 'Core-Upper');
INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
-- Computer Engineering (Degree_id = 24)
(24, 1001, 'Core-Lower'),
(24, 1002, 'Core-Lower'),
(24, 1003, 'Core-Lower'),
(24, 1004, 'Core-Lower'),
(24, 1005, 'Core-Lower'),
(24, 1024, 'Core-Lower'),
(24, 1025, 'Core-Lower'),
(24, 1026, 'Core-Lower'),
(24, 1027, 'Core-Lower'),
(24, 1028, 'Core-Lower'),
(24, 1029, 'Core-Lower'),
(24, 1030, 'Core-Lower'),
(24, 1031, 'Core-Lower'),
(24, 1032, 'Core-Upper'),
(24, 1033, 'Core-Upper'),
(24, 1034, 'Core-Upper'),
(24, 1035, 'Core-Upper'),
(24, 1036, 'Core-Upper'),
(24, 1037, 'Core-Upper'),
(24, 1038, 'Core-Upper'),
(24, 1039, 'Core-Upper'),
(24, 1041, 'Core-Upper');

INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
-- Electrical Engineering
(29, 1001, 'Core-Lower'),
(29, 1002, 'Core-Lower'),
(29, 1003, 'Core-Lower'),
(29, 1004, 'Core-Lower'),
(29, 1005, 'Core-Lower'),
(29, 1042, 'Core-Lower'),
(29, 1043, 'Core-Lower'),
(29, 1047, 'Core-Lower'),
(29, 1044, 'Core-Upper'),
(29, 1045, 'Core-Upper'),
(29, 1046, 'Core-Upper'),
(29, 1048, 'Core-Upper'),
(29, 1049, 'Core-Upper'),
(29, 1050, 'Core-Upper'),
(29, 1051, 'Core-Upper'),
(29, 1053, 'Core-Upper'),
(29, 1054, 'Core-Upper'),
(29, 1055, 'Core-Upper'),
(29, 1056, 'Core-Upper'),
(29, 1058, 'Core-Upper');

INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
-- Civil Engineering
(22, 1001, 'Core-Lower'),
(22, 1002, 'Core-Lower'),
(22, 1003, 'Core-Lower'),
(22, 1004, 'Core-Lower'),
(22, 1005, 'Core-Lower'),
(22, 1059, 'Core-Lower'),
(22, 1060, 'Core-Lower'),
(22, 1061, 'Core-Lower'),
(22, 1062, 'Core-Upper'),
(22, 1063, 'Core-Upper'),
(22, 1064, 'Core-Upper'),
(22, 1065, 'Core-Upper'),
(22, 1066, 'Core-Upper'),
(22, 1067, 'Core-Upper'),
(22, 1068, 'Core-Upper'),
(22, 1069, 'Core-Upper'),
(22, 1070, 'Core-Upper'),
(22, 1071, 'Core-Upper'),
(22, 1072, 'Core-Upper'),
(22, 1074, 'Core-Upper');

INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
-- Mechanical Engineering
(30, 1001, 'Core-Lower'),
(30, 1002, 'Core-Lower'),
(30, 1003, 'Core-Lower'),
(30, 1004, 'Core-Lower'),
(30, 1005, 'Core-Lower'),
(30, 2001, 'Core-Lower'),
(30, 2002, 'Core-Lower'),
(30, 2003, 'Core-Lower'),
(30, 2004, 'Core-Lower'),
(30, 2005, 'Core-Lower'),
(30, 2006, 'Core-Lower'),
(30, 2007, 'Core-Lower'),
(30, 2008, 'Core-Lower'),
(30, 2009, 'Core-Upper'),
(30, 2010, 'Core-Upper'),
(30, 2011, 'Core-Upper'),
(30, 2012, 'Core-Upper'),
(30, 2013, 'Core-Upper'),
(30, 2014, 'Core-Upper'),
(30, 2015, 'Core-Upper'),
(30, 2016, 'Core-Upper');

INSERT INTO DG_Requirements (Degree_ID, Course, Type) VALUES
-- Biological Science
(76, 2001, 'Core-Lower'),
(76, 2002, 'Core-Lower'),
(76, 2003, 'Core-Lower'),
(76, 2004, 'Core-Lower'),
(76, 2005, 'Core-Lower'),
(76, 2006, 'Core-Lower'),
(76, 2007, 'Core-Lower'),
(76, 2008, 'Core-Lower'),
(76, 2009, 'Core-Upper'),
(76, 2010, 'Core-Upper'),
(76, 2011, 'Core-Upper'),
(76, 2012, 'Core-Upper'),
(76, 2013, 'Core-Upper'),
(76, 2014, 'Core-Upper'),
(76, 2015, 'Core-Upper'),
(76, 2016, 'Core-Upper');


INSERT INTO GE_Requirements (Degree_ID, A_CR, B_CR, C_CR, D_CR, E_CR, F_CR) VALUES
(1, 6, 12, 9, 6, 0, 3),
(2, 9, 3, 6, 7, 7, 3),
(3, 6, 12, 9, 6, 0, 3);