# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


from collections import defaultdict
from typing import Dict, List, Set


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Naive
        # d: Dict[Set, List] = {}
        # for string in strs:
        #     sorted_ = tuple(sorted(list(string)))
        #     if sorted_ in d:
        #         d[sorted_].append(string)
        #     else:
        #         d[sorted_] = [string]

        # print(d)

        # return [v for v in d.values()]
        # Use defaultdict to store lists of anagrams
        anagrams = defaultdict(list)
        
        for string in strs:
            # Create a character count tuple as the key
            char_count = [0] * 26  # Assuming only lowercase 'a' to 'z'
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            
            # Use the tuple of counts as the key
            anagrams[tuple(char_count)].append(string)
        
        # Return the grouped anagrams
        return list(anagrams.values())
    

print(Solution().groupAnagrams(strs = ["ddddddddddg","dgggggggggg"]))