from typing import List

# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

# 1 -> 2 = 2
# 4 -> 5 = 2

# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

# 1 -> 2 = 2
# 2 -> 3 = 2

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or duration == 0:
            return 0
        
        total_duration = 0
        
        for i in range(len(timeSeries) - 1):
            # Calculate the gap between consecutive attacks
            interval = timeSeries[i + 1] - timeSeries[i]
            
            # Add the minimum duration for this attack
            total_duration += min(interval, duration)
        
        # Add the duration for the last attack
        total_duration += duration
        
        return total_duration
    

timeSeries = [1,2]
duration = 2
out = 4

print(Solution().findPoisonedDuration(timeSeries, duration))

