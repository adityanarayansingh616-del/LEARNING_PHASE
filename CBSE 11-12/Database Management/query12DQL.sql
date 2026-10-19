--To perform DQL Commands using Aggregate functions on a table!
USE PRACTICE;
SELECT Department,COUNT(*) Total_Employees FROM employee
GROUP BY Department;
SELECT Department,Sum(Salary) AS Total_Salary FROM employee
GROUP BY Department;
SELECT Department,avg(Salary) AS AverageSalary FROM employee
GROUP BY Department;
SELECT Department,MAX(Salary) HighestSalary FROM employee
GROUP BY Department;
SELECT Department,MIN(Salary) Lowest_Salary FROM employee
GROUP BY Department;
SELECT Department FROM employee
GROUP BY Department
HAVING COUNT(*)>1;
SELECT Department FROM employee
GROUP BY Department
HAVING AVG(Salary)>55000;
SELECT Department FROM employee
GROUP BY Department
Having SUM(Salary)>100000;