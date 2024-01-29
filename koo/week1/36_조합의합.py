import sys
from typing import List
read = sys.stdin.readline

def sol(output: List[int], rest: List[int]) -> None:
    if sum(output) == target:
        res.append(output[:])
        return
    elif sum(output) > target:
        return
    else:
        for i in range(len(rest)):
            sol(output + [rest[i]], [x for x in rest[i:]])

nums = sorted(list(map(int, list(read().rstrip()[1::2]))))
target = int(read())
res = []
sol([], nums)

print('[')
for r in res:
    print(' ' * 2, end='')
    print(r)
print(']')
