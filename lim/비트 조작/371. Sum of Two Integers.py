'''
더하기 회로 원리랑 같음
음수는 이진수 가장 큰 자리수에 1인 수
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_digit = 12
        all_mask = int('0b111111111111', 2)
        sign_digit = int('0b100000000000', 2)
        def sum_unsigned(a, b):
            result = 0
            for i in range(max_digit):
                window = 1 << i
                if (a & window) and (b & window) and (result & window): # 111
                    result |= (window << 1)
                    result |= window
                elif (not (a & window)) and (not (b & window)) and (not (result & window)): # 000
                    continue
                elif (not (a & window)) ^ (not (b & window)) ^ (not (result & window)): # 110
                    result |= (window << 1)
                    result |= window
                    result ^= window
                elif (a & window) ^ (b & window) ^ (result & window): # 100
                    result |= window
            result &= all_mask
            return result
        def toggle_sign(num):
            num = all_mask ^ num
            num = sum_unsigned(num, 1)
            return num
        def to_unsigned(num):
            if num >= 0:
                return num
            else:
                num = -num
            return toggle_sign(num)
        a = to_unsigned(a)
        b = to_unsigned(b)
        result = sum_unsigned(a, b)
        if result & sign_digit:
            result = toggle_sign(result)
            result = -result
        return result

Solution().getSum(-12, -8)
Solution().getSum(2, 3)
Solution().getSum(1, 2)
'''
 100
 101
1001

 1011
 1001
10100

 0001
 1111
10000

 1111
 1111
11110
00010

'0b001111101000' 1000
'0b110000011000' -1000
'0b100000110000' -2000

'0b111111111111' -1
'0b111111111110' -2
'''