'''
dp[i][j][k]: i번째까지의 선수들 중에서 축구 j명 농구 k명을 뽑는 최대 능력합
'''

import sys

def sol(n, students):
    dp = [[[-1]*10 for _ in range(12)] for __ in range(n)]
    dp[0][0][0] = 0
    dp[0][1][0] = students[0][0]
    dp[0][0][1] = students[0][1]

    for i in range(1, n):
        for j in range(12):
            for k in range(10):
                if dp[i-1][j][k] != -1:
                    dp[i][j][k] = dp[i-1][j][k]
                if j > 0 and dp[i-1][j-1][k] != -1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k]+students[i][0])
                if k > 0 and dp[i-1][j][k-1] != -1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1]+students[i][1])
    return dp[n-1][11][9]

n = int(sys.stdin.readline())
students = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, students))