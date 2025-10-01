# https://neetcode.io/problems/median-of-two-sorted-arrays


# Median of Two Sorted Arrays
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in O(log(m+n)) time.

# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:

# Input: nums1 = [1,3], nums2 = [2,4]

# Output: 2.5
# Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# -10^6 <= nums1[i], nums2[i] <= 10^6

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        n, m = len(nums1), len(nums2)
        i = j = 0
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < n:
            nums.extend(nums1[i:])
        if j < m:
            nums.extend(nums2[j:])
        if len(nums) % 2 == 1:
            return float(nums[len(nums)//2])
        return (nums[len(nums)//2] + nums[len(nums)//2-1]) / 2

print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3]))
print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4]))
print(Solution().findMedianSortedArrays(nums1 = [1,3,5,6,7], nums2 = [2,4,5,6]))