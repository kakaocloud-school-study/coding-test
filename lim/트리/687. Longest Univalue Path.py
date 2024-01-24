from typing import Optional, Self


class TreeNode:
    def __init__(self, val=0, left: Self=None, right: Self=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        global max_diameter
        max_diameter = 0
        def dfs(node: TreeNode):
            if node == None:
                return 0
            left_length = dfs(node.left) # 좌 최대 깊이
            right_length = dfs(node.right) # 우 최대 깊이            
            if (node.left == None) or (node.left.val != node.val): # 값 다른 서브 트리면 깊이 반영 안 함
                left_length = 0
            if (node.right == None) or (node.right.val != node.val): # 값 다른 서브 트리면 깊이 반영 안 함
                right_length = 0
            diameter = left_length + right_length # 방문 노드를 서브 트리로 했을 때의 최대 지름
            global max_diameter
            max_diameter = max(max_diameter, diameter) # 최대 지름 갱신
            return max(left_length, right_length) + 1 # 좌우 최대 깊이 중에서 가장 긴 길이에 +1한 것이 해당 서브트리 최대 깊이
        dfs(root)
        return max_diameter