'''
힙 + 슬라이딩 윈도우

슬라이딩에서 pop되는 원소를 기록했다가 윈도우최대값을 힙에서 구할 때 pop목록의 원소가 힙 top에 없을 때까지 pop한다
heappop 반복문이 for문 안에 있어 n^2처럼 보이지만 전체에서 봤을 때는 모든 원소를 한번씩만 넣다 빼므로 nlogn시간 걸린다
'''

from collections import defaultdict
from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = list(map(lambda x:-x, nums[:k]))
        heapq.heapify(window)
        pop_counts = defaultdict(int)
        answer = [-window[0]]

        for i in range(k, len(nums)):
            pop_counts[nums[i-k]] += 1
            heapq.heappush(window, -nums[i])
            while len(window) and pop_counts[-window[0]]:
                popped = -heapq.heappop(window)
                pop_counts[popped] -= 1
            answer.append(-window[0])
        return answer

Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)