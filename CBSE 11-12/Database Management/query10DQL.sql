--To create a table, insert values and then perform SQL-DQL data querying!
Use PRACTICE;
CREATE TABLE RESULT(RollNo INT PRIMARY KEY,Name VARCHAR(20) NOT NULL,Subject VARCHAR(20),Marks FLOAT,Section VARCHAR(3),City VARCHAR(15) NOT NULL);
INSERT INTO RESULT VALUES
(101, 'Aarav', 'Computer Science', 92, 'A', 'Ranchi'),
(102, 'Priya', 'Mathematics', 85, 'B', 'Delhi'),
(103, 'Rahul', 'Physics', 76, 'A', 'Ranchi'),
(104, 'Ananya', 'Computer Science', 92, 'B', 'Patna'),
(105, 'Karan', 'Chemistry', 68, 'A', 'Delhi'),
(106, 'Sneha', 'Mathematics', 88, 'B', 'Mumbai'),
(107, 'Arjun', 'Physics', 55, 'A', 'Patna'),
(108, 'Ishita', 'Computer Science', 76, 'A', 'Ranchi'),
(109, 'Rohan', 'Chemistry', 95, 'B', 'Mumbai'),
(110, 'Meera', 'Mathematics', 85, 'A', 'Delhi');
SELECT Name,Marks FROM result
WHERE Marks>75;
SELECT DISTINCT Section FROM RESULT
ORDER BY Section;
SELECT * FROM result
WHERE Section in('A','B','C');
SELECT * FROM result
WHERE Marks BETWEEN 60 AND 90;
SELECT * FROM result
WHERE Name LIKE '%n';
SELECT * FROM result
WHERE City LIKE 'R%';
SELECT Name StudentName,Marks AS Score FROM RESULT;
SELECT * FROM result
WHERE Section IN('A','B') AND Marks BETWEEN 70 AND 95;
SELECT * FROM result
ORDER BY Marks,Name DESC;