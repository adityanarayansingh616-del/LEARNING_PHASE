--To consider a table EMPLOYEE and perform DML operations on it!
USE PRACTICE;
INSERT INTO EMPLOYEE VALUES(101,'Aman','Sales',45000,'Delhi'),(102,'Riya','HR',52000,'Patna'),(103,'Raj','Sales',38000,'Ranchi'),
(104,'Neha','IT',65000,'Delhi');
Update EMPLOYEE
SET Salary=Salary+5000
WHERE Department='Sales';
UPDATE EMPLOYEE
SET City='Ranchi'
Where EmpID=102;
DELETE FROM EMPLOYEE
WHERE Salary<40000;
DELETE FROM EMPLOYEE;