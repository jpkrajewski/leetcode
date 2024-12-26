# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

 

# Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        START_COLOR = image[sr][sc]
        if START_COLOR == color:
            return image

        def dfs(image, sr, sc):
            if sr < 0 or sc < 0 or sr == len(image) or sc == len(image[0]) or image[sr][sc] != START_COLOR:
                return
            image[sr][sc] = color
            dfs(image, sr + 1, sc)
            dfs(image, sr - 1, sc)
            dfs(image, sr, sc + 1)
            dfs(image, sr, sc - 1)
            return

        dfs(image, sr, sc)
        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(Solution().floodFill(image, sr, sc, color))

out =  [[2,2,2],[2,2,0],[2,0,1]]