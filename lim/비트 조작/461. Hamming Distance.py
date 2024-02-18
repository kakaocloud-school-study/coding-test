class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(list(map(int, bin(x ^ y)[2:])))