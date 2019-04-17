# https://leetcode.com/problems/robot-return-to-origin/solution/
# Initially, the robot is at (x, y) = (0, 0). If the move is 'U', the robot
# goes to (x, y-1); if the move is 'R', the robot goes to (x, y) = (x+1, y),
# and so on.
# Input: "UD"
# Output: true 

# Your runtime beats 6.11 % of python3 submissions
# Runtime: 104 ms
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x= 0
        y = 0
        moves_list = [x for x in moves]
        for move in moves_list:
            if move == 'U':
                y += 1
            if move == 'D':
                y -= 1
            if move == 'R':
                x += 1
            if move == 'L':
                x -= 1
        return x == 0 and y == 0

# Runtime: 40 ms
# Your runtime beats 93.01 % of python3 submissions
# it uses buit ins and i cannot figure out how to 
# got faster with out them

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        