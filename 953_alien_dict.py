# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.


from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_priority = {x[1]:26 - x[0] for x in enumerate(order)}
        print(order_priority)

        def is_order_correct(w1, w2, order_priority) -> bool:
            pointer = 0
            w1_len = len(w1)
            w2_len = len(w2)
            while w1_len > pointer and w2_len > pointer:
                c1 = w1[pointer]
                c2 = w2[pointer]
                if order_priority[c2] > order_priority[c1]:
                    return False
                elif c1 == c2:
                    pass
                else:
                    return True
                pointer += 1
            return w1_len <= w2_len
        
        for index in range(len(words) - 1):
            if not is_order_correct(words[index], words[index + 1], order_priority):
                return False
        return True




words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"


print(Solution().isAlienSorted(words=words, order=order))