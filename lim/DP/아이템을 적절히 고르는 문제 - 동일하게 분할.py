'''
전체합 / 2 인 부분 수열 합이 존재하는 지 찾는다
'''

import sys


def sol(n, m, coins):
    if m % 2 == 1:
        return 'No'
    m //= 2
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
    if dp[m] > 0:
        return 'Yes'
    return 'No'

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
m = sum(coins)
print(sol(n, m, coins))