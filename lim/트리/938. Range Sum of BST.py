# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        range_sum = 0
        if (root.val >= low) and (root.val <= high):
            range_sum = root.val
        if root.val >= low:
            range_sum += self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            range_sum += self.rangeSumBST(root.right, low, high)
        return range_sum