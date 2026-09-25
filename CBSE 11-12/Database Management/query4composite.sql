--To create a table with composite primary key and then insert tuples with unique 3 value combinations to protect constraint rules. 
USE PRACTICE;
CREATE TABLE RESULT(StudentID INT,SubjectCode varchar(10),Semester INT,Marks INt,PRIMARY KEY(StudentID,SubjectCode,Semester));
INSERT INTO RESULT VALUES(0596,083,2027,100);
INSERT INTO RESULT VALUES(0596,067,2027,99);