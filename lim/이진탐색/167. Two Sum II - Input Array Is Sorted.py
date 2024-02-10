'''
투포인터 인덱스 이동 자체를 이진탐색으로 최적화?
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            sum_val = numbers[left] + numbers[right]
            if sum_val > target:
                right -= 1
            elif sum_val < target:
                left += 1
            else:
                break
        return [left, right]