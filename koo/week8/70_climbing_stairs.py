class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b, c = 1, 2, 3
        for i in range(3, n):
            a, b, c = b, c, b + c
        return c