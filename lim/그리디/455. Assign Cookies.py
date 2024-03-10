from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_idx = 0
        s_idx = 0
        count = 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                count += 1
                g_idx += 1
                s_idx += 1
            else:
                s_idx += 1
        return count