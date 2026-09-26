--To create a table then perform DML and DDL(DROP) on it!
USE PRACTICE;
CREATE TABLE STUDENT
(RollNo INT PRIMARY KEY,Name VARCHAR(30) NOT NULL,Class INT NOT NULL,Marks FLOAT,City VARCHAR(15) NOT NULL);
INSERT INTO STUDENT VALUES(07,'A',12,99,'Ranchi'),(08,'B',11,98,'Q'),(09,'c',10,97,'w'),(10,'u',9,87,'e'),(12,'p',8,95,'o');
UPDATE student
SET Marks=Marks+5
Where Class=12;
Update STUDENT
SET City='Ranchi'
WHERE Name='Aman';
DELETE from STUDENT
WHERE Marks<33;
DELETE FROM STUDENT;
DROP TABLE STUDENT;