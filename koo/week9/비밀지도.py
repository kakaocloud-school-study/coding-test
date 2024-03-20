from typing import List


def solution(n: int, arr1: List[int], arr2: List[int]):
    res = []
    for i in range(n):
        line = bin(arr1[i] | arr2[i])[2:]
        res.append(line.zfill(n).replace('1', '#').replace('0', ' '))
    return res
