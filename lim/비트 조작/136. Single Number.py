from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        bias = 3 * (10**4)
        for num in nums: # num번째 자리 수 비트 토글
            mask ^= 1 << (num + bias)
        for num in nums: # num번째 자리 수가 1이면 리턴
            if mask & (1 << (num + bias)):
                return num