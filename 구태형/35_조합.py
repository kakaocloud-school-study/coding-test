import sys
from typing import List
read = sys.stdin.readline

def sol(output: List[int], rest: List[int]) -> None:
    if k == len(output):
        res.append(output)
        return
    for i in rest:
        sol(output + [i], range(i+1, n+1))
    pass

res = []
n, k = map(int, read().split())
sol([], range(1, n+1))
print(res)