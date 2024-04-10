import sys

def sol(k, n):
    answer = []
    if n == 0:
        return [[]]
    subanswer = sol(k, n-1)
    for num in range(1, k+1):
        for sublist in subanswer:
            if len(sublist) > 1 and sublist[0] == num and sublist[1] == num:
                continue
            answer.append([num] + sublist)
    return answer

k, n = map(int, sys.stdin.readline().split())
for arr in sol(k, n):
    for num in arr:
        print(num, end=' ')
    print()