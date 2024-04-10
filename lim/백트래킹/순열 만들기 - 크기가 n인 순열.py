import sys


def sol(n):
    visited = set()
    def _sol(pos, n):
        if pos == n:
            return [[]]
        result = []
        for num in range(1, n+1):
            if num in visited:
                continue
            visited.add(num)
            for arr in _sol(pos+1, n):
                result.append([num]+arr)
            visited.remove(num)
        return result
    return _sol(0, n)

n = int(sys.stdin.readline())
for arr in sol(n):
    for num in arr:
        print(num, end=' ')
    print()