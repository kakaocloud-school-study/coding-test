from typing import List


def solution(triangle: List[List[int]]):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
    return max(dp[-1])