from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left_d = 0
        right_d = 0
        if not root:
            return 0
        if root.left or root.right:
            left_d = self.maxDepth(root.left)
            right_d = self.maxDepth(root.right)
        return 1 + max(left_d, right_d)

