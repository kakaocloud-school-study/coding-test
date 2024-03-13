from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = cur = nums[0]
        if cur < 0:
            cur = 0
        for num in nums[1:]:
            cur += num
            res = max(cur, res)
            if cur < 0:
                cur = 0
        return res