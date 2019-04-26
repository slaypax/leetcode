/* 
https://leetcode.com/problems/not-boring-movies
Runtime: 119 ms, faster than 88.83% of MySQL online submissions for Not Boring Movies.
*/

SELECT id, movie, description, rating
FROM cinema
WHERE description!='boring'
AND id % 2
ORDER BY rating DESC;