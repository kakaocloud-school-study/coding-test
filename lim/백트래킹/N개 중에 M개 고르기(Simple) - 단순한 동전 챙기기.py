import sys

def sol(n, sr, sc, er, ec, coins):
    def get_dist(r1, c1, r2, c2):
        return abs(r1-r2) + abs(c1-c2)
    def get_min(r, c, count):
        if len(picked_coins) >= 3:
            return count + get_dist(r, c, er, ec)
        
        min_value = sys.maxsize
        for nr, nc, price in coins:
            if (nr, nc, price) in visited:
                continue
            if len(picked_coins) != 0 and picked_coins[-1][2] >= price:
                continue

            picked_coins.append((nr, nc, price))
            visited.add((nr, nc, price))
            min_value = min(min_value, get_min(nr, nc, count + get_dist(r, c, nr, nc)))
            picked_coins.pop()
            visited.remove((nr, nc, price))
        return min_value

    picked_coins = []
    visited = set()

    answer = get_min(sr, sc, 0)
    return answer if answer != sys.maxsize else -1
    
                

n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
coins = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            sr, sc = i, j
        elif grid[i][j] == 'E':
            er, ec = i, j
        elif grid[i][j] == '.':
            pass
        else:
            coins.append((i, j, grid[i][j]))
print(sol(n, sr, sc, er, ec, coins))