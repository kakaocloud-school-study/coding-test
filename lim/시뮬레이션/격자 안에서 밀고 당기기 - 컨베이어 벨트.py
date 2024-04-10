import sys


def sol(arr1, arr2, n, t):
    new_arr1 = []
    new_arr2 = []
    s_idx = (2*n - t) % (2*n)
    for i in range(s_idx, s_idx + n):
        if (i % (n * 2)) < n:
            new_arr1.append(arr1[i % n])
        else:
            new_arr1.append(arr2[i % n])
    for i in range(s_idx + n, s_idx + 2*n):
        if (i % (n * 2)) < n:
            new_arr2.append(arr1[i % n])
        else:
            new_arr2.append(arr2[i % n])
    return new_arr1, new_arr2

n, t = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))
new_arr1, new_arr2 = sol(arr1, arr2, n, t)
for e in new_arr1:
    print(e, end=' ')
print()
for e in new_arr2:
    print(e, end=' ')