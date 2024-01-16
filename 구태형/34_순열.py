import sys
from typing import List
read = sys.stdin.readline

def sol(output: List[int], rest: List[int]):
    if len(output) == len(nums):
        res.append(output)
        return
    for num in rest:
        next = rest[:]
        next.remove(num)
        sol(output + [num], next)

nums = sorted(list(map(int, list(read().rstrip()[1::2]))))
res = []
sol([], nums)
print(res)