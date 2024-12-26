# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).


# Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

 

# Example 1:


# Input: img = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[0,0,0],[0,0,0],[0,0,0]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0

from math import floor
from typing import List, Optional


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        # construct new matrix
        matrix = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]

        def get_avg_floor(i, j):
            results = []
            for i_ in range(i - 1, i + 2):
                for j_ in range(j - 1, j + 2):
                    if (val := get_number_safe(i_, j_)) is not None:
                        results.append(val)
            res = floor(sum(results) / len(results))
            matrix[i][j] = res

        def get_number_safe(i, j) -> Optional[int]:
            if i < 0 or j < 0 or i > len(img) - 1 or j > len(img[0]) - 1:
                return None
            return img[i][j]
        
        for i_ in range(len(img)):
            for j_ in range(len(img[0])):
                get_avg_floor(i_, j_)

        return matrix

print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))