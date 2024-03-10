from typing import List

class Node:
    def __init__(self, val, idx, left = None, right = None):
        self.val = val
        self.idx = idx
        self.left = left
        self.right = right
        self.visited = False


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = [gas[i] - cost[i] for i in range(len(gas))]
        prev_sum = 0
        curr_sum = 0
        idx = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum < 0:
                prev_sum += curr_sum
                curr_sum = 0
                idx = i + 1
        if prev_sum + curr_sum < 0:
            return -1
        return idx
    
Solution().canCompleteCircuit(gas = [5,1,2,3,4], cost = [4,4,1,5,1])
