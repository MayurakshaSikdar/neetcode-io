# https://neetcode.io/problems/permutation-string

# Permutation in String
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false
# Constraints:

# 1 <= s1.length, s2.length <= 1000

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if len(s1) == 1 and s1 in s2: return True
        frequency = Counter(s1)
        distinct_char = len(frequency)
        for i in range(len(s2)):
            count, current = {}, 0
            for j in range(i, len(s2)):
                count[s2[j]] = 1 + count.get(s2[j], 0)
                if frequency.get(s2[j], 0) < count[s2[j]]:
                    break
                if frequency.get(s2[j], 0) == count[s2[j]]:
                    current += 1
                if current == distinct_char:
                    return True
        return False

print(Solution().checkInclusion(s1 = "abc", s2 = "lecabee"))
print(Solution().checkInclusion(s1 = "abc", s2 = "lecaabee"))