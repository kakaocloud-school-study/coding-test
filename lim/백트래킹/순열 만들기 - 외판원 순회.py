import sys

def sol(n, grid):
    def get_min(count, picked_idx, picked_sum):
        if count == n:
            value = picked_sum + grid[picked_idx][0]
            return value if grid[picked_idx][0] != 0 else sys.maxsize
        min_value = sys.maxsize
        for i in range(n):
            if i in picked_indices:
                continue
            if grid[picked_idx][i] == 0:
                continue
            picked_indices.add(i)
            min_value = min(min_value, get_min(count+1, i, picked_sum+grid[picked_idx][i]))
            picked_indices.remove(i)
        return min_value
    picked_indices = set([0])
    return get_min(1, 0, 0)

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, grid))