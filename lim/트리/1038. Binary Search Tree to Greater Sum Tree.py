# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        num_2_greater_sum = dict()
        def get_greater_sum(node, num): # bst를 성질을 통해 특정 숫자보다 큰 수들의 합을 구한다.
            if node == None:
                return 0
            total = 0
            total += get_greater_sum(node.right, num)
            if num < node.val:
                total += get_greater_sum(node.left, num)
                total += node.val
            return total
        
        def record_sum(node): # 노드별로 get_greater_sum 결과값을 기록
            if node == None:
                return
            num_2_greater_sum[node.val] = get_greater_sum(root, node.val)
            record_sum(node.left)
            record_sum(node.right)
            
        def convert(node):
            if node == None: # 노드들의 값을 기록한 값으로 변경
                return
            node.val += num_2_greater_sum[node.val]
            convert(node.left)
            convert(node.right)
        
        record_sum(root)
        convert(root)
        return root