/*
https://leetcode.com/problems/triangle-judgement/

a + b > c
a + c > b
b + c > a

Runtime: 142 ms, faster than 97.25% of MySQL online submissions for Triangle Judgement.

*/


SELECT x, y, z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS 'triangle'
FROM triangle;