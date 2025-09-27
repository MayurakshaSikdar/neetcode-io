# https://neetcode.io/problems/max-water-container

# Container With Most Water
# You are given an integer array heights where heights[i] represents the height of the `i` bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4
# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        left, right = 0, len(heights) - 1
        while left < right:
            container = (right-left) * min(heights[left], heights[right])
            max_container = max(container, max_container)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_container

print(Solution().maxArea([1,7,2,5,4,7,3,6]))
print(Solution().maxArea([2,2,2]))