import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        while k:
            k -= 1
            answer = -heapq.heappop(nums)
        return answer