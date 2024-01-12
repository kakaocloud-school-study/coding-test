from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        answers = []
        def foo(num, count):
            if num > n + 1:
                return
            if count == k:
                answers.append(list(arr))
                return
            arr.append(num)
            foo(num + 1, count + 1)
            arr.pop()
            foo(num + 1, count)
        
        foo(1, 0)
        return answers