# https://neetcode.io/problems/sliding-window-maximum

# Sliding Window Maximum
# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6
# Constraints:

# 1 <= nums.length <= 1000
# -10,000 <= nums[i] <= 10,000
# 1 <= k <= nums.length

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == k:
            return [max(nums)]
        if k == 1:
            return nums
        i, j = 0, k
        max_index = nums[i:k].index(max(nums[i:k]))
        result = []
        result.append(nums[max_index])
        i += 1
        while j < n:
            if i <= max_index and max_index <= j:
                if nums[j] >= nums[max_index]:
                    max_index = j
            else:
                max_index = i + nums[i:i+k].index(max(nums[i:i+k]))

            result.append(nums[max_index])
            i += 1
            j += 1
        return result