'''
보이어 무어 다수결 투표
분할정복?
'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        voted = None
        for num in nums:
            if count == 0:
                voted = num
            if voted == num:
                count += 1
            else:
                count -= 1
        
        return voted