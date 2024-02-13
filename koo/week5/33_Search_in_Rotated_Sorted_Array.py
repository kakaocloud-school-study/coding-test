from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        nums = nums[pivot:] + nums[:pivot]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return pivot + mid if pivot + mid < len(nums) else pivot + mid - len(nums)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1