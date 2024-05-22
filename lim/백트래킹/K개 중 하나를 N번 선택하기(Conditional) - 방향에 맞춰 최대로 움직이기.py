import sys

def sol(n, r, c, grid, dir_grid):
    drs = [-1,-1,0,1,1,1,0,-1]
    dcs = [0,1,1,1,0,-1,-1,-1]  

    def in_range(r, c):
        return r<n and r>=0 and c<n and c>=0

    def get_max(r, c, count):
        direction = dir_grid[r][c]
        value = grid[r][c]
        max_count = count
        dist = 1
        nr, nc = r+drs[direction]*dist, c+dcs[direction]*dist
        while in_range(nr, nc):
            if grid[nr][nc] > value:
                max_count = max(max_count, get_max(nr, nc, count+1))

            dist += 1
            nr, nc = r+drs[direction]*dist, c+dcs[direction]*dist
        
        return max_count
    
    return get_max(r, c, 0)
        

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dir_grid = [list(map(lambda x: int(x)-1, sys.stdin.readline().split())) for _ in range(n)]
r, c = map(lambda x: int(x)-1, sys.stdin.readline().split())
print(sol(n, r, c, grid, dir_grid))