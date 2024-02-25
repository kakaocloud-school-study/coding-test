'''
슬라이딩 윈도우가 아닌 투포인터로 풀림
윈도우 체크할 때 알파벳 개수가 한정적이므로 거의 상수 시간으로 체크 함수가 돌아감에 유의
'''

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = defaultdict(int)
        window_counts = defaultdict(int)
        min_range = None
        s_idx, e_idx = 0, 0

        for ch in t:
            t_counts[ch] += 1
        window_counts[s[0]] += 1

        def check():
            for key in t_counts:
                if window_counts[key] < t_counts[key]:
                    return False
            return True
        while e_idx < len(s):
            if check():
                if (min_range == None) or (min_range[1] - min_range[0] > e_idx - s_idx):
                    min_range = (s_idx, e_idx)
                window_counts[s[s_idx]] -= 1
                s_idx += 1
            else:
                e_idx += 1
                if e_idx < len(s):
                    window_counts[s[e_idx]] += 1
        
        if min_range == None:
            return ''
        return s[min_range[0]: min_range[1]+1]

Solution().minWindow(s = "A", t = "A")