# Definition for a binary tree node.
from typing import List, Optional
from _783_min_diff_bst import insert_into_bst, build_bst

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def traversal(node: TreeNode, level = 0, levels: list[list] = []):
            if node is None:
                return 
            if level > len(levels) - 1:
                levels.append([])
            levels[level].append(node.val)
            traversal(node.left, level + 1, levels)
            traversal(node.right, level + 1, levels)

        levels = [[]]
        traversal(root, 0, levels)

        return list(map(lambda l: sum(l) / len(l), levels))



print(Solution().averageOfLevels(build_bst([3,9,20,None,None,15,7])))