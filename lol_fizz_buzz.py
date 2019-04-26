# https://leetcode.com/problems/fizz-buzz/
# 
# Runtime: 56 ms, faster than 73.57% of Python3 online submissions for Fizz Buzz.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n +1):
            if i == 0:
                continue
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
                continue
            if i % 3 == 0:
                result.append("Fizz")
                continue
            if i % 5 == 0:
                result.append("Buzz")
                continue
            result.append(str(i))
        return result

# use a hash
# easier with lots of mappings 'maintainable'

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        fizzbuzz = {3 : 'Fizz', 5: 'Buzz'}
        
        for num in range (1, n + 1):
            ans = ''
            for key in fizzbuzz.keys():

                if num % key == 0:
                    ans += fizzbuzz[key]

            if not ans:
                ans = str(num)
            
            result.append(ans)
            
        return result