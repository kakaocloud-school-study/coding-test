from typing import List


def solution(number, k):
    lens = len(number) - k
    nums = list(map(int, list(number)))
    ret = 0

    def dfs(rest: List[int], res: List[str]):
        if len(res) == lens:
            nonlocal ret
            ret = max(ret, int(''.join(res)))
            return
        for i in range(len(rest)):
            dfs(rest[i+1:], res + [str(rest[i])])

    dfs(nums, [])
    return ret