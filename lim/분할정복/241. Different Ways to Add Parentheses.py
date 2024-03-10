'''
시간복잡도?
'''

from typing import List
import re


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = list(map(int, re.split("[*+-]", expression)))
        ops = re.findall('[*+-]', expression)
        
        def foo(s_idx, e_idx):
            if s_idx == e_idx:
                return [nums[s_idx]]
            values = []
            for i in range(s_idx, e_idx):
                left_values = foo(s_idx, i)
                right_values = foo(i + 1, e_idx)
                for left_value in left_values:
                    for right_value in right_values:
                        if ops[i] == '+':
                            values.append(left_value + right_value)
                        elif ops[i] == '-':
                            values.append(left_value - right_value)
                        elif ops[i] == '*':
                            values.append(left_value * right_value)
            return values
        
        return foo(0, len(nums) - 1)
