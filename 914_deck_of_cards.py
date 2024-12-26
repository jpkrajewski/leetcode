# You are given an integer array deck where deck[i] represents the number written on the ith card.

# Partition the cards into one or more groups such that:

# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.


from typing import List
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        card_count = {}

        for n in deck:
            if n in card_count:
                card_count[n] += 1
            else:
                card_count[n] = 1

        common_gcd = reduce(gcd, card_count.values())
        return common_gcd > 1

deck = [1,1,1,1,2,2,2,2,2,2]
print(Solution().hasGroupsSizeX(deck))