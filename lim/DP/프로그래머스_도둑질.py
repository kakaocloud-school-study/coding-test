'''
첫집을 턴 경우와 첫집을 털지 않은 경우를 둘로 나눠서 푼다
'''


def solution(money):
    def rob(nums):
        if len(nums) < 2:
            return nums[-1]
        
        dp1 = [0] * (len(nums))
        dp2 = [0] * (len(nums))
        dp1[0] = nums[0]
        dp2[0] = 0
        dp1[1] = nums[1]
        dp2[1] = dp1[0]
        for i in range(2, len(nums)):
            dp1[i] = dp2[i-1] + nums[i]
            dp2[i] = max(dp1[i-1], dp2[i-1])
        
        return max(dp1[-1], dp2[-1])
    if len(money) < 4:
        return max(money)
    rob_first = rob(money[2:-1]) + money[0]
    rob_except_first = rob(money[1:])
    return max(rob_first, rob_except_first)