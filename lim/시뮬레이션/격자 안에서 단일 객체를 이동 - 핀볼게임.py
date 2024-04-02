import sys


def sol(n, grid):
    answer = 0
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    def roll(r, c, direction):
        count = 1
        while r >= 0 and r < n and c >= 0 and c < n:
            if grid[r][c] != 0 and (grid[r][c] % 2) == (direction % 2):
                direction = ((direction + 4 - 1) % 4)
            elif grid[r][c] != 0 and (grid[r][c] % 2) != (direction % 2):
                direction = ((direction + 4 + 1) % 4)
            r, c = r + drs[direction], c + dcs[direction]
            count += 1
        return count
    
    # roll(4, 0, 1)
    for i in range(n):
        for j in range(n):
            if i != 0 and j != 0 and i != n-1 and j != n-1:
                continue
            for direction in range(4):
                if direction == 0 and i != n - 1:
                    continue
                if direction == 1 and j != 0:
                    continue
                if direction == 2 and i != 0:
                    continue
                if direction == 3 and j != n - 1:
                    continue
                answer = max(answer, roll(i, j, direction))
    return answer

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(sol(n, grid))