# https://neetcode.io/problems/trapping-rain-water

# Trapping Rain Water
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:

# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9
# Constraints:

# 1 <= height.length <= 1000
# 0 <= height[i] <= 1000

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                water += right_max - height[right]
        return water

print(Solution().trap([0,2,0,3,1,0,1,3,2,1]))