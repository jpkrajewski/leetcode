from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data, end=' ')
    printInorder(node.right)


def insert_into_bst(root: Optional[TreeNode], val: Optional[int]) -> TreeNode:
    """Helper function to insert a value into the BST."""
    if not val:
        return root
    if not root:  # If the tree/subtree is empty, create a new node
        return TreeNode(val)
    if val < root.val:  # Insert into the left subtree
        root.left = insert_into_bst(root.left, val)
    else:  # Insert into the right subtree
        root.right = insert_into_bst(root.right, val)
    return root

def build_bst(values: List[int]) -> Optional[TreeNode]:
    """Build a BST from a list of values."""
    if not values:  # If the input list is empty, return None
        return None
    root = None
    for val in values:
        root = insert_into_bst(root, val)  # Insert each value into the BST
    return root


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_ = float('inf')  # Initialize to infinity
        last = None

        def inorder_traversal(node):
            nonlocal min_, last
            if node is None:
                return
            inorder_traversal(node.left)
            if last is not None:
                min_ = min(min_, abs(node.val - last))
            last = node.val
            inorder_traversal(node.right)

        inorder_traversal(root)

        return min_


tree = build_bst([1,0,48,None,None,12,49])
print(Solution().minDiffInBST(tree))
