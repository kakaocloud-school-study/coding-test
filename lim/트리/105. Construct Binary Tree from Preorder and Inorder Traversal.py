'''
inorder에서는 루트 노드 좌측에는 다 좌측 서브트리 노드들이고 우측도 마찬가지다. 이를 통해 좌우 각각 서브트리의 노드 개수를 구할 수 있다
inorder = [(좌 서브트리 sub inorder), 루트노드, (우 서브트리 sub inorder)]
preorder = [루트노드, (좌 서브트리 sub preorder), (우 서브트리 sub preorder)]
위의 관계를 통해 문제를 작은 문제로 쪼개어 풀 수 있다.
'''

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        # 주어진 preorder, inorder로 트리의 루트 노드를 구한다.
        if len(preorder) == 0:
            return
        root_num = preorder[0]
        left_size = inorder.index(root_num)

        # 좌우 서브트리의 preorder, inorder를 구하여 재귀적으로 좌우 노드를 구한다.
        left = self.buildTree(preorder[1:left_size+1], inorder[:left_size])
        right = self.buildTree(preorder[left_size+1:], inorder[left_size+1:])

        # 좌우 노드를 잇고 루트 노드를 리턴한다.
        root = TreeNode(root_num)
        root.left = left
        root.right = right
        return root