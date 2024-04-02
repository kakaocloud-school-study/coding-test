import sys


def sol(n, m, t, grid):
    max_w = 0
    count = 0

    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    def move(new_grid, r, c, idx, w, d):
        if new_grid[r][c]:
            old_idx, old_w, old_d = new_grid[r][c]
            if old_idx > idx:
                new_grid[r][c] = (old_idx, old_w + w, old_d)
            else:
                new_grid[r][c] = (idx, old_w + w, d)
        else:
            new_grid[r][c] = (idx, w, d)
    def move_all():
        new_grid = [[None for __ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == None:
                    continue
                idx, w, d = grid[i][j]
                nr, nc = i + drs[d], j + dcs[d]
                if nr >= 0 and nr < n and nc >= 0 and nc < n:
                    move(new_grid, nr, nc, idx, w, d)
                else:
                    move(new_grid, i, j, idx, w, (d + 2) % 4)
        return new_grid
    
    while t:
        t -= 1
        grid = move_all()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == None:
                continue
            count += 1
            max_w = max(max_w, grid[i][j][1])
    return count, max_w


n, m, t = map(int, sys.stdin.readline().split())
grid = [[None for __ in range(n)] for _ in range(n)]
dirs = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3,
}
for i in range(m):
    r, c, d, w = sys.stdin.readline().split()
    grid[int(r)-1][int(c)-1] = (i, int(w), dirs[d])

count, max_w = sol(n, m, t, grid)
print(count, max_w)

'''
D5   R9   0    0
D2   D10  0    0
0    0    0    0
0    0    0    0

0    0    R9   0
D5   0    0    0
D2   D10  0    0
0    0    0    0
'''