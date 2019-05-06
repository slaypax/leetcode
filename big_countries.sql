/*
https://leetcode.com/problems/big-countries/submissions/
Runtime: 188 ms, faster than 95.91% of MySQL online submissions for Big Countries.
*/
SELECT name, population, area
FROM World
WHERE population > 25000000 OR area > 3000000;