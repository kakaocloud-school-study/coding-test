'''
재귀적으로 왼쪽 서브트리와 오른쪽 서브트리 각각에서 최대 깊이를 구하고 좌우를 비교하여 자신의 최대 깊이를 구한다.
좌우의 최대 깊이를 구할 때 좌우 최대 깊이 각각의 합이 곧 해당 노드에서의 최대 지름이다.
루트 노드에서부터 해당 알고리즘을 재귀적으로 실행해가며 전체 실행 과정에서 등장하는 지름 중에서 최대 지름을 구한다.
'''

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_diameter
        max_diameter = 0
        def dfs(node: TreeNode):
            if node == None:
                return 0
            left_length = dfs(node.left) # 좌 최대 깊이
            right_length = dfs(node.right) # 우 최대 깊이
            diameter = left_length + right_length # 방문 노드를 서브 트리로 했을 때의 최대 지름
            global max_diameter
            max_diameter = max(max_diameter, diameter) # 최대 지름 갱신
            return max(left_length, right_length) + 1 # 좌우 최대 깊이 중에서 가장 긴 길이에 +1한 것이 해당 서브트리 최대 깊이
        dfs(root)
        return max_diameter