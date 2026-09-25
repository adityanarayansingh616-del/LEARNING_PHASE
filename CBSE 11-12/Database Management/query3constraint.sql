--To create a table and then showing examples to insert tuples/rows/records/values into it!
USE PRACTICE;
CREATE TABLE STUDENT(StudentID INT PRIMARY KEY,Name VARCHAR(40) NOT NULL,Email VARCHAR(50) UNIQUE,Marks FLOAT);
INSERT INTO STUDENT VALUES(0596,'Aditya Narayan Singh','adityanarayansingh616@gmail.com',100);--Valid data entry example!
INSERT INTO STUDENT VALUES(NULL,'Adam','adam@gmail.com',98);--primary key rule/constraint violation example!
INSERT INTO STUDENT VALUES(0597,nuLL,'null@gmail.com',99);--NOT NULL constraint/rule violation example!