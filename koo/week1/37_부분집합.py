import sys
from typing import List
read = sys.stdin.readline

def sol(idx: int, path: List[int]) -> None:
    res.append(path)
    
    for i in range(idx, len(nums)):
        sol(i + 1, path + [nums[i]])
    
res = []
nums = list(map(int, list(read().rstrip()[1::2])))
sol(0, [])
print(res)