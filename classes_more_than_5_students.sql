/*
https://leetcode.com/problems/classes-more-than-5-students/submissions/
Runtime: 174 ms, faster than 98.32% of MySQL online submissions for Classes More Than 5 Students.ß
*/
SELECT class FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;