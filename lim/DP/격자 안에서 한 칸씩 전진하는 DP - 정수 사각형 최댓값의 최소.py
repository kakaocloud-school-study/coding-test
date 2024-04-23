'''
O(nm)시간 풀이도 존재함
'''

import sys


def sol(n, arr):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] <= arr[j]:
                continue
            dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(sol(n, arr))