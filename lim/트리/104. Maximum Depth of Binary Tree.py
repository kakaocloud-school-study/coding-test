from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(node: TreeNode):
            if node == None: # 루트 노트가 None인 경우도 테케에 존재...
                return 0
            dq = deque([(node, 1)])
            while len(dq):
                node, depth = dq.popleft()
                left_node = node.left
                if left_node != None:
                    dq.append((left_node, depth + 1))
                right_node = node.right
                if right_node != None:
                    dq.append((right_node, depth + 1))
            return depth
        return bfs(root)