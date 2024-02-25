'''
쿨타임이 다 찬 태스크 중에 남은 양이 많은 태스크를 우선 처리함
쿨타임이 다 찬 태스크가 없으면 쿨타임이 가장 얼마 안 남은 태스크 중에 남은 양이 가장 많은 태스크에 대해 처리 대기함

힙큐를 두 개(힙큐1:(쿨타임풀리는 시간, 남은 양), 힙큐2:(남은 양)) 사용하여 최적화할 수 있지 않을까?
'''

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_queue = []
        task_counts = defaultdict(int)
        time = 0
        for task_name in tasks:
            task_counts[task_name] += 1
        for task_name in task_counts:
            task_queue.append((0, task_counts[task_name], task_name))
        
        def find_task():
            task_idx = -1
            for i, (end_at, count, task_name) in enumerate(task_queue):
                if count == 0:
                    continue
                if time < end_at:
                    continue
                if task_idx == -1 or task_queue[task_idx][1] < count:
                    task_idx = i
            if task_idx == -1:
                for i, (end_at, count, task_name) in enumerate(task_queue):
                    if count == 0:
                        continue
                    if task_idx == -1 or task_queue[task_idx][0] > end_at:
                        task_idx = i
                    elif task_queue[task_idx][0] == end_at:
                        if task_queue[task_idx][1] < count:
                            task_idx = i
            return task_idx

        while True:
            task_idx = find_task()
            if task_idx == -1:
                break
            end_at, count, task = task_queue[task_idx]
            if time < end_at:
                time = end_at
            count -= 1
            time += 1
            end_at = time + n
            task_queue[task_idx] = (end_at, count, task)
        return time
    
Solution().leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 1)