from typing import List


def solution(number, k):
    stk = []
    
    for num in number:
        while stk and stk[-1] < num and k > 0:
            stk.pop()
            k -= 1
        stk.append(num)
    if k > 0:
        stk = stk[:-k]
    return ''.join(stk)
