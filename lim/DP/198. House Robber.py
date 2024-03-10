'''
dp1[i]: i를 털었을 때 i까지의 최대값
dp2[i]: i를 털지않았을 때 i까지의 최대값
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[-1]
        
        dp1 = [0] * (len(nums))
        dp2 = [0] * (len(nums))
        dp1[0] = nums[0]
        dp2[0] = 0
        dp1[1] = nums[1]
        dp2[1] = dp1[0]
        for i in range(2, len(nums)):
            dp1[i] = dp2[i-1] + nums[i]
            dp2[i] = max(dp1[i-1], dp2[i-1])
        
        return max(dp1[-1], dp2[-1])
    
Solution().rob([1,2,3,1])