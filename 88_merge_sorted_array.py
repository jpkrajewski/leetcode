from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # First
        # if m == 0:
        #     nums1[0] = nums2[0]
        # pos = len(nums1) - 1
        # p1 = m - 1
        # p2 = n - 1
        # while p1 != -1 and p2 != -1 and pos != -1:
        #     if nums1[p1] > nums2[p2]:
        #         nums1[pos] = nums1[p1]
        #         p1 -= 1
        #     elif nums2[p2] > nums1[p1]:
        #         nums1[pos] = nums2[p2]
        #         p2 -= 1
        #     else:
        #         nums1[pos] = nums2[p2]
        #         pos -= 1
        #         nums1[pos] = nums1[p1]
        #         p1 -= 1
        #         p2 -= 1
        #     pos -= 1

        # while p1 != -1 and pos != -1:
        #     nums1[pos] = nums1[p1]
        #     p1 -= 1
        #     pos -= 1

        # while p2 != -1 and pos != -1:
        #     nums1[pos] = nums2[p2]
        #     p2 -= 1
        #     pos -= 1

        p1 = m - 1
        p2 = n - 1
        pos = m + n - 1

         # Merge from the back
        while p2 >= 0:
            # If p1 is exhausted, or nums2[p2] is larger, place nums2[p2]
            if p1 < 0 or nums2[p2] >= nums1[p1]:
                nums1[pos] = nums2[p2]
                p2 -= 1
            else:
                # Otherwise, place nums1[p1]
                nums1[pos] = nums1[p1]
                p1 -= 1
            pos -= 1






nums1 = [0,0,3,0,0,0,0,0,0]
m = 3
nums2 = [-1,1,1,1,2,3]
n = 6


Solution().merge(nums1, m, nums2, n)
print(nums1)
assert nums1 == [-1,0,0,1,1,1,2,3,3]