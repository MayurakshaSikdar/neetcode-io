# https://neetcode.io/problems/longest-substring-without-duplicates

# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            return len(set(s))
        l = 0
        longest_substr = set()
        max_count = 0
        for r in range(len(s)):
            while s[r] in longest_substr:
                longest_substr.remove(s[l])
                l += 1
            longest_substr.add(s[r])
            max_count = max(max_count, r-l+1)
        return max_count

print(Solution().lengthOfLongestSubstring("cddd"))
print(Solution().lengthOfLongestSubstring("xxxx"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("aab"))