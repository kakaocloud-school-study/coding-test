import sys

def sol(n, arr):
    sum_2n = sum(arr)

    def get_min_diff(count, picked_idx, picked_sum):
        if count == n:
            return abs(sum_2n - 2*picked_sum)
        min_value = sys.maxsize
        for i in range(picked_idx+1, 2*n):
            if i in picked_indices:
                continue
            picked_indices.add(i)
            min_value = min(min_value, get_min_diff(count + 1, i, picked_sum + arr[i]))
            picked_indices.remove(i)
        return min_value
    picked_indices = set()
    return get_min_diff(0, -1, 0)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(sol(n, arr))