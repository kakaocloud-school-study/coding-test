from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        for interval in intervals[1:]:
            prev_s, prev_e = answer[-1]
            s, e = interval
            if s <= prev_e:
                answer[-1] = (prev_s, max(e, prev_e))
            else:
                answer.append((s, e))
        return answer

Solution().merge([[1,3],[2,6],[8,10],[15,18]])