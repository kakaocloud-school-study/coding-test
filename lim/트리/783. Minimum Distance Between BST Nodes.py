'''
해시맵을 쓰면 쉽게 풀리지만 굳이 안쓰고 풀어보았다
'''

# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def foo(node): # 재귀적으로 서브 트리의 (최소값, 최소차, 최대값)을 구함
            if node == None:
                return (sys.maxsize, sys.maxsize, -sys.maxsize)
            left_min, left_min_diff, left_max = foo(node.left)
            right_min, right_min_diff, right_max = foo(node.right)
            return (
                min(left_min, node.val),
                min(left_min_diff, right_min_diff, abs(left_max - node.val), abs(right_min - node.val)),
                max(right_max, node.val),
            )
        _, diff, _ = foo(root)
        return diff