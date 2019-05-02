/*
https://leetcode.com/problems/duplicate-emails/
Runtime: 181 ms, faster than 93.74% of MySQL online submissions for Duplicate Emails
*/

SELECT Email FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;