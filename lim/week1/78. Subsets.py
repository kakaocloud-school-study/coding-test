from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            yield []
        else:
            for i, num in enumerate(nums):
                for subset in self.subsets(nums[i+1:]):
                    yield [num] + subset
            yield []

aaa = Solution().subsets([1,2,3])
next(aaa)