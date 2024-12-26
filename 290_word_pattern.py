# 290. Word Pattern
# Easy
# Topics
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false

 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d_pattern = {}
        d_s = {}
        words = s.split()
        for index in range(len(words)):
            if pattern[index] in d_pattern:
                if d_pattern[pattern[index]] != words[index]:
                    return False
            if words[index] in d_s:
                if d_s[words[index]] != pattern[index]:
                    return False
            else:
                d_pattern[pattern[index]] = words[index]
                d_s[words[index]] = pattern[index]
        return True

print(Solution().wordPattern(pattern = "abc", s = "b c a")) # true
print(Solution().wordPattern( pattern = "abba", s = "dog cat cat dog")) # true
print(Solution().wordPattern( pattern = "abba", s = "dog cat cat fish")) # false
print(Solution().wordPattern( pattern = "aaa", s = "dog dog dog")) # true
print(Solution().wordPattern( pattern = "aac", s = "dog dog dog")) # false