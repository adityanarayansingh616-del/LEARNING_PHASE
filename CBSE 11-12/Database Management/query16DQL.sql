-- To perform Equi-Join on two tables!
SELECT Name,CourseName FROM STUDENT,COURSE
WHERE STUDENT.CourseID=COURSE.CourseID;
SELECT Name,CourseName,TeacherName FROM STUDENT S, COURSE AS C, TEACHER T
WHERE S.CourseID=C.CourseID AND C.TeacherID=T.TeacherID;
SELECT * FROM STUDENT,COURSE,TEACHER
WHERE CourseName='Computer Science' AND STUDENT.CourseID=COURSE.CourseID and COURSE.TeacherID=TEACHER.TeacherID;
SELECT * FROM STUDENT S,COURSE C,TEACHER T
WHERE Name Like 'A%' AND S.CourseID=C.CourseID And C.TeacherID=T.TeacherID
ORDER BY Name;