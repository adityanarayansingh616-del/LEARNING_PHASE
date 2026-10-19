--To test aggregate functions on a table!
USE PRACTICE;
SELECT MAX(Salary) AS HighestSalary FROM EMPLOYEE;
SELECT MIN(Salary) LowestSalary FROM EMPLOYEE;
SELECT AVG(Salary) Average_Salary FROM EMPLOYEE;
SELECT SUM(Salary) AS Total_Salary FROM EMPLOYEE;
SELECT COUNT(*) AS TotalEmployees FROM EMPLOYEE;
SELECT COUNT(Salary) TotalNotNullSalary FROM EMPLOYEE;
SELECT MAX(Salary) Max_IT_Salary FROM employee
WHERE Department='IT';
SELECT AVG(Salary) AS Delhi_Avg_Salary FROM employee
WHERE City='Delhi';
SELECT SUM(Salary) AS Total_HR_Salary FROM employee
WHERE Department='HR';
SELECT MAX(Salary) Highest_Salary,MIN(Salary) AS LowestSalary,AVG(Salary) AverageSalary FROM EMPLOYEE;