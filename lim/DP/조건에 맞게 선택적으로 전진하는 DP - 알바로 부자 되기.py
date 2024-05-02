'''
dp[i]: i번째 알바를 무조건 포함한채 0~i 알바를 안겹치게 고르는 경우에서 최대 총금액
dp[i+1]: 0~i번 dp 중에서 안겹치는 dp중 값이 가장 큰 dp와 i+1번째 금액은 더한 값

nlogn 최적화 풀이도 있음
'''

import sys


def sol(n, works):
    dp = [0] * n
    for i in range(n):
        i_s, i_e, i_p = works[i]
        dp[i] = i_p
        for j in range(i):
            j_s, j_e, j_p = works[j]
            if i_s <= j_e:
                continue
            dp[i] = max(dp[i], dp[j] + i_p)
    return max(dp)

n = int(sys.stdin.readline())
works = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, works))