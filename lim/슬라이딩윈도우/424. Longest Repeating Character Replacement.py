'''
통과는 했는데 속도가...
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def count_ch(ch):
            max_repeat_count = 0
            repeat_count = 0
            k_count = 0
            s_idx = 0
            e_idx = 0

            while e_idx < len(s):
                if s[e_idx] == ch:
                    e_idx += 1
                    repeat_count += 1
                    max_repeat_count = max(max_repeat_count, repeat_count)
                elif s[e_idx] != ch and k_count < k:
                    k_count += 1
                    e_idx += 1
                    repeat_count += 1
                    max_repeat_count = max(max_repeat_count, repeat_count)
                elif s[e_idx] != ch and k_count >= k:
                    if s[s_idx] != ch and k_count != 0:
                        k_count -= 1
                    if repeat_count != 0:
                        repeat_count -= 1
                    s_idx += 1
                e_idx = max(e_idx, s_idx)
            return max_repeat_count

        answer = 0
        for ch in set(s):
            answer = max(answer, count_ch(ch))
        return answer

Solution().characterReplacement(s = "ABAA", k = 0)