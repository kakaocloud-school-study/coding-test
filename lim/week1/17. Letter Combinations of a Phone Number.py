from typing import List
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_2_chs = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        visited = set()
        answers = []
        def foo(word, idx):
            if idx == len(digits):
                answers.append(word)
                return
            num = digits[idx]
            for ch in num_2_chs[num]:
                foo(word + ch, idx + 1)
        foo('', 0)

        if digits == '':
            return []
        return answers
