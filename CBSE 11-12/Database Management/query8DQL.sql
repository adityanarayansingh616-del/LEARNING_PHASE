--To consider a table/relation and perform following DQL queries on it!
USE PRACTICE;
SELECT * FROM EMPLOYEE;
SELECT Name,Department,Salary FRom employee;
SELECT Name FROM EMPLOYEE
WHERE Salary>60000;
SELECT * FROM employee
WHERE Department in ('HR','IT');
SELECT * FROM employee
WHERE Salary BETWEEN 50000 AND 80000;
SELECT * FROM employee
WHERE City IN ('Delhi','Patna','Ranchi');
SELECT * FROM employee
WHERE Name LIKE 'A%';
SELECT * FROM employee
WHERE Name LIKE '%an%';
SELECT DISTINCT City FROM employee;
SELECT Name as EmployeeName, Salary MonthlySalary From EMPLOYEE;
SELECT * FROM employee
ORDER BY Salary DESC;
SELECT * FROM employee
WHERE Department='IT' and Salary>=50000
ORDER BY Salary Desc;