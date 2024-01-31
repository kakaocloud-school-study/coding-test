from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        def dfs(node):
            if node == None:
                return 0
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            if abs(left_length - right_length) > 1:
                self.answer = False
            return max(left_length, right_length) + 1
        dfs(root)
        return self.answer