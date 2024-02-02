from heapq import *
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr: List[int] = []
        res: int = None
        for num in nums:
            heappush(arr, -num)
        for _ in range(k):
            res = -heappop(arr)
        return res
