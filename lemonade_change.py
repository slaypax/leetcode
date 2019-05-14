# https://leetcode.com/problems/lemonade-change/submissions/
# Runtime: 48 ms, faster than 92.30% of Python3 online submissions for Lemonade Change.
# https://leetcode.com/submissions/detail/228768048/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_dict = {
            '5': 0,
            '10': 0,
            '20': 0
        }
        
        for bill in bills:
            if bill == 5:
                bills_dict['5'] += 1
            elif bill == 10:
                if bills_dict['5'] == 0:
                    return False
                bills_dict['10'] += 1
                bills_dict['5'] -= 1

            else:
                bills_dict['20'] += 1
                if bills_dict['5'] >= 1 and bills_dict['10'] >= 1:
                    bills_dict['5'] -= 1
                    bills_dict['10'] -= 1
                elif bills_dict['5'] >= 3:
                    bills_dict['5'] -= 3
                else:
                    return False
        return True
        