import sys


def sol(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + 2*dp[i-2]) % 10_007
    return dp[n]

n = int(sys.stdin.readline())
print(sol(n))