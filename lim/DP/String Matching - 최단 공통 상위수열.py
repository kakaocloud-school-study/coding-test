import sys


def sol(line1, line2):
    n = len(line1)
    m = len(line2)
    dp = [[sys.maxsize]*m for _ in range(n)]
    dp[0][0] = 1 if line1[0] == line2[0] else 2
    for i in range(1, n):
        dp[i][0] = i+1 if line1[i] == line2[0] else dp[i-1][0] + 1
    for j in range(1, m):
        dp[0][j] = j+1 if line1[0] == line2[j] else dp[0][j-1] + 1
    
    for i in range(1, n):
        for j in range(1, m):
            if line1[i] == line2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
    return dp[-1][-1]

line1 = sys.stdin.readline().strip() # 개행 문자 주의
line2 = sys.stdin.readline().strip()
print(sol(line1, line2))
