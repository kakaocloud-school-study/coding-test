import sys

def sol(n, m, arr):
    def n_count(idx):
        origin_num = arr[idx]
        count = 0
        while idx < n and arr[idx] == origin_num:
            count += 1
            idx += 1
        return count
    def bomb():
        n_arr = []
        idx = 0
        while idx < n:
            count = n_count(idx)
            if count >= m:
                idx += count
                continue
            n_arr.append(arr[idx])
            idx += 1
        return n_arr
    
    n_arr = bomb()
    while len(n_arr) != len(arr):
        arr = n_arr
        n = len(n_arr)
        n_arr = bomb()
    return arr

n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr = sol(n, m, arr)
print(len(arr))
for num in arr:
    print(num)