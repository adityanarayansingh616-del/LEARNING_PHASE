--To consider a table STUDENT and then perform DML Operations on it!
USE PRACTICE;
INSERT INTO STUDENT(Name,RollNo,Marks,Email) VALUES('Aditya Narayan Singh',07,100,'adityanarayansingh616@gmail.com'),('Adam',08,99,'adam@gmail.com'),
('Yoyo',54,96,'yoyo@gmail.com');
INSERT INTO STUDENT VALUES(07,'Toto','Toto@gmail.com',85);--Primary Key Violation example!
INSERT INTO STUDENT VALUES(09,NULL,'NULL@gmail.com',78);--NOT NULL Constraint Violation!
INSERT INTO STUDENT VALUES(69,'WAR','NULL@gmail.com',79);--UNIQUE Constraint Violation!
UPDATE STUDENT
SET Marks=Marks+10
WHERE Marks<50;
DELETE FROM STUDENT
WHERE Marks<40;