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

def cal(arr, points):
    dists = []
    for i in range(len(arr)):
        x1, y1 = points[arr[i] - 1]
        for j in range(len(arr)):
            x2, y2 = points[arr[j] - 1]
            dists.append(abs(x2 - x1)**2 + abs(y2 - y1)**2)
    return max(dists)

n, m = map(int, sys.stdin.readline().split())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dists = []
for arr in sol(1, n, m):
    dists.append(cal(arr, points))
print(min(dists))