'''
시간제한을 너무 후하게 주는 것 같다.
n^2 풀이로도 가능할 것 같지만 이진탐색 적용하여 nlogn 풀이로 해결함.
'''

from typing import List
from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            idx = bisect_left(arr, target)
            if idx != len(arr) and arr[idx] == target:
                return True
        return False
    
Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)