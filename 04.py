from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 3, 5, 6]
target1 = 5
output1 = solution.searchInsert(nums1, target1)
print(output1)  # Output: 2

# Example 2
nums2 = [1, 3, 5, 6]
target2 = 2
output2 = solution.searchInsert(nums2, target2)
print(output2)  # Output: 1

# Example 3
nums3 = [1, 3, 5, 6]
target3 = 7
output3 = solution.searchInsert(nums3, target3)
print(output3)  # Output: 4
