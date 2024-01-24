from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            yield []
        elif target < 0:
            return
        else:
            for i, num in enumerate(candidates):
                for comb in self.combinationSum(candidates[i:], target - num):
                    yield [num] + comb