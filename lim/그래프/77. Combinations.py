from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            yield []
        else:
            for num in range(1, n+1):
                for sub_list in self.combine(n-1, k-1):
                    yield [num] + sub_list