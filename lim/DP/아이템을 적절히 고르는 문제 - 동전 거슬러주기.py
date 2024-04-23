import sys


def sol(n, m, coins):
    dp = [-1] * (m+1)
    for coin in coins:
        if coin > m:
            break
        dp[coin] = 1
    for curr_money in range(1, m):
        if dp[curr_money] == -1:
            continue
        for coin in coins:
            if curr_money + coin > m:
                continue
            if dp[curr_money + coin] == -1:
                dp[curr_money + coin] = dp[curr_money] + 1
            else:
                dp[curr_money + coin] = min(dp[curr_money + coin], dp[curr_money] + 1)
    return dp[m]

n, m = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()
print(sol(n, m, coins))