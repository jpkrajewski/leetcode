# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

 

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:

# Input: left = 47, right = 85
# Output: [48,55,66,77]
 

# Constraints:

# 1 <= left <= right <= 10^4


from operator import is_
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for n in range(left, right + 1):
            num = n 
            is_self_div = True
            while num > 0 and is_self_div:
                dig = num % 10
                if dig == 0:
                    is_self_div = False
                    break
                num //= 10
                if n % dig != 0:
                    is_self_div = False
            if is_self_div:
                result.append(n)

        return result
    


print(Solution().selfDividingNumbers(47, 85))

