# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for r_c in ransomNote:
            if  r_c not in d:
                return False
            else:
                d[r_c] -= 1
                if d[r_c] < 0:
                    return False
        
        return True
    

print(Solution().canConstruct(ransomNote = "aa", magazine = "aab"))