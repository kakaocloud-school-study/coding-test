import sys


def sol(s, e, m):
    if m == 0:
        return [[]]
    answer = []
    for i in range(s, e + 1):
        subanswer = sol(i+1, e, m-1)
        for arr in subanswer:
            answer.append([i] + arr)
    return answer

n, m = map(int, sys.stdin.readline().split())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for arr in sol(1, n, m):
    for num in arr:
        print(num, end=' ')
    print()