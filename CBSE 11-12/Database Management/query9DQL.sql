--To consider a table and then perform following commands/statements!
USE PRACTICE;
SELECT * FROM student
WHERE Marks is NULL;
SELECT * FROM student
WHERE Marks IS NOT NULL;
SELECT * FROM student
WHERE City is null;
SELECT * FROM student
WHERE Email is not NULL;
SELECT * FROM student
WHERE Marks BETWEEN 70 AND 90;
SELECT * FROM student
WHERE Name LIKE 'A%';
SELECT * FROM student
WHERE City IN('Delhi','Patna') and Marks IS NOT NULL;
SELECT * FROM student
ORDER BY Marks DESC;