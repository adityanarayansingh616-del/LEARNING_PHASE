--To perform DQL Aggregate functions and GROUPING/Elimination of rows(WHERE) or groups(HAVING) on a relation!
USE PRACTICE;
SELECT MAX(Marks) HighestMarks FROM RESULT;
SELECT MIN(Marks) AS Lowest_Marks FROM RESULT;
SELECT AVG(Marks) AS Average_Marks FROM RESULT;
SELECT SUM(Marks) TotalMarks FROM RESULT;
SELECT COUNT(*) Total_Students FROM RESULT;
SELECT Section, COUNT(*) AS TotalStudents FROM result
GROUP BY Section;
SELECT Section, AVG(Marks) Average_Marks FROM RESULT
GROUP BY Section;
SELECT Section FROM result
GROUP BY Section
HAVING AVG(Marks)>75;
SELECT Section FROM result
GROUP BY Section
HAVING COUNT(*)>=3;
SELECT Section, MAX(Marks) AS Highest_Marks, MIN(Marks) Lowest_Marks FROM result
GROUP BY Section;
SELECT Section, AVG(Marks) AverageMarks FROM result
WHERE Marks>=60
GROUP BY Section
HAVING AVG(Marks)>75;