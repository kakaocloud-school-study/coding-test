'''
dp[i][j]: i번째 층에서 j번 방에 들어갔을 때 얻은 i번째 층까지의 최대 보물수 합
'''

import sys

def sol(n, m, stages):
    dp = [[-1]*m for __ in range(n)]
    for i in range(m):
        dp[0][i] = stages[0][i]

    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                if j == k:
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k] + stages[i][j])
    return max(dp[n-1])

n, m = map(int, sys.stdin.readline().split())
stages = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, m, stages))