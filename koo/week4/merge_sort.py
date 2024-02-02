def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    res = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1
    res += left[left_idx:]
    res += right[right_idx:]
    return res


if __name__ == '__main__':
    arr = [5, 7, 9, 3, 1, 6, 2, 4, 8]
    arr = merge_sort(arr)
    print(arr)