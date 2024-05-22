import sys

def sol(n, grid):
    dxs = [1, 1, -1, -1]
    dys = [-1, 1, 1, -1]
    def cal(r, c, w, h):
        if r+(w-1) >= n or c-(w-1) < 0:
            return 0
        if r+(h-1) >= n or c+(h-1) >= n:
            return 0
        if r+(w-1)+(h-1) >= n or c-(w-1)+(h-1) >= n or c-(w-1)+(h-1) < 0:
            return 0
        value = 0
        for _ in range(w-1):
            value += grid[r][c]
            r += dxs[0]
            c += dys[0]
        for _ in range(h-1):
            value += grid[r][c]
            r += dxs[1]
            c += dys[1]
        for _ in range(w-1):
            value += grid[r][c]
            r += dxs[2]
            c += dys[2]
        for _ in range(h-1):
            value += grid[r][c]
            r += dxs[3]
            c += dys[3]
        return value
    def max_at(r, c):
        value = 0
        for i in range(2, n):
            for j in range(2, n):
                value = max(value, cal(r, c, i, j))
        return value
        
    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(answer, max_at(i, j))
    return answer


n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, grid))