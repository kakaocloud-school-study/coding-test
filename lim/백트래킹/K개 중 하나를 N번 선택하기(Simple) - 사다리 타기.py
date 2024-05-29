import sys

def sol(n, m, swaps):
    def get_min(arr, swap_idx, swap_count):
        if swap_idx == m:
            return swap_count if origin_arr == arr else sys.maxsize
        
        min_value = sys.maxsize

        idx = swaps[swap_idx][0]
        arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        min_value = min(min_value, get_min(arr, swap_idx+1, swap_count+1))

        arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        min_value = min(min_value, get_min(arr, swap_idx+1, swap_count))

        return min_value
        
    origin_arr = list(range(1, n+1))
    swaps.sort(key=lambda x:x[1])
    for i, _ in swaps:
        origin_arr[i], origin_arr[i+1] = origin_arr[i+1], origin_arr[i]
    
    return get_min(list(range(1, n+1)), 0, 0)    

n, m = map(int, sys.stdin.readline().split())
swaps = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    swaps.append((a-1, b-1))
print(sol(n, m, swaps))