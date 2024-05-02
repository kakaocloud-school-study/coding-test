'''
dp[i]: i번 숫자를 끝으로 하는 최대 부분합. i-1번째에서 부분합이 이어지는 경우와 i번 숫자를 첫 숫자로 부분합을 새로 시작하는 경우를 비교한다
'''

import sys

def sol(n, arr):
    dp = [-sys.maxsize] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    answer = max(dp)
    return answer if answer != -sys.maxsize else -1

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(sol(n, arr))