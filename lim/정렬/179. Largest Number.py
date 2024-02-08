from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(list(map(str, nums)), reverse=True, key=cmp_to_key(lambda x, y: 1 if x+y > y+x else (0 if x+y == y+x else -1))))))