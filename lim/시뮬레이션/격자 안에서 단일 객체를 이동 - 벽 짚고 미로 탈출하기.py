import sys


def sol(n, r, c, grid):
    drs = [0, 1, 0, -1]
    dcs = [1, 0, -1, 0]
    direction = 0
    visited = set()

    def out_range(r, c):
        return r < 0 or r >= n or c < 0 or c >= n

    time = 0
    while True:
        if (r, c, direction) in visited:
            return -1
        visited.add((r, c, direction))
        foward_r, foward_c = r + drs[direction], c + dcs[direction]
        right_r, right_c = r + drs[(direction+1)%4], c + dcs[(direction+1)%4]

        if grid[right_r][right_c] == '.':
            direction = (direction + 1) % 4
            foward_r, foward_c = r + drs[direction], c + dcs[direction]
            r, c = foward_r, foward_c
            time += 1
            continue
        if out_range(foward_r, foward_c):
            time += 1
            return time
        if grid[foward_r][foward_c] == '#':
            direction = (direction + 3) % 4
            continue
        r, c = foward_r, foward_c
        time += 1


n = int(sys.stdin.readline())
r, c = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().strip() for _ in range(n)]

print(sol(n, r-1, c-1, grid))