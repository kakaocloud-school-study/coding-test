from copy import deepcopy
import sys

def sol(n, grid):
    def in_range(r, c):
        return r<n and r>=0 and c<n and c>=0
    def increase_count(bomb_grid, r, c, rollback):
        if in_range(r, c):
            bomb_grid[r][c] += (-1 if rollback else 1)    
    def bomb(bomb_grid, r, c, bomb_type, rollback = False):
        if bomb_type == 1:
            increase_count(bomb_grid, r-1, c, rollback)
            increase_count(bomb_grid, r-2, c, rollback)
            increase_count(bomb_grid, r+1, c, rollback)
            increase_count(bomb_grid, r+2, c, rollback)
        elif bomb_type == 2:
            increase_count(bomb_grid, r+1, c, rollback)
            increase_count(bomb_grid, r-1, c, rollback)
            increase_count(bomb_grid, r, c+1, rollback)
            increase_count(bomb_grid, r, c-1, rollback)
        elif bomb_type == 3:
            increase_count(bomb_grid, r+1, c+1, rollback)
            increase_count(bomb_grid, r+1, c-1, rollback)
            increase_count(bomb_grid, r-1, c+1, rollback)
            increase_count(bomb_grid, r-1, c-1, rollback)
    def count(bomb_grid):
        value = 0
        for i in range(n):
            for j in range(n):
                if bomb_grid[i][j] != 0:
                    value += 1
        return value
    
    def next_pos(r, c):
        c += 1
        while r < n:
            while c < n:
                if grid[r][c] == 1:
                    return (r, c)
                c += 1
            r += 1
            c = 0
        return (n, 0)

    def get_max_bombs(bomb_grid, r, c):
        if r == n:
            return count(bomb_grid)

        max_value = 0
        for bomb_type in range(1, 4):
            bomb(bomb_grid, r, c, bomb_type)
            nr, nc = next_pos(r, c)
            max_value = max(max_value, get_max_bombs(bomb_grid, nr, nc))
            bomb(bomb_grid, r, c, bomb_type, rollback=True)
        return max_value
    
    bomb_grid = deepcopy(grid)
    r, c = (0, 0) if grid[0][0] == 1 else next_pos(0, 0)
    return get_max_bombs(bomb_grid, r, c)

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, grid))