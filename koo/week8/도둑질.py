from typing import List

def solution(money: List[int]):
    dp = [[0] * len(money) for _ in range(2)]
    dp[0][0], dp[0][1] = 0, money[1] # 첫 번째 집 선택 x
    dp[1][0], dp[1][1] = money[0], money[0] # 첫 번째 집 선택

    for i in range(2, len(money)):
        for j in range(2):
            dp[j][i] = max(dp[j][i-1], money[i] + dp[j][i-2])
    return max(dp[0][-1], dp[1][-2])
