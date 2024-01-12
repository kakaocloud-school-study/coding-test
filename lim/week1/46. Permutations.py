'''
메모리가 많이 사용된다. 더 좋은 풀이를 생각해 보자.
'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = []
        checked = [False] * len(nums)
        def foo(arr):
            if len(arr) == len(nums):
                answers.append(arr)
                return
            for i in range(len(nums)):
                if checked[i]:
                    continue
                arr.append(nums[i])
                checked[i] = True
                foo(arr, checked)
                arr.pop()
                checked[i] = False
        foo([])
        return answers

