import sys


def sol(n, m, coins):
    dp = [-1] * (m+1)
    dp[0] = 0
    for coin in coins:
        for curr_money in range(m, 0, -1):
            if coin > curr_money:
                continue
            if dp[curr_money - coin] == -1:
                continue
            if dp[curr_money] == -1:
                dp[curr_money] = dp[curr_money - coin] + 1
            dp[curr_money] = min(dp[curr_money], dp[curr_money - coin] + 1)
    return dp[m]

n, m = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))
print(sol(n, m, coins))