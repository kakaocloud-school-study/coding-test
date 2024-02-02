# Definition for singly-linked list.
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hq = []
        node = head
        seq = 0
        while node != None:
            heapq.heappush(hq, (node.val, seq, node))
            node = node.next
            seq += 1
        
        head = None if len(hq) == 0 else hq[0][2]
        while len(hq):
            _, _, node = heapq.heappop(hq)
            if len(hq):
                node.next = hq[0][2]
            else:
                node.next = None
        return head