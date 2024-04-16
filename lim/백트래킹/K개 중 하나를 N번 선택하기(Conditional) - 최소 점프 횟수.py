import sys

def sol(pos, n, jump_limits):
    answer = []
    if n == 0 or pos + 1 >= len(jump_limits):
        return [[]]
    for jump in range(1, jump_limits[pos] + 1):
        subanswer = sol(pos+jump, n-1, jump_limits)
        for sublist in subanswer:
            answer.append([jump] + sublist)
    return answer

n = int(sys.stdin.readline())
jump_limits = list(map(int, sys.stdin.readline().split()))
counts = []
for jumps in sol(0, n, jump_limits):
    count = len(jumps)
    if count != 0:
        counts.append(count)
if len(counts):
    print(min(counts))
else:
    print(-1)