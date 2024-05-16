'''
dp[day][i]: day번째 날에 i번 옷을 입었을 때 day날까지의 최대 만족도
'''

import sys

def sol(n, m, clothes):
    dp = [[-1]*n for __ in range(m+1)]
    for i in range(n):
        s, e, v = clothes[i]
        if s > 1 or e < 1:
            continue
        dp[1][i] = 0

    for day in range(2, m+1):
        for today_clothes_idx in range(n):
            today_s, today_e, today_v = clothes[today_clothes_idx]
            if today_s > day or today_e < day:
                continue
            for prev_clothes_idx in range(n):
                if dp[day-1][prev_clothes_idx] == -1:
                    continue
                dp[day][today_clothes_idx] = max(dp[day][today_clothes_idx], dp[day-1][prev_clothes_idx] + abs(clothes[prev_clothes_idx][2]-today_v))
    return max(dp[m])

n, m = map(int, sys.stdin.readline().split())
clothes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, m, clothes))