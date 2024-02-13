from bisect import bisect_left


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res:Set[int] = set()
        nums2.sort()

        for num in nums1:
            idx = bisect_left(nums2, num)
            if len(nums2) > 0 and len(nums2) > idx and num == nums2[idx]:
                res.add(num)
        return list(res)