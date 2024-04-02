import sys


def sol(n, arr, s1, e1, s2, e2):
    arr = arr[:s1-1] + arr[e1:]
    arr = arr[:s2-1] + arr[e2:]
    return arr

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
s1, e1 = list(map(int, sys.stdin.readline().split()))
s2, e2 = list(map(int, sys.stdin.readline().split()))

arr = sol(n, arr, s1, e1, s2, e2)
print(len(arr))
for e in arr:
    print(e)