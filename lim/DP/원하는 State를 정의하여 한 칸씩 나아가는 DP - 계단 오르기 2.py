'''
dp[i][j]: i번 계단까지 올라왔을 때 모은 최대 동전 수. 단 j번 한칸뛰기함
'''

import sys

def sol(n, arr):
    dp = [[-1] * 4 for _ in range(n)]
    dp[0][1] = arr[0]
    dp[1][0] = arr[1]
    dp[1][2] = dp[0][1] + arr[1]
    for i in range(1, n):
        if dp[i-2][0] != -1:
            dp[i][0] = dp[i-2][0] + arr[i]
        if max(dp[i-1][0], dp[i-2][1]) != -1:
            dp[i][1] = max(dp[i-1][0], dp[i-2][1]) + arr[i]
        if max(dp[i-1][1], dp[i-2][2]) != -1:
            dp[i][2] = max(dp[i-1][1], dp[i-2][2]) + arr[i]
        if max(dp[i-1][2], dp[i-2][3]) != -1:
            dp[i][3] = max(dp[i-1][2], dp[i-2][3]) + arr[i]
    return max(dp[n-1])

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(sol(n, arr))