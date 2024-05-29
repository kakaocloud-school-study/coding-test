import sys

def sol(n, grid):
    def get_max(count, picked_sum):
        if count == n:
            return picked_sum
        max_value = 0
        for i in range(n):
            if i in picked_indices:
                continue
            picked_indices.add(i)
            max_value = max(max_value, get_max(count+1, picked_sum+grid[count][i]))
            picked_indices.remove(i)
        return max_value
    picked_indices = set()
    return get_max(0, 0)

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(sol(n, grid))