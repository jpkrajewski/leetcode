# 128. Longest Consecutive Sequence
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        for n in num_set:  # Iterate over the set, not the list
            # Only start counting if n is the start of a sequence
            if n - 1 not in num_set:
                current_num = n
                current_streak = 1

                # Count the length of the current sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest sequence
                longest = max(longest, current_streak)

        return longest
    
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))