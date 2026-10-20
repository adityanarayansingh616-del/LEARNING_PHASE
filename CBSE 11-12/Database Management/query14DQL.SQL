--To test Cartesian Product and Equi-Join on two tables!(Table aliasing too)
CREATE TABLE STUDENT(StudentID INT PRIMARY KEY, Name VARCHAR(30) NOT NULL, CourseID VARCHAR(5) REFERENCES COURSE(CourseID));
CREATE TABLE COURSE(CourseID VARCHAR(5) PRIMARY KEY, CourseName VARCHAR(25));
INSERT INTO COURSE (CourseID, CourseName) VALUES
('C01', 'Computer Science'),
('C02', 'Mathematics'),
('C03', 'Physics');
INSERT INTO STUDENT (StudentID, Name, CourseID) VALUES
(101, 'Aman', 'C01'),
(102, 'Riya', 'C02'),
(103, 'Raj', 'C01'),
(104, 'Neha', 'C03');
SELECT * FROM STUDENT,COURSE;--Cartesian Product of two relations/tables!
SELECT Name,CourseName FROM STUDENT,COURSE;--Equi-Join of two tables!
SELECT * FROM STUDENT,COURSE
WHERE STUDENT.CourseID=COURSE.CourseID;
SELECT StudentID,Name,CourseName FROM STUDENT S,COURSE AS C
WHERE S.CourseID=C.CourseID;
SELECT * FROM STUDENT AS S,COURSE C
WHERE S.CourseID=C.CourseID AND CourseName='Computer Science';
SELECT * FROM STUDENT S,COURSE C
WHERE S.CourseID=C.CourseID AND Name LIKE 'A%';