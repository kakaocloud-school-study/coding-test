'''
리스트 슬라이싱을 사용하면 슬라이싱 범위만큼 선형 시간 소비되므로 bisect 라이브러리를 사용할 수 없고 직접구현 필요
1. 원본 첫번째 원소 찾는 함수
2. 첫 원소를 기점으로 나눠진 두 정렬 범위 중에 타겟이 있는 범위에서 이진탐색
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_first():
            left = 0
            right = len(nums) - 1
            first = 0
            while left <= right:
                mid = (left + right) // 2
                if nums[first] > nums[mid]:
                        first = mid
                if nums[left] <= nums[mid] and nums[mid] > nums[right]:
                    left = mid + 1
                    if nums[first] > nums[left]:
                        first = left
                elif nums[left] > nums[mid] and nums[mid] < nums[right]:
                    right = mid - 1
                    if nums[first] > nums[right]:
                        first = right
                else:
                    break
            return first
        
        def search(s, e):
            left = s
            right = e
            answer = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    answer = mid
                    break
            return answer


        first = find_first()

        if nums[0] <= target and first != 0:
            return search(0, first)
        else:
            return search(first, len(nums) - 1)

Solution().search([3, 1], 3)
