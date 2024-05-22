import sys

def sol(n):
    def find_same_value_indices(idx):
        indices = []
        for i in range(idx):
            if arr[i] == arr[idx]:
                indices.append(i)
        return indices
    
    def has_pattern(idx1, idx2):
        i1 = 2*idx1 - idx2 + 1
        for i2 in range(idx1+1, idx2+1):
            if i1 < 0:
                return False
            if arr[i1] != arr[i2]:
                return False
            i1 += 1
        return True
    
    def possible():
        i2 = len(arr) - 1
        for i1 in find_same_value_indices(i2):
            if has_pattern(i1, i2):
                return False
        return True

    def get_min():
        if len(arr) == n:
            print(''.join(arr))
            return True
        
        for num in ('4', '5', '6'):
            arr.append(num)
            if possible() and get_min():
                return True
            arr.pop()
        return False
        
    arr = []
    return get_min()

n = int(sys.stdin.readline())
sol(n)