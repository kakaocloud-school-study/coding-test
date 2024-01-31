import sys
from typing import List, Dict
read = sys.stdin.readline

num_alphabet_dict = {
    '2': list('abc'),
    '3': list('def'),
    '4': list('ghi'),
    '5': list('jkl'),
    '6': list('mno'),
    '7': list('pqrs'),
    '8': list('tuv'),
    '9': list('wxyz')
}

def sol(idx: int, words: str) -> None:
    if idx == len(nums):
        res.append(words)
        return
    for alphabet in num_alphabet_dict[nums[idx]]:
        sol(idx + 1, words + alphabet)
    pass

idx = 0
res = []
nums = read().rstrip()
sol(0, '')
print(res)