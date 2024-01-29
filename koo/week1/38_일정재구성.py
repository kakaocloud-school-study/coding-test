import sys
from collections import defaultdict
from typing import List, Dict
read = sys.stdin.readline

def sol(src: str='JFK') -> None:
    if src != 'JFK':
        return
    stk: List[str] = []
    stk.append(src)
    while stk:
        src = stk.pop()
        res.append(src)
        for dst in flight_dict[src]:
            if dst[1] == 1:
                dst[1] = 0
                stk.append(dst[0])

n = int(read())
flight_dict = defaultdict(list)
res = []

for _ in range(n):
    x, y = read().split()
    flight_dict[x].append([y, 1])

for elem_list in flight_dict.values():
    elem_list.sort(reverse=True)

sol()
print(res)
