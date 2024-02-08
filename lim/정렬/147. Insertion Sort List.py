'''
이게 맞나?
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        node = head
        while node != None:
            nodes.append(node)
            node = node.next
        
        for i in range(len(nodes)):
            for j in range(i-1, -1, -1):
                picked_node = nodes[j+1]
                target_node = nodes[j]
                if target_node.val > picked_node.val:
                    nodes[j+1] = target_node
                    nodes[j] = picked_node
                else:
                    continue
        
        nodes.append(None)
        head = nodes[0]
        for i, node in enumerate(nodes[:-1]):
            node.next = nodes[i+1]
        return head

node = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
Solution().insertionSortList(node)