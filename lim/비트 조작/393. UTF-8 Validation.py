from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        '''
        01111111
        10111111
        11011111
        11101111
        11110111
        '''
        one_code_max = int('0b01111111', 2)
        follow_code_max = int('0b10111111', 2)
        two_code_max = int('0b11011111', 2)
        three_code_max = int('0b11101111', 2)
        four_code_max = int('0b11110111', 2)

        def get_type(num):
            if num <= one_code_max:
                return 0
            elif num <= follow_code_max:
                return -1
            elif num <= two_code_max:
                return 1
            elif num <= three_code_max:
                return 2
            elif num <= four_code_max:
                return 3
            else:
                return None
        
        follow_count = 0
        for num in data:
            code_type = get_type(num)
            if code_type == None: # 포맷에 없는 코드
                return False
            if follow_count > 0 and code_type >= 0: # 아직 처리해야 할 부분이 있는데 또 코드가 시작된 경우 False
                return False
            follow_count += code_type
            if follow_count < 0: # 새 코드가 시작되지 않고 부분 코드만 계속 나온 경우 False
                return False
        if follow_count == 0:
            return True
        return False
            
Solution().validUtf8([235,140,4])